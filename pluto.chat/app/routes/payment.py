import os
import razorpay
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.db.session import get_db
from app.db.models import User
import secrets
import hmac
import hashlib

router = APIRouter()

RAZORPAY_KEY = os.getenv("RAZORPAY_KEY")
RAZORPAY_SECRET = os.getenv("RAZORPAY_SECRET")

razorpay_client = razorpay.Client(auth=(RAZORPAY_KEY, RAZORPAY_SECRET))


class PaymentRequest(BaseModel):
    amount: int  # in paise (₹499 = 49900 paise)
    plan_name: str
    email: str


class PaymentVerifyRequest(BaseModel):
    razorpay_order_id: str
    razorpay_payment_id: str
    razorpay_signature: str
    email: str
    plan_name: str


@router.post("/create-order")
def create_payment_order(body: PaymentRequest, db: Session = Depends(get_db)):
    """Create Razorpay order - Check if user exists first"""
    try:
        # Check if user exists
        user = db.query(User).filter(User.email == body.email).first()
        if not user:
            raise HTTPException(
                status_code=404, 
                detail="Account not found. Please create an account first."
            )
        
        # Create order
        order_data = {
            "amount": body.amount,
            "currency": "INR",
            "payment_capture": 1,
            "notes": {
                "plan": body.plan_name,
                "email": body.email,
                "user_id": user.id
            }
        }
        
        order = razorpay_client.order.create(data=order_data)
        
        return {
            "order_id": order["id"],
            "amount": order["amount"],
            "currency": order["currency"],
            "key": RAZORPAY_KEY
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/verify-payment")
def verify_payment(body: PaymentVerifyRequest, db: Session = Depends(get_db)):
    """Verify payment and upgrade user account"""
    try:
        # Verify signature
        generated_signature = hmac.new(
            RAZORPAY_SECRET.encode(),
            f"{body.razorpay_order_id}|{body.razorpay_payment_id}".encode(),
            hashlib.sha256
        ).hexdigest()
        
        if generated_signature != body.razorpay_signature:
            raise HTTPException(status_code=400, detail="Invalid payment signature")
        
        # Get user
        user = db.query(User).filter(User.email == body.email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Determine user type based on plan
        user_type = "free"
        if body.plan_name.lower() == "professional":
            user_type = "paid"
        elif body.plan_name.lower() == "enterprise":
            user_type = "premium"
        
        # Update user with payment info
        user.user_type = user_type
        user.payment_id = body.razorpay_payment_id
        user.order_id = body.razorpay_order_id
        db.commit()
        db.refresh(user)
        
        return {
            "message": "Payment verified and account upgraded",
            "user": {
                "id": user.id,
                "email": user.email,
                "user_type": user_type,
                "bot_token": user.bot_token
            }
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/plans")
def get_plans():
    """Get available plans"""
    return {
        "plans": [
            {
                "name": "Starter",
                "price": 0,
                "type": "free",
                "features": ["1,000 AI responses/month", "Basic analytics", "Email support"]
            },
            {
                "name": "Professional",
                "price": 49900,  # ₹499 in paise
                "type": "paid",
                "features": ["10,000 AI responses/month", "Advanced analytics", "Priority support"]
            },
            {
                "name": "Enterprise",
                "price": 149900,  # ₹1499 in paise
                "type": "premium",
                "features": ["Unlimited responses", "Custom analytics", "Dedicated manager"]
            }
        ]
    }
