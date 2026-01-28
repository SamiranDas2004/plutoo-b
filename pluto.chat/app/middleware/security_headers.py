"""
Security Headers Middleware
Adds security headers to all responses
"""
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import os


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Add security headers to all responses"""
    
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        
        # Debug: Print environment and path info
        env = os.getenv("ENVIRONMENT", "not_set")
        # print(f"DEBUG: ENVIRONMENT={env}, PATH={request.url.path}")  # Remove debug logging
        
        # Prevent clickjacking - Allow widget to be embedded anywhere
        if request.url.path.startswith("/widget") or request.url.path.startswith("/chat"):
            # Allow embedding for widget/chat endpoints (needed for customer websites)
            pass  # Don't set X-Frame-Options, allow all origins
        else:
            # Block all other endpoints from being embedded
            response.headers["X-Frame-Options"] = "DENY"
        
        # Prevent MIME type sniffing
        response.headers["X-Content-Type-Options"] = "nosniff"
        
        # XSS Protection
        response.headers["X-XSS-Protection"] = "1; mode=block"
        
        # Referrer Policy
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        
        # Content Security Policy - Allow localhost in development
        if request.url.path.startswith("/widget"):
            # Relaxed CSP for widget iframe
            response.headers["Content-Security-Policy"] = (
                "default-src 'self'; "
                "script-src 'self' 'unsafe-inline' 'unsafe-eval'; "
                "style-src 'self' 'unsafe-inline'; "
                "connect-src 'self' http://localhost:* http://127.0.0.1:* https://openrouter.ai https://*.pinecone.io"
            )
        elif env == "production":
            response.headers["Content-Security-Policy"] = (
                "default-src 'self'; "
                "script-src 'self' 'unsafe-inline' 'unsafe-eval'; "
                "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
                "img-src 'self' data: https:; "
                "font-src 'self' data: https://fonts.gstatic.com; "
                "connect-src 'self' https://openrouter.ai https://*.pinecone.io"
            )
        else:
            # Development CSP - allow localhost connections
            response.headers["Content-Security-Policy"] = (
                "default-src 'self'; "
                "script-src 'self' 'unsafe-inline' 'unsafe-eval'; "
                "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
                "img-src 'self' data: https:; "
                "font-src 'self' data: https://fonts.gstatic.com; "
                "connect-src 'self' http://localhost:* http://127.0.0.1:* https://openrouter.ai https://*.pinecone.io"
            )
        
        # HSTS (only in production with HTTPS)
        if os.getenv("ENVIRONMENT") == "production":
            response.headers["Strict-Transport-Security"] = (
                "max-age=31536000; includeSubDomains; preload"
            )
        
        # Permissions Policy (formerly Feature-Policy)
        response.headers["Permissions-Policy"] = (
            "geolocation=(), microphone=(), camera=(), payment=()"
        )
        
        return response
