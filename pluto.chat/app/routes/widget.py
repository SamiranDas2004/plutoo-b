from fastapi import APIRouter, Depends, HTTPException, Response, Form
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.db.session import get_db
from app.db.models import User
from app.utils.auth_middleware import get_current_user
import os
import secrets

router = APIRouter()



@router.get("/iframe/widget.html")
def get_widget_html():
    """Serve widget HTML directly"""
    html_content = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat Widget</title>
    <style>
        body { margin: 0; padding: 10px; font-family: Arial, sans-serif; background: #fff; }
        #chat-box { height: 480px; display: flex; flex-direction: column; }
        #messages { flex: 1; overflow-y: auto; padding: 10px; border: 1px solid #ddd; border-radius: 8px; margin-bottom: 10px; background: #fafafa; }
        #input-area { display: flex; gap: 8px; }
        #chat-input { flex: 1; padding: 10px; border: 1px solid #ddd; border-radius: 6px; outline: none; }
        #send-btn { padding: 10px 20px; background: #4f46e5; color: white; border: none; border-radius: 6px; cursor: pointer; }
        #send-btn:hover { background: #4338ca; }
        #send-btn:disabled { background: #ccc; cursor: not-allowed; }
        .message { margin: 8px 0; padding: 10px; border-radius: 8px; max-width: 80%; }
        .user-msg { background: #e3f2fd; margin-left: auto; text-align: right; }
        .bot-msg { background: #f5f5f5; margin-right: auto; }
    </style>
</head>
<body>
<div id="chat-box">
    <div id="messages"></div>
    <div id="input-area">
        <input type="text" id="chat-input" placeholder="Type your message..." autocomplete="off" />
        <button type="button" id="send-btn">Send</button>
    </div>
</div>
<script>
(function() {
const urlParams = new URLSearchParams(window.location.search);
const botToken = urlParams.get("bot_token");
const sessionId = urlParams.get("session_id");
const API_URL = "http://localhost:8000/chat/";
const messagesDiv = document.getElementById("messages");
const input = document.getElementById("chat-input");
const sendBtn = document.getElementById("send-btn");
let isSending = false;

function addMessage(text, type) {
    const msg = document.createElement("div");
    msg.className = "message " + type;
    msg.textContent = text;
    messagesDiv.appendChild(msg);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

async function sendMessage(e) {
    if (e) e.preventDefault();
    if (isSending) return false;
    const text = input.value.trim();
    if (!text) return false;
    
    isSending = true;
    addMessage(text, "user-msg");
    input.value = "";
    sendBtn.disabled = true;
    
    try {
        const res = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ bot_token: botToken, session_id: sessionId, message: text })
        });
        
        if (res.ok) {
            const data = await res.json();
            addMessage(data.reply, "bot-msg");
        } else {
            addMessage("Sorry, something went wrong.", "bot-msg");
        }
    } catch (error) {
        addMessage("Sorry, something went wrong.", "bot-msg");
    } finally {
        isSending = false;
        sendBtn.disabled = false;
        input.focus();
    }
    return false;
}

sendBtn.onclick = sendMessage;
input.onkeypress = (e) => { if (e.key === "Enter") { e.preventDefault(); sendMessage(e); } };
})();
</script>
</body>
</html>
    '''
    
    response = HTMLResponse(content=html_content)
    response.headers["Cache-Control"] = "no-store"
    response.headers["X-Frame-Options"] = "ALLOWALL"
    return response

@router.get("/config/{bot_token}")
def get_widget_config(bot_token: str, db: Session = Depends(get_db)):
    """Public endpoint - Widget fetches its config using bot_token"""
    user = db.query(User).filter(User.bot_token == bot_token).first()
    if not user:
        raise HTTPException(status_code=404, detail="Invalid bot token")
    
    return {
        "primaryColor": user.widget_primary_color or "#007bff",
        "textColor": user.widget_text_color or "#ffffff",
        "fontFamily": user.widget_font_family or "Arial, sans-serif",
        "position": user.widget_position or "bottom-right",
        "welcomeMessage": user.widget_welcome_message or "Hi! How can I help you today?"
    }

@router.get("/settings")
def get_widget_settings(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get widget settings for the authenticated user"""
    user_id = user["id"]
    
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "botToken": db_user.bot_token,
        "primaryColor": db_user.widget_primary_color or "#007bff",
        "textColor": db_user.widget_text_color or "#ffffff",
        "fontFamily": db_user.widget_font_family or "Arial, sans-serif",
        "position": db_user.widget_position or "bottom-right",
        "welcomeMessage": db_user.widget_welcome_message or "Hi! How can I help you today?"
    }

@router.post("/customize")
def update_widget_customization(
    primary_color: str = Form(...),
    text_color: str = Form(...),
    font_family: str = Form(...),
    position: str = Form(...),
    welcome_message: str = Form(...),
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update widget customization settings"""
    import re
    print("Updating widget customization...", primary_color, text_color, font_family, position, welcome_message)
    
    # Validate hex colors
    if not re.match(r'^#[0-9A-Fa-f]{6}$', primary_color):
        raise HTTPException(status_code=400, detail="Invalid primary color format")
    if not re.match(r'^#[0-9A-Fa-f]{6}$', text_color):
        raise HTTPException(status_code=400, detail="Invalid text color format")
    
    # Validate position
    if position not in ["bottom-right", "bottom-left"]:
        raise HTTPException(status_code=400, detail="Invalid position")
    
    # Validate welcome message length
    if len(welcome_message) > 500:
        raise HTTPException(status_code=400, detail="Welcome message too long")
    
    user_id = user["id"]
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update settings
    db_user.widget_primary_color = primary_color
    db_user.widget_text_color = text_color
    db_user.widget_font_family = font_family
    db_user.widget_position = position
    db_user.widget_welcome_message = welcome_message
    
    db.commit()
    
    return {"success": True, "message": "Widget customization updated successfully"}

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