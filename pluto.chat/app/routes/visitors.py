from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func, distinct, desc
from app.db.session import get_db
from app.db.models import ChatSession, ChatMessage
from app.utils.auth_middleware import get_current_user

router = APIRouter()

@router.get("/")
def list_visitors(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List all visitors (unique session IDs) for the authenticated user"""
    user_id = user["id"]
    
    # Get unique visitors with their stats
    visitors = db.query(
        ChatSession.session_id,
        ChatSession.created_at,
        func.count(ChatMessage.id).label('total_messages'),
        func.max(ChatMessage.created_at).label('last_active')
    ).outerjoin(
        ChatMessage, ChatSession.session_id == ChatMessage.session_id
    ).filter(
        ChatSession.user_id == user_id
    ).group_by(
        ChatSession.session_id, ChatSession.created_at
    ).order_by(desc(ChatSession.created_at)).all()
    
    result = []
    for visitor in visitors:
        result.append({
            "id": visitor.session_id,
            "name": f"Visitor {visitor.session_id[:8]}",
            "email": None,  # We don't collect emails in current implementation
            "totalMessages": visitor.total_messages or 0,
            "createdAt": visitor.created_at.isoformat(),
            "lastActive": visitor.last_active.isoformat() if visitor.last_active else visitor.created_at.isoformat()
        })
    
    return result

@router.get("/{visitor_id}")
def get_visitor(
    visitor_id: str,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get specific visitor details"""
    user_id = user["id"]
    
    # Get visitor session
    session = db.query(ChatSession).filter(
        ChatSession.session_id == visitor_id,
        ChatSession.user_id == user_id
    ).first()
    
    if not session:
        raise HTTPException(status_code=404, detail="Visitor not found")
    
    # Get message stats
    message_stats = db.query(
        func.count(ChatMessage.id).label('total_messages'),
        func.max(ChatMessage.created_at).label('last_active')
    ).filter(ChatMessage.session_id == visitor_id).first()
    
    return {
        "id": visitor_id,
        "name": f"Visitor {visitor_id[:8]}",
        "email": None,
        "totalMessages": message_stats.total_messages or 0,
        "createdAt": session.created_at.isoformat(),
        "lastActive": message_stats.last_active.isoformat() if message_stats.last_active else session.created_at.isoformat()
    }