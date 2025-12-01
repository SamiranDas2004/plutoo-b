import os
import httpx
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
import cloudinary
import cloudinary.uploader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from app.db.session import get_db
from app.utils.auth_middleware import get_current_user
from app.services.pinecone_client import index

router = APIRouter()

# Groq API for free Whisper transcription
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_API_URL = "https://api.groq.com/openai/v1/audio/transcriptions"

# Initialize Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    model="text-embedding-3-large",
    openai_api_base="https://openrouter.ai/api/v1",
)

MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB

@router.post("/")
async def upload_audio(
    file: UploadFile = File(...),
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    from app.db.models import AudioRecording
    
    # Validate file type
    allowed_types = ["audio/mpeg", "audio/mp3", "audio/wav", "audio/m4a", "audio/webm"]
    if file.content_type not in allowed_types:
        raise HTTPException(400, f"Unsupported audio format: {file.content_type}")
    
    # Read file
    content = await file.read()
    file_size = len(content)
    
    # Check file size
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(400, f"File too large. Max size: 50MB")
    
    # Save temporarily for Whisper
    os.makedirs("temp", exist_ok=True)
    temp_path = f"temp/{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(content)
    
    try:
        # Transcribe with Groq Whisper (FREE)
        async with httpx.AsyncClient() as client:
            with open(temp_path, "rb") as audio_file:
                files = {"file": (file.filename, audio_file, file.content_type)}
                data = {"model": "whisper-large-v3"}
                headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
                
                response = await client.post(
                    GROQ_API_URL,
                    files=files,
                    data=data,
                    headers=headers,
                    timeout=60.0
                )
                
                if response.status_code != 200:
                    raise HTTPException(500, f"Transcription failed: {response.text}")
                
                result = response.json()
                transcribed_text = result.get("text", "")
        
        # Upload to Cloudinary
        upload_result = cloudinary.uploader.upload(
            temp_path,
            resource_type="video",  # Cloudinary uses 'video' for audio
            folder="pluto_audio"
        )
        audio_url = upload_result["secure_url"]
        
        # Chunk transcribed text
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            separators=["\n\n", "\n", ".", "!", "?", " ", ""],
        )
        from langchain_core.documents import Document as LangChainDoc
        chunks = splitter.split_documents([LangChainDoc(page_content=transcribed_text)])
        
        # Generate embeddings
        vectors = []
        for i, chunk in enumerate(chunks):
            vector = embeddings.embed_query(chunk.page_content)
            vectors.append({
                "id": f"audio_{user['id']}_{upload_result['public_id']}_{i}",
                "values": vector,
                "metadata": {
                    "user_id": user["id"],
                    "text": chunk.page_content[:500],
                    "source": file.filename,
                    "type": "audio"
                }
            })
        
        # Store in Pinecone
        index.upsert(vectors=vectors, namespace=str(user["id"]))
        
        # Store in database
        audio_record = AudioRecording(
            user_id=user["id"],
            filename=file.filename,
            file_size=file_size,
            file_type=file.content_type,
            audio_url=audio_url,
            transcribed_text=transcribed_text,
            chunks_count=len(vectors),
            duration=upload_result.get("duration", 0)
        )
        db.add(audio_record)
        db.commit()
        db.refresh(audio_record)
        
        return {
            "message": "Audio processed successfully!",
            "audio_id": audio_record.id,
            "transcribed_text": transcribed_text,
            "chunks_stored": len(vectors),
            "audio_url": audio_url
        }
        
    finally:
        # Cleanup temp file
        if os.path.exists(temp_path):
            os.remove(temp_path)


@router.get("/")
async def list_audio(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    from app.db.models import AudioRecording
    
    recordings = db.query(AudioRecording).filter(
        AudioRecording.user_id == user["id"]
    ).order_by(AudioRecording.created_at.desc()).all()
    
    return [
        {
            "id": r.id,
            "filename": r.filename,
            "file_size": r.file_size,
            "audio_url": r.audio_url,
            "transcribed_text": r.transcribed_text,
            "duration": r.duration,
            "chunks_count": r.chunks_count,
            "created_at": r.created_at.isoformat()
        }
        for r in recordings
    ]


@router.delete("/{audio_id}")
async def delete_audio(
    audio_id: int,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    from app.db.models import AudioRecording
    
    audio = db.query(AudioRecording).filter(
        AudioRecording.id == audio_id,
        AudioRecording.user_id == user["id"]
    ).first()
    
    if not audio:
        raise HTTPException(404, "Audio not found")
    
    db.delete(audio)
    db.commit()
    
    return {"message": "Audio deleted successfully"}
