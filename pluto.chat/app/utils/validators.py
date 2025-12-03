"""
Input validation utilities
"""
import re
from typing import Optional
from fastapi import HTTPException

def validate_email(email: str) -> str:
    """Validate email format"""
    email = email.strip().lower()
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise HTTPException(status_code=400, detail="Invalid email format")
    if len(email) > 255:
        raise HTTPException(status_code=400, detail="Email too long")
    return email

def validate_password(password: str) -> str:
    """Validate password strength"""
    if len(password) < 8:
        raise HTTPException(
            status_code=400,
            detail="Password must be at least 8 characters long"
        )
    
    if len(password) > 128:
        raise HTTPException(status_code=400, detail="Password too long")
    
    if not re.search(r'[A-Z]', password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one uppercase letter"
        )
    
    if not re.search(r'[a-z]', password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one lowercase letter"
        )
    
    if not re.search(r'\d', password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one digit"
        )
    
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one special character"
        )
    
    return password

def validate_file_size(file_size: int, max_size: int = 10485760) -> None:
    """Validate file size (default 10MB)"""
    if file_size > max_size:
        raise HTTPException(
            status_code=400,
            detail=f"File size exceeds maximum allowed size of {max_size / 1048576}MB"
        )

def validate_file_type(filename: str, allowed_types: list = None) -> None:
    """Validate file extension"""
    if allowed_types is None:
        allowed_types = [".pdf", ".txt", ".docx"]
    
    ext = filename.lower().split(".")[-1]
    if f".{ext}" not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail=f"File type not allowed. Allowed types: {', '.join(allowed_types)}"
        )

def sanitize_filename(filename: str) -> str:
    """Sanitize filename to prevent path traversal"""
    # Remove any path components
    filename = filename.split("/")[-1].split("\\")[-1]
    # Remove dangerous characters
    filename = re.sub(r'[^\w\s.-]', '', filename)
    # Limit length
    if len(filename) > 255:
        name, ext = filename.rsplit(".", 1)
        filename = name[:250] + "." + ext
    return filename

def validate_session_id(session_id: str) -> str:
    """Validate session ID format"""
    if not re.match(r'^[a-zA-Z0-9_-]+$', session_id):
        raise HTTPException(status_code=400, detail="Invalid session ID format")
    if len(session_id) > 100:
        raise HTTPException(status_code=400, detail="Session ID too long")
    return session_id
