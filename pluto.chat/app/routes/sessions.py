from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from app.db.session import get_db
from app.db.models import ChatSession, ChatMessage
from app.utils.auth_middleware import get_current_user
from typing import List

router = APIRouter()

@router.get("/")
def list_sessions(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List all chat sessions for the authenticated user"""
    user_id = user["id"]
    
    # Get sessions with message counts and last message time
    sessions = db.query(
        ChatSession.id,
        ChatSession.session_id,
        ChatSession.created_at,
        func.count(ChatMessage.id).label('message_count'),
        func.max(ChatMessage.created_at).label('last_message_at')
    ).outerjoin(
        ChatMessage, ChatSession.session_id == ChatMessage.session_id
    ).filter(
        ChatSession.user_id == user_id
    ).group_by(
        ChatSession.id, ChatSession.session_id, ChatSession.created_at
    ).order_by(desc(ChatSession.created_at)).all()
    
    result = []
    for session in sessions:
        result.append({
            "id": session.session_id,
            "visitorId": session.session_id,
            "visitorName": f"Visitor {session.session_id[:8]}",
            "startedAt": session.created_at.isoformat(),
            "lastMessageAt": session.last_message_at.isoformat() if session.last_message_at else session.created_at.isoformat(),
            "messageCount": session.message_count or 0
        })
    
    return result

@router.get("/{session_id}")
def get_session(
    session_id: str,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get specific session details"""
    user_id = user["id"]
    
    session = db.query(ChatSession).filter(
        ChatSession.session_id == session_id,
        ChatSession.user_id == user_id
    ).first()
    
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    # Get message count and last message time
    message_stats = db.query(
        func.count(ChatMessage.id).label('message_count'),
        func.max(ChatMessage.created_at).label('last_message_at')
    ).filter(ChatMessage.session_id == session_id).first()
    
    return {
        "id": session.session_id,
        "visitorId": session.session_id,
        "visitorName": f"Visitor {session.session_id[:8]}",
        "startedAt": session.created_at.isoformat(),
        "lastMessageAt": message_stats.last_message_at.isoformat() if message_stats.last_message_at else session.created_at.isoformat(),
        "messageCount": message_stats.message_count or 0
    }

@router.get("/{session_id}/messages")
def get_session_messages(
    session_id: str,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all messages for a specific session"""
    user_id = user["id"]
    
    # Verify session belongs to user
    session = db.query(ChatSession).filter(
        ChatSession.session_id == session_id,
        ChatSession.user_id == user_id
    ).first()
    
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    # Get messages
    messages = db.query(ChatMessage).filter(
        ChatMessage.session_id == session_id
    ).order_by(ChatMessage.created_at.asc()).all()
    
    result = []
    for msg in messages:
        result.append({
            "id": str(msg.id),
            "sessionId": msg.session_id,
            "sender": "user" if msg.sender == "visitor" else "bot",
            "content": msg.message,
            "timestamp": msg.created_at.isoformat()
        })
    
    return result