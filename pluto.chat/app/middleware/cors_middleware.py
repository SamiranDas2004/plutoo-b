"""
Custom CORS Middleware
Allows all origins for widget/chat endpoints, restricted for others
"""
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import os


class CustomCORSMiddleware(BaseHTTPMiddleware):
    """Custom CORS handling for widget endpoints"""
    
    async def dispatch(self, request: Request, call_next):
        origin = request.headers.get("origin")
        
        # Handle preflight requests
        if request.method == "OPTIONS":
            response = Response()
        else:
            response = await call_next(request)
        
        # Allow all origins for widget/chat endpoints (customer websites)
        if request.url.path.startswith("/widget") or request.url.path.startswith("/chat"):
            response.headers["Access-Control-Allow-Origin"] = origin or "*"
            response.headers["Access-Control-Allow-Credentials"] = "true"
        else:
            # Restricted origins for admin/auth endpoints
            allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
            if origin in allowed_origins:
                response.headers["Access-Control-Allow-Origin"] = origin
                response.headers["Access-Control-Allow-Credentials"] = "true"
        
        # Common CORS headers
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Access-Control-Max-Age"] = "3600"
        
        return response
