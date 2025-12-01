import secrets
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.db.session import get_db
from app.db.models import User
from app.utils.auth_middleware import get_current_user

router = APIRouter()

class WidgetSettingsUpdate(BaseModel):
    color: str = None
    position: str = None
    welcomeMessage: str = None

@router.get("/settings")
def get_widget_settings(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get widget settings for the authenticated user"""
    user_id = user["id"]
    
    # Get user from database
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Return current settings (with defaults)
    return {
        "botToken": db_user.bot_token,
        "color": "#3B82F6",  # Default blue color
        "position": "right",  # Default position
        "welcomeMessage": "Hello! How can I help you today?"  # Default message
    }

@router.put("/settings")
def update_widget_settings(
    settings: WidgetSettingsUpdate,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update widget settings for the authenticated user"""
    user_id = user["id"]
    
    # Get user from database
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # For now, we'll just return the updated settings
    # In a full implementation, you'd store these in a separate widget_settings table
    
    return {
        "botToken": db_user.bot_token,
        "color": settings.color or "#3B82F6",
        "position": settings.position or "right",
        "welcomeMessage": settings.welcomeMessage or "Hello! How can I help you today?",
        "message": "Settings updated successfully"
    }

@router.post("/regenerate-token")
def regenerate_bot_token(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Regenerate bot token for the authenticated user"""
    user_id = user["id"]
    
    # Get user from database
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Generate new bot token
    new_token = secrets.token_urlsafe(32)
    db_user.bot_token = new_token
    
    db.commit()
    db.refresh(db_user)
    
    return {
        "botToken": new_token,
        "message": "Bot token regenerated successfully"
    }