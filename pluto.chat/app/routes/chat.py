import os
import httpx
from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from pydantic import BaseModel, validator
from app.db.session import get_db
from app.db.models import User
from app.services.pinecone_client import index
from slowapi import Limiter
from slowapi.util import get_remote_address

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE = "https://openrouter.ai/api/v1"


# ==========================================================
# REQUEST BODY MODEL
# ==========================================================
class ChatRequest(BaseModel):
    bot_token: str
    session_id: str
    message: str
    visitor_contact: str | None = None
    
    @validator('bot_token')
    def validate_bot_token(cls, v):
        if not v or len(v) < 10 or len(v) > 100:
            raise ValueError("Invalid bot token format")
        # Only allow alphanumeric, dash, underscore
        import re
        if not re.match(r'^[a-zA-Z0-9_-]+$', v):
            raise ValueError("Bot token contains invalid characters")
        return v
    
    @validator('session_id')
    def validate_session_id(cls, v):
        if not v or len(v) > 100:
            raise ValueError("Invalid session ID")
        import re
        if not re.match(r'^[a-zA-Z0-9_-]+$', v):
            raise ValueError("Session ID contains invalid characters")
        return v
    
    @validator('message')
    def validate_message(cls, v):
        if not v or not v.strip():
            raise ValueError("Message cannot be empty")
        if len(v) > 5000:
            raise ValueError("Message too long (max 5000 characters)")
        return v.strip()


# ==========================================================
# INTENT CLASSIFIER — Decide RAG vs No RAG
# ==========================================================
async def should_use_pinecone(query: str) -> bool:
    url = f"{OPENROUTER_BASE}/chat/completions"
    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}"}

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an intent classifier. "
                    "Determine if this user message needs database or knowledge base search. "
                    "Answer YES only if the question asks about:\n"
                    "- Specific products, services, or features\n"
                    "- Pricing, plans, or documentation\n"
                    "- Company policies or procedures\n"
                    "- Technical details or specifications\n"
                    "- Past orders, accounts, or stored data\n\n"
                    "Answer NO if the message is:\n"
                    "- A greeting (hi, hello, hey)\n"
                    "- General conversation or chit-chat\n"
                    "- A question the AI can answer from general knowledge\n"
                    "- Math, coding, or common sense questions\n\n"
                    "Respond with only YES or NO."
                )
            },
            {"role": "user", "content": query}
        ]
    }

    async with httpx.AsyncClient() as client:
        res = await client.post(url, headers=headers, json=payload)
        data = res.json()

    ans = data["choices"][0]["message"]["content"].strip().upper()
    return ans == "YES"


# ==========================================================
# EMBEDDINGS
# ==========================================================
async def create_embedding(text: str):
    url = f"{OPENROUTER_BASE}/embeddings"
    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}"}

    payload = {"model": "text-embedding-3-large", "input": text}

    async with httpx.AsyncClient() as client:
        res = await client.post(url, headers=headers, json=payload)
        data = res.json()

    return data["data"][0]["embedding"]


# ==========================================================
# MAIN LLM CHAT COMPLETION (IMPROVED LOGIC)
# ==========================================================
async def create_chat_response(context: str, query: str, used_rag: bool):
    url = f"{OPENROUTER_BASE}/chat/completions"
    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}"}

    # Different system prompts based on whether RAG was used
    if used_rag:
        system_prompt = (
            "You are a helpful AI assistant for a SaaS chatbot platform.\n"
            "The user has asked a question that requires specific information from the knowledge base.\n\n"
            "IMPORTANT RULES:\n"
            "1. If the provided context contains relevant information, answer using that information\n"
            "2. If the context does NOT contain enough details to answer the question accurately, "
            "respond with: 'I don't have enough information to answer this. Would you like me to raise a support ticket?'\n"
            "3. Do NOT make up or guess information that isn't in the context\n"
            "4. You can combine the context information with conversation history to give helpful answers"
        )
    else:
        system_prompt = (
            "You are a friendly and helpful AI assistant for a SaaS chatbot platform.\n"
            "The user's message doesn't require searching the knowledge base - it's a general conversation.\n\n"
            "IMPORTANT RULES:\n"
            "1. For greetings, respond naturally and warmly\n"
            "2. For general questions, use your knowledge to provide helpful answers\n"
            "3. For casual conversation, be friendly and engaging\n"
            "4. If the user asks something specific about the company's products, policies, or services, "
            "let them know you'd be happy to look that up for them\n"
            "5. Keep responses concise and natural"
        )

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nUser Query: {query}"
            }
        ]
    }

    async with httpx.AsyncClient() as client:
        res = await client.post(url, headers=headers, json=payload)
        data = res.json()

    return data["choices"][0]["message"]["content"]


