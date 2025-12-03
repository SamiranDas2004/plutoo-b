"""
Request Size Limiter Middleware
Limits request body size to prevent DoS attacks
"""
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
import os


class RequestSizeLimiterMiddleware(BaseHTTPMiddleware):
    """Limit request body size"""
    
    def __init__(self, app, max_size: int = 10 * 1024 * 1024):  # 10MB default
        super().__init__(app)
        self.max_size = max_size
    
    async def dispatch(self, request: Request, call_next):
        # Check Content-Length header
        content_length = request.headers.get("content-length")
        
        if content_length:
            content_length = int(content_length)
            if content_length > self.max_size:
                return JSONResponse(
                    status_code=413,
                    content={
                        "detail": f"Request body too large. Maximum size: {self.max_size / 1024 / 1024}MB"
                    }
                )
        
        response = await call_next(request)
        return response
