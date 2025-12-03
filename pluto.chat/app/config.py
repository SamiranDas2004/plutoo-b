"""
Security Configuration
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Security Settings
class SecurityConfig:
    # JWT
    JWT_SECRET = os.getenv("JWT_SECRET")
    if not JWT_SECRET:
        raise ValueError("JWT_SECRET must be set in environment variables")
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRATION_MINUTES = 1440  # 24 hours
    
    # CORS
    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "").split(",")
    if not ALLOWED_ORIGINS or ALLOWED_ORIGINS == [""]:
        raise ValueError("ALLOWED_ORIGINS must be set in environment variables")
    
    # Rate Limiting
    RATE_LIMIT_PER_MINUTE = int(os.getenv("RATE_LIMIT_PER_MINUTE", "60"))
    
    # File Upload
    MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", "10485760"))  # 10MB default
    ALLOWED_FILE_TYPES = [".pdf", ".txt", ".docx"]
    
    # Password Policy
    MIN_PASSWORD_LENGTH = 8
    REQUIRE_UPPERCASE = True
    REQUIRE_LOWERCASE = True
    REQUIRE_DIGIT = True
    REQUIRE_SPECIAL = True
    
    # Database
    DATABASE_URL = os.getenv("DATABASE_URL")
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL must be set")
    
    # API Keys (validate they exist)
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    
    if not OPENROUTER_API_KEY or not PINECONE_API_KEY:
        raise ValueError("API keys must be set in environment variables")
