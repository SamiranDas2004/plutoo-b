# Brevo (Sendinblue) Email Setup - EASIER ALTERNATIVE

If Gmail App Passwords are not working, use Brevo instead. It's FREE and much simpler!

## Why Brevo?
- ✅ FREE (300 emails/day)
- ✅ No 2FA required
- ✅ No App Passwords needed
- ✅ Simple API key
- ✅ More reliable for automated emails

## Setup Steps (5 minutes)

### 1. Create Brevo Account
1. Go to: https://www.brevo.com/
2. Click "Sign up free"
3. Enter your email and create password
4. Verify your email

### 2. Get SMTP Credentials
1. Login to Brevo
2. Go to: https://app.brevo.com/settings/keys/smtp
3. You'll see:
   - **SMTP Server:** smtp-relay.brevo.com
   - **Port:** 587
   - **Login:** (your email)
   - **SMTP Key:** (click "Generate new SMTP key")

### 3. Update .env File

Replace your Gmail settings with:

```env
SMTP_HOST=smtp-relay.brevo.com
SMTP_PORT=587
SMTP_EMAIL=samiran4209@gmail.com
SMTP_PASSWORD=your_brevo_smtp_key_here
```

### 4. Restart Server

```bash
cd pluto.chat
uvicorn main:app --reload --port 8000
```

### 5. Test

Send a ticket via Postman - email should work immediately!

## Example .env

```env
# Brevo SMTP (FREE - 300 emails/day)
SMTP_HOST=smtp-relay.brevo.com
SMTP_PORT=587
SMTP_EMAIL=samiran4209@gmail.com
SMTP_PASSWORD=xkeysib-abc123def456...
```

That's it! Much easier than Gmail App Passwords.
