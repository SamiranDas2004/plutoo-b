import secrets
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from pydantic import BaseModel, validator
from app.db.session import get_db
from app.db.models import User
from app.utils.jwt_handler import create_access_token
from app.utils.auth_middleware import get_current_user
from passlib.context import CryptContext
from slowapi import Limiter
from slowapi.util import get_remote_address
from app.utils.validators import validate_email, validate_password

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
limiter = Limiter(key_func=get_remote_address)


class SignupRequest(BaseModel):
    email: str
    password: str
    
    @validator('email')
    def validate_email_field(cls, v):
        return validate_email(v)
    
    @validator('password')
    def validate_password_field(cls, v):
        return validate_password(v)


class LoginRequest(BaseModel):
    email: str
    password: str
    
    @validator('email')
    def validate_email_field(cls, v):
        return validate_email(v)


def hash_password(password: str):
    return pwd_context.hash(password)


@router.post("/signup")
@limiter.limit("5/minute")
def signup(request: Request, body: SignupRequest, db: Session = Depends(get_db)):
    from app.utils.audit_logger import AuditLogger, get_client_ip
    
    email = body.email
    password = body.password
    client_ip = get_client_ip(request)

    # Check if user already exists
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        AuditLogger.log_auth_attempt(email, False, client_ip, "signup", "Email already registered")
        raise HTTPException(status_code=400, detail="Email already registered")

    # Generate bot token for tenant chat identification
    bot_token = secrets.token_urlsafe(32)

    # Create user record (namespace blank for now)
    user = User(
        email=email,
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
    
    # Log successful signup
    AuditLogger.log_auth_attempt(email, True, client_ip, "signup")

    return {
        "message": "User created successfully",
        "user": {
            "id": user.id,
            "email": user.email,
            "namespace": namespace,
            "bot_token": bot_token
        }
    }


@router.post("/login")
@limiter.limit("10/minute")
def login(request: Request, body: LoginRequest, db: Session = Depends(get_db)):
    from app.utils.audit_logger import AuditLogger, get_client_ip
    
    email = body.email
    password = body.password
    client_ip = get_client_ip(request)

    user = db.query(User).filter(User.email == email).first()
    if not user:
        AuditLogger.log_auth_attempt(email, False, client_ip, "login", "User not found")
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not pwd_context.verify(password, user.hashed_password):
        AuditLogger.log_auth_attempt(email, False, client_ip, "login", "Invalid password")
        raise HTTPException(status_code=400, detail="Invalid email or password")

    # Generate JWT
    token = create_access_token({
        "id": str(user.id),
        "email": user.email
    })
    
    # Log successful login
    AuditLogger.log_auth_attempt(email, True, client_ip, "login")

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
    
    @validator('email')
    def validate_email_field(cls, v):
        if v:
            return validate_email(v)
        return v
    
    @validator('password')
    def validate_password_field(cls, v):
        if v:
            return validate_password(v)
        return v


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
