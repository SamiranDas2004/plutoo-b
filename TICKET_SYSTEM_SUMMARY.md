# Ticket System Implementation Summary

## ✅ What Was Implemented

### 1. Database Model
- Updated `Ticket` model in [models.py](pluto.chat/app/db/models.py)
- Fields: ticket_id, user_id, session_id, visitor_name, visitor_email, visitor_phone, issue, status
- Created migration script: [create_tickets_table.sql](pluto.chat/create_tickets_table.sql)

### 2. Backend API
- Created [tickets.py](pluto.chat/app/routes/tickets.py) route
- Endpoint: `POST /tickets/create`
- Validates bot_token
- Generates unique ticket IDs (format: TKT-YYYYMMDD-0001)
- Stores tickets in database
- Sends email notifications

### 3. Email Notifications
- Uses Gmail SMTP (FREE)
- Sends HTML-formatted emails to bot owner
- Includes ticket details and visitor contact info
- Requires Gmail App Password (not regular password)

### 4. Configuration
- Updated [.env.example](pluto.chat/.env.example) with SMTP settings
- Registered tickets router in [main.py](pluto.chat/main.py)

## 🔧 How It Works

1. **Visitor raises ticket** → Widget sends POST to `/tickets/create`
2. **Backend validates** → Checks bot_token, finds user
3. **Creates ticket** → Generates ID, saves to database
4. **Sends email** → Notifies bot owner via Gmail
5. **Returns response** → Widget shows success message

## 📋 Setup Required

### 1. Run Database Migration
```bash
mysql -u root -p plutochat < pluto.chat/create_tickets_table.sql
```

### 2. Configure Gmail
1. Enable 2FA on Gmail
2. Generate App Password: https://myaccount.google.com/apppasswords
3. Add to `.env`:
```env
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_16_char_app_password
```

### 3. Restart Server
```bash
cd pluto.chat
uvicorn main:app --reload --port 8000
```

## 🎯 Features

✅ Ticket storage in database
✅ Email notifications to bot owner
✅ Unique ticket ID generation
✅ Visitor contact information capture
✅ Session tracking
✅ Status management (open/closed/pending)
✅ HTML-formatted emails
✅ Error handling

## 📧 Email Example

When a ticket is created, the bot owner receives:

```
Subject: New Support Ticket #TKT-20240115-0001

🎫 New Support Ticket Received

Ticket ID: TKT-20240115-0001
Visitor Name: John Doe
Visitor Email: john@example.com

Issue Description:
I'm having trouble accessing my account...

Please respond to the visitor at: john@example.com
```

## 🔍 Testing

1. Open test.html in browser
2. Chat with bot and mention "support ticket"
3. Click "🎫 Raise Support Ticket" button
4. Fill form and submit
5. Check database and email inbox

## 📊 Database Query

View all tickets:
```sql
SELECT ticket_id, visitor_name, visitor_email, issue, status, created_at 
FROM tickets 
ORDER BY created_at DESC;
```

## 🚀 Next Steps (Optional Enhancements)

- Add ticket dashboard in frontend
- Implement ticket status updates
- Add ticket reply functionality
- Send confirmation email to visitor
- Add ticket priority levels
- Implement ticket assignment
