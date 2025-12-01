from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
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

app = FastAPI(
    title="My SaaS API",
    version="1.0.0"
)

# Enable CORS for widget
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing. In production, specify your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
