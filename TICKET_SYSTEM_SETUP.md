# Ticket System Setup Guide

## Overview
The ticket system allows visitors to raise support tickets directly from the chat widget. When a ticket is created:
1. It's stored in the database
2. An email notification is sent to the bot owner

## Database Setup

Run the SQL migration to create the tickets table:

```bash
# Connect to your database and run:
mysql -u root -p plutochat < pluto.chat/create_tickets_table.sql
```

Or use Python:
```bash
cd pluto.chat
python -c "from app.db.database import engine; from app.db.models import Base; Base.metadata.create_all(bind=engine)"
```

## Email Configuration (Gmail - FREE)

### Step 1: Enable 2-Factor Authentication
1. Go to your Google Account: https://myaccount.google.com/
2. Navigate to Security
3. Enable 2-Step Verification

### Step 2: Generate App Password
1. Go to: https://myaccount.google.com/apppasswords
2. Select "Mail" and "Other (Custom name)"
3. Name it "PlutoChat"
4. Click "Generate"
5. Copy the 16-character password

### Step 3: Update .env File
Add these lines to your `.env` file:

```env
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=xxxx xxxx xxxx xxxx  # The 16-character app password
```

## Testing the Ticket System

1. Start your FastAPI server:
```bash
cd pluto.chat
uvicorn main:app --reload --port 8000
```

2. Open `test.html` in your browser

3. In the chat widget, type something like:
   - "I need help with my account"
   - "Can you raise a support ticket?"
   - "I want to create a ticket"

4. Click the "🎫 Raise Support Ticket" button

5. Fill in the form and submit

6. Check:
   - Database: `SELECT * FROM tickets;`
   - Email: Check the bot owner's inbox

## Ticket Fields

- **ticket_id**: Unique ID (format: TKT-YYYYMMDD-0001)
- **visitor_name**: Name of the person raising the ticket
- **visitor_email**: Email for follow-up
- **visitor_phone**: Optional phone number
- **issue**: Description of the problem
- **status**: open/closed/pending
- **session_id**: Links to the chat session

## Email Notification

The bot owner receives an email with:
- Ticket ID
- Visitor contact information
- Issue description
- Direct reply link to visitor's email

## Troubleshooting

### Email not sending?
- Verify SMTP credentials in .env
- Check if 2FA is enabled on Gmail
- Ensure you're using App Password, not regular password
- Check spam folder

### Ticket not saving?
- Verify database connection
- Run the migration script
- Check FastAPI logs for errors

### Button not appearing?
- The bot must mention "support ticket", "raise ticket", or "create ticket" in its response
- Check browser console for JavaScript errors
