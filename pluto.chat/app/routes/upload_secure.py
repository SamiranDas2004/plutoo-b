import os
from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from app.db.session import get_db
from app.utils.auth_middleware import get_current_user
from app.services.pinecone_client import index
from app.utils.validators import validate_file_size, validate_file_type, sanitize_filename

router = APIRouter()

embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    model="text-embedding-3-large",
    openai_api_base="https://openrouter.ai/api/v1",
)

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_EXTENSIONS = [".pdf", ".txt", ".docx"]


def extract_text_from_file(file: UploadFile, saved_path: str):
    ext = file.filename.split(".")[-1].lower()

    if ext == "pdf":
        loader = PyMuPDFLoader(saved_path)
    elif ext == "txt":
        loader = TextLoader(saved_path)
    elif ext == "docx":
        loader = Docx2txtLoader(saved_path)
    else:
        raise HTTPException(status_code=400, detail=f"Unsupported file type: {ext}")

    return loader.load()


@router.post("/")
async def upload_file(
    file: UploadFile = File(None),
    text: str = Form(None),
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Supports:
    - File upload (PDF/TXT/DOCX)
    - Raw text upload via form body
    """
    from app.db.models import Document

    if not file and not text:
        raise HTTPException(400, "Send either a file or text")

    # Extract documents
    if file:
        # Validate file
        content = await file.read()
        file_size = len(content)
        
        validate_file_size(file_size, MAX_FILE_SIZE)
        validate_file_type(file.filename, ALLOWED_EXTENSIONS)
        
        # Sanitize filename
        safe_filename = sanitize_filename(file.filename)
        
        # Save file
        os.makedirs("temp", exist_ok=True)
        upload_path = f"temp/{safe_filename}"

        with open(upload_path, "wb") as f:
            f.write(content)

        try:
            documents = extract_text_from_file(file, upload_path)
            filename = safe_filename
            file_type = file.content_type or "application/octet-stream"
        finally:
            # Clean up temp file
            if os.path.exists(upload_path):
                os.remove(upload_path)

    else:
        # Validate text size
        if len(text) > MAX_FILE_SIZE:
            raise HTTPException(400, "Text content too large")
        
        # Raw text → convert to LangChain Document
        from langchain_core.documents import Document as LangChainDoc
        documents = [LangChainDoc(page_content=text)]
        file_size = len(text.encode('utf-8'))
        filename = "raw_text.txt"
        file_type = "text/plain"

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", ".", "!", "?", " ", ""],
    )

    chunks = splitter.split_documents(documents)

    # Extract full content
    full_content = "\n\n".join([doc.page_content for doc in documents])

    # Generate embeddings
    vectors = []
    for i, chunk in enumerate(chunks):
        vector = embeddings.embed_query(chunk.page_content)
        vectors.append({
            "id": f"doc_{user['id']}_{i}",
            "values": vector,
            "metadata": {
                "user_id": user["id"],
                "text": chunk.page_content[:500],
                "source": filename
            }
        })

    # Store in Pinecone
    index.upsert(
        vectors=vectors,
        namespace=str(user["id"])
    )

    # Store document metadata in database
    doc = Document(
        user_id=user["id"],
        filename=filename,
        file_size=file_size,
        file_type=file_type,
        content=full_content,
        chunks_count=len(vectors)
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)

    return {
        "message": "Data stored successfully!",
        "chunks_stored": len(vectors),
        "mode": "file" if file else "raw_text",
        "namespace": user["id"],
        "document_id": doc.id
    }
