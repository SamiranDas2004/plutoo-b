from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, distinct
from app.db.session import get_db
from app.db.models import User, ChatSession, ChatMessage
from app.utils.auth_middleware import get_current_user
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/dashboard")
def get_dashboard_stats(
    days: int = 7,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get dashboard analytics for the authenticated user"""
    user_id = user["id"]
    
    # Get today's date range
    today_start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    today_end = datetime.now().replace(hour=23, minute=59, second=59, microsecond=999999)
    
    # Count unique sessions today (visitors today)
    visitors_today = db.query(func.count(distinct(ChatSession.session_id))).filter(
        ChatSession.user_id == user_id,
        ChatSession.created_at >= today_start,
        ChatSession.created_at <= today_end
    ).scalar() or 0
    
    # Messages today
    messages_today = db.query(func.count(ChatMessage.id)).join(
        ChatSession, ChatMessage.session_id == ChatSession.session_id
    ).filter(
        ChatSession.user_id == user_id,
        ChatMessage.created_at >= today_start,
        ChatMessage.created_at <= today_end
    ).scalar() or 0
    
    # Total messages for this user
    total_messages = db.query(func.count(ChatMessage.id)).join(
        ChatSession, ChatMessage.session_id == ChatSession.session_id
    ).filter(ChatSession.user_id == user_id).scalar() or 0
    
    # Total sessions for this user
    total_sessions = db.query(func.count(ChatSession.id)).filter(
        ChatSession.user_id == user_id
    ).scalar() or 0
    
    # Documents count from database
    from app.db.models import Document
    documents_count = db.query(func.count(Document.id)).filter(
        Document.user_id == user_id
    ).scalar() or 0
    
    # Get chart data for specified days
    chart_data = []
    for i in range(days - 1, -1, -1):
        day = datetime.now() - timedelta(days=i)
        day_start = day.replace(hour=0, minute=0, second=0, microsecond=0)
        day_end = day.replace(hour=23, minute=59, second=59, microsecond=999999)
        
        # Count visitors for this day
        day_visitors = db.query(func.count(distinct(ChatSession.session_id))).filter(
            ChatSession.user_id == user_id,
            ChatSession.created_at >= day_start,
            ChatSession.created_at <= day_end
        ).scalar() or 0
        
        # Count messages for this day
        day_messages = db.query(func.count(ChatMessage.id)).join(
            ChatSession, ChatMessage.session_id == ChatSession.session_id
        ).filter(
            ChatSession.user_id == user_id,
            ChatMessage.created_at >= day_start,
            ChatMessage.created_at <= day_end
        ).scalar() or 0
        
        chart_data.append({
            "date": day.strftime("%Y-%m-%d"),
            "visitors": day_visitors,
            "messages": day_messages
        })
    
    return {
        "visitorsToday": visitors_today,
        "messagesToday": messages_today,
        "totalMessages": total_messages,
        "totalSessions": total_sessions,
        "documentsCount": documents_count,
        "chartData": chart_data
    }