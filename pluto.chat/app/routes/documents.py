from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.utils.auth_middleware import get_current_user
from app.services.pinecone_client import index
import os
from datetime import datetime

router = APIRouter()

@router.get("/")
def list_documents(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List all documents for the authenticated user"""
    from app.db.models import Document
    
    user_id = user["id"]
    
    # Get documents from database
    documents = db.query(Document).filter(
        Document.user_id == user_id
    ).order_by(Document.created_at.desc()).all()
    
    result = []
    for doc in documents:
        result.append({
            "id": str(doc.id),
            "name": doc.filename,
            "size": doc.file_size,
            "type": doc.file_type,
            "uploadedAt": doc.created_at.isoformat()
        })
    
    return result

@router.get("/{document_id}/content")
def get_document_content(
    document_id: str,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get document content"""
    from app.db.models import Document
    
    user_id = user["id"]
    
    doc = db.query(Document).filter(
        Document.id == int(document_id),
        Document.user_id == user_id
    ).first()
    
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    
    return {
        "id": str(doc.id),
        "name": doc.filename,
        "content": doc.content or ""
    }

@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Upload a document (reuse existing upload logic)"""
    # Import the existing upload logic
    from app.routes.upload import extract_text_from_file
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_openai import OpenAIEmbeddings
    
    user_id = user["id"]
    
    # Save file temporarily
    os.makedirs("temp", exist_ok=True)
    upload_path = f"temp/{file.filename}"
    
    with open(upload_path, "wb") as f:
        f.write(await file.read())
    
    try:
        # Extract text
        documents = extract_text_from_file(file, upload_path)
        
        # Split into chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            separators=["\n\n", "\n", ".", "!", "?", " ", ""],
        )
        chunks = splitter.split_documents(documents)
        
        # Generate embeddings
        from app.db.models import Document
        
        embeddings = OpenAIEmbeddings(
            openai_api_key=os.getenv("OPENROUTER_API_KEY"),
            model="text-embedding-3-large",
            openai_api_base="https://openrouter.ai/api/v1",
        )
        
        vectors = []
        for i, chunk in enumerate(chunks):
            vector = embeddings.embed_query(chunk.page_content)
            vectors.append({
                "id": f"doc_{user_id}_{file.filename}_{i}",
                "values": vector,
                "metadata": {
                    "user_id": user_id,
                    "text": chunk.page_content[:500],
                    "source": file.filename,
                    "uploaded_at": datetime.now().isoformat()
                }
            })
        
        # Store in Pinecone
        index.upsert(vectors=vectors, namespace=str(user_id))
        
        # Store in database
        doc = Document(
            user_id=user_id,
            filename=file.filename,
            file_size=file.size,
            file_type=file.content_type or "application/octet-stream",
            chunks_count=len(vectors)
        )
        db.add(doc)
        db.commit()
        db.refresh(doc)
        
        # Clean up temp file
        os.remove(upload_path)
        
        # Return document info
        return {
            "id": str(doc.id),
            "name": file.filename,
            "size": file.size,
            "type": file.content_type,
            "uploadedAt": doc.created_at.isoformat(),
            "chunks_stored": len(vectors)
        }
        
    except Exception as e:
        # Clean up temp file on error
        if os.path.exists(upload_path):
            os.remove(upload_path)
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

@router.delete("/{document_id}")
def delete_document(
    document_id: str,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete a document and its vectors from Pinecone"""
    from app.db.models import Document
    
    user_id = user["id"]
    namespace = str(user_id)
    
    # Get document from database
    doc = db.query(Document).filter(
        Document.id == int(document_id),
        Document.user_id == user_id
    ).first()
    
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    
    try:
        # Delete vectors from Pinecone
        index.delete(
            filter={"source": {"$eq": doc.filename}},
            namespace=namespace
        )
        
        # Delete from database
        db.delete(doc)
        db.commit()
        
        return {"message": "Document deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Delete failed: {str(e)}")