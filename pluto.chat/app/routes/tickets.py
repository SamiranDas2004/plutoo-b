import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from app.db.session import get_db
from app.db.models import User, Ticket
from datetime import datetime

router = APIRouter()

class TicketRequest(BaseModel):
    bot_token: str
    session_id: str
    name: str
    email: EmailStr
    phone: str | None = None
    issue: str

def send_email_notification(to_email: str, ticket_id: str, visitor_name: str, visitor_email: str, issue: str):
    """Send email notification using SMTP (Gmail or Brevo)"""
    smtp_email = os.getenv("SMTP_EMAIL")
    smtp_password = os.getenv("SMTP_PASSWORD")
    smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    
    if not smtp_email or not smtp_password:
        print("Warning: SMTP credentials not configured. Email not sent.")
        return False
    
    try:
        msg = MIMEMultipart()
        msg['From'] = smtp_email
        msg['To'] = to_email
        msg['Subject'] = f"New Support Ticket #{ticket_id}"
        
        body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <h2 style="color: #4f46e5;">🎫 New Support Ticket Received</h2>
            <div style="background: #f9fafb; padding: 20px; border-radius: 8px; margin: 20px 0;">
                <p><strong>Ticket ID:</strong> {ticket_id}</p>
                <p><strong>Visitor Name:</strong> {visitor_name}</p>
                <p><strong>Visitor Email:</strong> {visitor_email}</p>
                <hr style="border: 1px solid #e5e7eb; margin: 15px 0;">
                <p><strong>Issue Description:</strong></p>
                <p style="background: white; padding: 15px; border-radius: 4px; border-left: 4px solid #4f46e5;">
                    {issue}
                </p>
            </div>
            <p style="color: #6b7280; font-size: 14px;">
                Please respond to the visitor at: <a href="mailto:{visitor_email}">{visitor_email}</a>
            </p>
        </body>
        </html>
        """
        
        msg.attach(MIMEText(body, 'html'))
        
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_email, smtp_password)
            server.send_message(msg)
        
        print(f"✅ Email sent successfully to {to_email}")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

@router.post("/create")
async def create_ticket(req: TicketRequest, db: Session = Depends(get_db)):
    """Create a new support ticket and send email notification"""
    
    # Validate bot token
    user = db.query(User).filter(User.bot_token == req.bot_token).first()
    if not user:
        raise HTTPException(status_code=404, detail="Invalid bot token")
    
    # Generate unique ticket ID
    ticket_id = f"TKT-{datetime.now().strftime('%Y%m%d')}-{db.query(Ticket).count() + 1:04d}"
    
    # Create ticket in database
    ticket = Ticket(
        ticket_id=ticket_id,
        user_id=user.id,
        session_id=req.session_id,
        visitor_name=req.name,
        visitor_email=req.email,
        visitor_phone=req.phone,
        issue=req.issue,
        status="open"
    )
    
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    
    # Send email notification to bot owner
    send_email_notification(
        to_email=user.email,
        ticket_id=ticket_id,
        visitor_name=req.name,
        visitor_email=req.email,
        issue=req.issue
    )
    
    return {
        "success": True,
        "ticket_id": ticket_id,
        "message": "Ticket created successfully"
    }

@router.get("/list")
async def list_tickets(db: Session = Depends(get_db)):
    """Get all tickets (for dashboard)"""
    tickets = db.query(Ticket).order_by(Ticket.created_at.desc()).all()
    return {"tickets": tickets}
