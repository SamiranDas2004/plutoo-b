import os
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from app.db.session import get_db
from app.utils.auth_middleware import get_current_user
from app.services.pinecone_client import index

router = APIRouter()

embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    model="text-embedding-3-large",
    openai_api_base="https://openrouter.ai/api/v1",
)

class TextInfoRequest(BaseModel):
    title: str
    content: str

@router.post("/")
def create_text_info(
    request: TextInfoRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    from app.db.models import TextInformation
    from langchain_core.documents import Document as LangChainDoc
    
    if not request.content.strip():
        raise HTTPException(400, "Content cannot be empty")
    
    # Chunk content
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", ".", "!", "?", " ", ""],
    )
    chunks = splitter.split_documents([LangChainDoc(page_content=request.content)])
    
    # Generate embeddings
    vectors = []
    for i, chunk in enumerate(chunks):
        vector = embeddings.embed_query(chunk.page_content)
        vectors.append({
            "id": f"text_{user['id']}_{request.title}_{i}",
            "values": vector,
            "metadata": {
                "user_id": user["id"],
                "text": chunk.page_content[:500],
                "source": request.title,
                "type": "text_info"
            }
        })
    
    # Store in Pinecone
    index.upsert(vectors=vectors, namespace=str(user["id"]))
    
    # Store in database
    text_info = TextInformation(
        user_id=user["id"],
        title=request.title,
        content=request.content,
        chunks_count=len(vectors)
    )
    db.add(text_info)
    db.commit()
    db.refresh(text_info)
    
    return {
        "message": "Text information saved successfully!",
        "id": text_info.id,
        "title": request.title,
        "chunks_stored": len(vectors)
    }

@router.get("/")
def list_text_info(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    from app.db.models import TextInformation
    
    texts = db.query(TextInformation).filter(
        TextInformation.user_id == user["id"]
    ).order_by(TextInformation.created_at.desc()).all()
    
    return [
        {
            "id": t.id,
            "title": t.title,
            "content": t.content,
            "chunks_count": t.chunks_count,
            "created_at": t.created_at.isoformat()
        }
        for t in texts
    ]

@router.get("/{text_id}")
def get_text_info(
    text_id: int,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    from app.db.models import TextInformation
    
    text = db.query(TextInformation).filter(
        TextInformation.id == text_id,
        TextInformation.user_id == user["id"]
    ).first()
    
    if not text:
        raise HTTPException(404, "Text information not found")
    
    return {
        "id": text.id,
        "title": text.title,
        "content": text.content,
        "chunks_count": text.chunks_count,
        "created_at": text.created_at.isoformat()
    }

@router.delete("/{text_id}")
def delete_text_info(
    text_id: int,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    from app.db.models import TextInformation
    
    text = db.query(TextInformation).filter(
        TextInformation.id == text_id,
        TextInformation.user_id == user["id"]
    ).first()
    
    if not text:
        raise HTTPException(404, "Text information not found")
    
    # Delete from Pinecone
    try:
        index.delete(
            filter={"source": {"$eq": text.title}, "type": {"$eq": "text_info"}},
            namespace=str(user["id"])
        )
    except:
        pass
    
    # Delete from database
    db.delete(text)
    db.commit()
    
    return {"message": "Text information deleted successfully"}
