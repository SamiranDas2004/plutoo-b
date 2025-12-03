from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from app.middleware.security_headers import SecurityHeadersMiddleware
from app.middleware.request_size_limiter import RequestSizeLimiterMiddleware
from app.middleware.cors_middleware import CustomCORSMiddleware
import os
from app.routes.chat import router as chat_router
from app.routes.upload import router as upload_router
from app.routes.auth import router as auth_router
from app.routes.analytics import router as analytics_router
from app.routes.sessions import router as sessions_router
from app.routes.documents import router as documents_router
from app.routes.visitors import router as visitors_router
from app.routes.widget import router as widget_router
from app.routes.text_info import router as text_info_router
from app.routes.audio import router as audio_router
from app.routes.website import router as website_router
from app.routes.tickets import router as tickets_router

# Rate limiter
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="My SaaS API",
    version="1.0.0",
    docs_url=None if os.getenv("ENVIRONMENT") == "production" else "/docs",
    redoc_url=None if os.getenv("ENVIRONMENT") == "production" else "/redoc"
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Add security middlewares
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(RequestSizeLimiterMiddleware, max_size=10 * 1024 * 1024)  # 10MB
app.add_middleware(CustomCORSMiddleware)  # Custom CORS for widget endpoints

# Global exception handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Invalid request data"},
    )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # Log the error (add proper logging)
    if os.getenv("ENVIRONMENT") == "production":
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "Internal server error"},
        )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": str(exc)},
    )

# Register routes
app.include_router(auth_router, prefix="/auth")
app.include_router(chat_router, prefix="/chat")
app.include_router(upload_router, prefix="/upload")
app.include_router(analytics_router, prefix="/analytics")
app.include_router(sessions_router, prefix="/sessions")
app.include_router(documents_router, prefix="/documents")
app.include_router(visitors_router, prefix="/visitors")
app.include_router(widget_router, prefix="/widget")
app.include_router(text_info_router, prefix="/text-info")
app.include_router(audio_router, prefix="/audio")
app.include_router(website_router, prefix="/website")
app.include_router(tickets_router, prefix="/tickets")

# Mount static files for widget
app.mount("/widget", StaticFiles(directory="../widget", html=True), name="widget")

@app.get("/")
def root():
    return {"message": "API is running!"}
