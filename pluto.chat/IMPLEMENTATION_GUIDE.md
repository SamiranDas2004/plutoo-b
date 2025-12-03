# Security Implementation Guide

## Step-by-Step Implementation

### 1. IMMEDIATE - Rotate All Secrets (CRITICAL)
```bash
# Generate new JWT secret
openssl rand -hex 32

# Update all API keys:
# - OpenRouter: https://openrouter.ai/keys
# - Pinecone: https://app.pinecone.io/
# - Cloudinary: https://cloudinary.com/console
# - Gmail App Password: https://myaccount.google.com/apppasswords
```

### 2. Install Security Dependencies
```bash
pip install slowapi python-dotenv passlib[bcrypt] PyJWT cryptography
```

### 3. Update Environment Variables
```bash
# Copy the secure template
cp .env.secure.example .env

# Edit .env with your new secrets
# NEVER commit .env to git
```

### 4. Update .gitignore
```bash
echo ".env" >> .gitignore
echo "temp/" >> .gitignore
echo "*.pyc" >> .gitignore
echo "__pycache__/" >> .gitignore
```

### 5. Replace Route Files
```bash
# Backup originals
cp app/routes/auth.py app/routes/auth.py.backup
cp app/routes/upload.py app/routes/upload.py.backup

# Use secure versions
cp app/routes/auth_secure.py app/routes/auth.py
cp app/routes/upload_secure.py app/routes/upload.py
```

### 6. Update main.py
The main.py has been updated with:
- Secure CORS configuration
- Rate limiting
- Error handling
- Production mode (hides docs)

### 7. Database Security
```sql
-- Create read-only user for analytics
CREATE USER 'analytics'@'localhost' IDENTIFIED BY 'strong_password';
GRANT SELECT ON plutochat.* TO 'analytics'@'localhost';

-- Ensure proper indexes for performance
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_session_id ON chat_sessions(session_id);
CREATE INDEX idx_bot_token ON users(bot_token);
```

### 8. Add Security Headers (Nginx/Apache)
```nginx
# Nginx configuration
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
add_header Content-Security-Policy "default-src 'self'" always;
```

### 9. Enable HTTPS
```bash
# Using Let's Encrypt with Certbot
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

### 10. Setup Logging
```python
# Add to main.py
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

### 11. Monitoring & Alerts
- Setup error tracking (Sentry)
- Monitor failed login attempts
- Alert on unusual API usage
- Track rate limit violations

### 12. Regular Security Tasks
- [ ] Rotate secrets every 90 days
- [ ] Update dependencies monthly
- [ ] Review access logs weekly
- [ ] Backup database daily
- [ ] Test disaster recovery quarterly

## Testing Security Fixes

### Test Rate Limiting
```bash
# Should block after 10 attempts
for i in {1..15}; do
  curl -X POST http://localhost:8000/auth/login \
    -H "Content-Type: application/json" \
    -d '{"email":"test@test.com","password":"wrong"}'
done
```

### Test Password Validation
```bash
# Should reject weak password
curl -X POST http://localhost:8000/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","password":"weak"}'
```

### Test File Upload Limits
```bash
# Should reject large files
dd if=/dev/zero of=large.pdf bs=1M count=20
curl -X POST http://localhost:8000/upload \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "file=@large.pdf"
```

### Test CORS
```bash
# Should reject unauthorized origin
curl -X POST http://localhost:8000/auth/login \
  -H "Origin: https://evil.com" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","password":"test"}'
```

## Security Checklist

- [ ] All secrets rotated
- [ ] .env not in git
- [ ] JWT_SECRET is strong (32+ chars)
- [ ] CORS configured with specific origins
- [ ] Rate limiting enabled
- [ ] Password validation active
- [ ] File upload limits enforced
- [ ] HTTPS enabled
- [ ] Security headers configured
- [ ] Error messages don't leak info
- [ ] Database uses strong password
- [ ] Logging configured
- [ ] Backups automated
- [ ] Dependencies updated

## Additional Recommendations

### 1. Add 2FA (Two-Factor Authentication)
```bash
pip install pyotp qrcode
```

### 2. Implement API Key Rotation
- Allow users to regenerate bot_token
- Invalidate old tokens after rotation

### 3. Add Request Signing
- Sign requests with HMAC
- Prevent replay attacks

### 4. Database Encryption
- Encrypt sensitive fields at rest
- Use TLS for database connections

### 5. Audit Logging
- Log all authentication attempts
- Track data access patterns
- Monitor for suspicious activity

### 6. Penetration Testing
- Run OWASP ZAP scans
- Test for SQL injection
- Check for XSS vulnerabilities

### 7. Compliance
- GDPR: Add data export/deletion
- CCPA: Implement privacy controls
- SOC 2: Document security procedures
