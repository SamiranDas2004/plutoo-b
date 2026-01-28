import secrets
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.db.session import get_db
from app.db.models import User
from app.utils.jwt_handler import create_access_token
from app.services.pinecone_client import index
from app.utils.auth_middleware import get_current_user
from passlib.context import CryptContext




router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class SignupRequest(BaseModel):
    email: str
    password: str


def hash_password(password: str):
    return pwd_context.hash(password)


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.db.session import get_db
from app.db.models import User
from app.utils.jwt_handler import create_access_token
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class SignupRequest(BaseModel):
    full_name: str
    email: str
    company_name: str
    password: str


def hash_password(password: str):
    return pwd_context.hash(password)


@router.post("/signup")
def signup(body: SignupRequest, db: Session = Depends(get_db)):
    email = body.email
    password = body.password
    full_name = body.full_name
    company_name = body.company_name

    # Check if user already exists
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Generate bot token for tenant chat identification
    bot_token = secrets.token_urlsafe(32)

    # Create user record (namespace blank for now)
    user = User(
        full_name=full_name,
        email=email,
        company_name=company_name,
        hashed_password=hash_password(password),
        pinecone_namespace="",
        bot_token=bot_token
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    # Now assign Pinecone namespace = user ID
    namespace = str(user.id)
    user.pinecone_namespace = namespace
    db.commit()

    return {
        "message": "User created successfully",
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "company_name": user.company_name,
            "namespace": namespace,
            "bot_token": bot_token
        }
    }


class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/login")
def login(body: LoginRequest, db: Session = Depends(get_db)):
    email = body.email
    password = body.password

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not pwd_context.verify(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    # Generate JWT
    token = create_access_token({
    "id": str(user.id),
    "email": user.email
    })


    return {
        "message": "Login successful",
        "token": token,
        "user": {
            "id": user.id,
            "email": user.email,
            "namespace": user.pinecone_namespace
        }
    }


class ProfileUpdateRequest(BaseModel):
    name: str = None
    email: str = None
    password: str = None


@router.put("/profile")
def update_profile(
    body: ProfileUpdateRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update user profile"""
    user_id = user["id"]
    
    # Get user from database
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update fields if provided
    if body.email:
        # Check if email is already taken
        existing = db.query(User).filter(User.email == body.email, User.id != user_id).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email already in use")
        db_user.email = body.email
    
    if body.password:
        db_user.hashed_password = hash_password(body.password)
    
    db.commit()
    db.refresh(db_user)
    
    return {
        "message": "Profile updated successfully",
        "user": {
            "id": db_user.id,
            "email": db_user.email
        }
    }


@router.post("/logout")
def logout():
    """Logout endpoint (client-side token removal)"""
    return {"message": "Logged out successfully"}