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

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            res = await client.post(url, headers=headers, json=payload)
            data = res.json()
        ans = data["choices"][0]["message"]["content"].strip().upper()
        return ans == "YES"
    except:
        return False


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
            "CRITICAL RULES - Follow these strictly:\n\n"
            "1. FIRST, carefully check if the provided context contains relevant information to answer the question\n\n"
            "2. IF the context IS relevant and sufficient:\n"
            "   - Answer the question clearly using the context\n"
            "   - You may combine context with conversation history\n"
            "   - Cite specific details from the context when helpful\n\n"
            "3. IF the context is NOT relevant OR lacks necessary details:\n"
            "   - Do NOT attempt to answer from general knowledge\n"
            "   - Do NOT make assumptions or guesses\n"
            "   - Respond EXACTLY with: 'I don't have enough information in our knowledge base to answer this accurately. Would you like me to raise a support ticket so our team can help you?'\n\n"
            "4. IF the context is partially relevant but incomplete:\n"
            "   - Share what you DO know from the context\n"
            "   - Then say: 'For complete details on this, I'd recommend raising a support ticket. Would you like me to do that?'\n\n"
            "5. NEVER fabricate information, dates, policies, features, or details not present in the context"
        )
    else:
        system_prompt = (
            "You are a friendly and helpful AI assistant for a SaaS chatbot platform.\n"
            "The user's message is general conversation that doesn't require searching the knowledge base.\n\n"
            "IMPORTANT RULES:\n\n"
            "1. For greetings (hi, hello, how are you): Respond warmly and ask how you can help\n\n"
            "2. For general questions (what's the weather, tell me a joke): Use your general knowledge appropriately\n\n"
            "3. For casual conversation: Be friendly, natural, and engaging\n\n"
            "4. IF the user asks about specific company information (products, pricing, policies, account details, technical issues):\n"
            "   - Say: 'That's a great question about [topic]. Let me search our knowledge base for the most accurate information.'\n"
            "   - Note: The system will then trigger a knowledge base search\n\n"
            "5. Keep responses concise (2-3 sentences for simple queries)\n\n"
            "6. Always be helpful and guide users toward the right solution"
        )

    # Improved message structure
    if used_rag:
        user_message = (
            f"CONTEXT FROM KNOWLEDGE BASE:\n"
            f"---\n"
            f"{context if context.strip() else 'No relevant context found'}\n"
            f"---\n\n"
            f"USER QUESTION: {query}\n\n"
            f"Remember: Only answer if the context above contains the information. "
            f"If not, suggest raising a support ticket."
        )
    else:
        user_message = query

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.3,  # Lower temperature for more consistent responses
        "max_tokens": 500,   # Reasonable limit for chatbot responses
    }

    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            res = await client.post(url, headers=headers, json=payload)
            res.raise_for_status()  # Raise exception for bad status codes
            data = res.json()
        
        response = data["choices"][0]["message"]["content"]
        
        # Validation: Check if model is hallucinating when it should suggest ticket
        if used_rag and context.strip() == "":
            # No context provided but RAG was used - force ticket suggestion
            return "I don't have enough information in our knowledge base to answer this accurately. Would you like me to raise a support ticket so our team can help you?"
        
        return response
        
    except httpx.TimeoutException:
        return "I'm taking longer than expected to respond. Please try again in a moment."
    except httpx.HTTPStatusError as e:
        return f"I'm experiencing technical difficulties (Error {e.response.status_code}). Please try again shortly."
    except Exception:
        return "I'm having trouble connecting right now. Please try again in a moment."
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

    try:
        async with httpx.AsyncClient(timeout=20.0) as client:
            res = await client.post(url, headers=headers, json=payload)
            data = res.json()
        return data["choices"][0]["message"]["content"]
    except:
        return ""  # Return empty string on timeout instead of crashing


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

    # 4️⃣ Auto-summarize if total messages > 20 (with timeout handling)
    total_msgs = db.query(ChatMessage).filter(ChatMessage.session_id == req.session_id).count()

    if total_msgs > 20:
        full_history = (
            db.query(ChatMessage)
            .filter(ChatMessage.session_id == req.session_id)
            .order_by(ChatMessage.created_at.asc())
            .all()
        )
        summary = await summarize_conversation(full_history)
        if summary:  # Only update if summarization succeeded
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