# ==========================================================
# AUTO SUMMARY GENERATION
# ==========================================================
async def summarize_conversation(full_messages):
    url = f"{OPENROUTER_BASE}/chat/completions"
    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}"}

    text = "\n".join([f"{m.sender}: {m.message}" for m in full_messages])

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "Summarize the conversation objectively. Keep only important details."
            },
            {"role": "user", "content": text}
        ]
    }

    async with httpx.AsyncClient() as client:
        res = await client.post(url, headers=headers, json=payload)
        data = res.json()

    return data["choices"][0]["message"]["content"]


# ==========================================================
# MAIN CHAT ENDPOINT
# ==========================================================
@router.post("/")
@limiter.limit("30/minute")
async def chat(request: Request, req: ChatRequest, db: Session = Depends(get_db)):
    from app.db.models import ChatMessage, ChatSession
    from app.utils.audit_logger import AuditLogger, get_client_ip
    
    client_ip = get_client_ip(request)

    # 1️⃣ Validate bot token → find user
    user = db.query(User).filter(User.bot_token == req.bot_token).first()
    if not user:
        AuditLogger.log_security_event(
            "INVALID_BOT_TOKEN",
            f"Invalid bot token attempt: {req.bot_token[:10]}...",
            client_ip
        )
        raise HTTPException(status_code=404, detail="Invalid bot token")
    
    # Log API access
    AuditLogger.log_api_access(
        user_id=user.id,
        endpoint="/chat",
        method="POST",
        ip_address=client_ip,
        status_code=200
    )

    namespace = user.pinecone_namespace

    # 2️⃣ Ensure chat session exists
    session = db.query(ChatSession).filter(ChatSession.session_id == req.session_id).first()
    if not session:
        session = ChatSession(session_id=req.session_id, user_id=user.id)
        db.add(session)
        db.commit()
        db.refresh(session)

    # 3️⃣ Save visitor message
    visitor_msg = ChatMessage(
        session_id=req.session_id,
        sender="visitor",
        role="user",
        message=req.message
    )
    db.add(visitor_msg)
    db.commit()

    # 4️⃣ Auto-summarize if total messages > 20
    total_msgs = db.query(ChatMessage).filter(ChatMessage.session_id == req.session_id).count()

    if total_msgs > 20:
        full_history = (
            db.query(ChatMessage)
            .filter(ChatMessage.session_id == req.session_id)
            .order_by(ChatMessage.created_at.asc())
            .all()
        )
        summary = await summarize_conversation(full_history)
        session.summary = summary
        db.commit()

    # 5️⃣ Get last 10 messages for short-term memory
    history = (
        db.query(ChatMessage)
        .filter(ChatMessage.session_id == req.session_id)
        .order_by(ChatMessage.created_at.desc())
        .limit(10)
        .all()
    )

    memory_context = "\n".join([f"{m.sender}: {m.message}" for m in reversed(history)])
    summary_context = session.summary if session.summary else ""

    # 6️⃣ Check if we need RAG or not
    use_rag = await should_use_pinecone(req.message)

    pinecone_context = ""
    if use_rag:
        embedding = await create_embedding(req.message)

        results = index.query(
            vector=embedding,
            namespace=namespace,
            top_k=5,
            include_metadata=True
        )

        pinecone_context = "\n".join(
            [m["metadata"].get("text", "") for m in results["matches"]]
        )

    # 7️⃣ Build final context for LLM
    if use_rag:
        full_context = (
            f"Summary:\n{summary_context}\n\n"
            f"Recent Messages:\n{memory_context}\n\n"
            f"Relevant Knowledge:\n{pinecone_context}"
        )
    else:
        full_context = (
            f"Summary:\n{summary_context}\n\n"
            f"Recent Messages:\n{memory_context}"
        )

    # 8️⃣ LLM reply (pass the use_rag flag)
    reply = await create_chat_response(full_context, req.message, use_rag)

    # 9️⃣ Save bot message
    bot_msg = ChatMessage(
        session_id=req.session_id,
        sender="bot",
        role="assistant",
        message=reply
    )
    db.add(bot_msg)
    db.commit()

    # 🔟 Return response to widget
    return {
        "session_id": req.session_id,
        "used_rag": use_rag,
        "reply": reply
    }