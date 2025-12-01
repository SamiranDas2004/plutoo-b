import smtplib
from email.mime.text import MIMEText

# Test with NEW password
smtp_email = "samiran4209@gmail.com"
smtp_password = "fkwuzmsomerpdlje"

print(f"Testing email credentials...")
print(f"Email: {smtp_email}")
print(f"Password length: {len(smtp_password) if smtp_password else 0}")
print(f"Password: {smtp_password}")

try:
    print("\nConnecting to Gmail SMTP...")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    print("TLS started...")
    
    print("Attempting login...")
    server.login(smtp_email, smtp_password)
    print("✅ LOGIN SUCCESSFUL!")
    
    # Send test email
    msg = MIMEText("Test email from PlutoChat")
    msg['Subject'] = "Test Email"
    msg['From'] = smtp_email
    msg['To'] = smtp_email
    
    server.send_message(msg)
    print("✅ TEST EMAIL SENT!")
    
    server.quit()
    
except Exception as e:
    print(f"❌ ERROR: {e}")
    print("\nPossible solutions:")
    print("1. Generate a NEW App Password at: https://myaccount.google.com/apppasswords")
    print("2. Make sure 2-Step Verification is ON")
    print("3. Delete old app passwords and create a fresh one")
    print("4. Copy the password WITHOUT spaces")
