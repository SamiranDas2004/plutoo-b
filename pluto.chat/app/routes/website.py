import os
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, HttpUrl
from sqlalchemy.orm import Session
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from app.db.session import get_db
from app.utils.auth_middleware import get_current_user
from app.services.pinecone_client import index

router = APIRouter()

embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    model="text-embedding-3-large",
    openai_api_base="https://openrouter.ai/api/v1",
)

llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    model="openai/gpt-4o-mini",
    temperature=0.3
)

class WebsiteRequest(BaseModel):
    url: HttpUrl

@router.post("/")
async def load_website(
    request: WebsiteRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    from app.db.models import WebsiteData
    
    url = str(request.url)
    
    try:
        # Load website content
        loader = WebBaseLoader(url)
        documents = loader.load()
        
        if not documents:
            raise HTTPException(400, "Failed to load website content")
        
        full_content = "\n\n".join([doc.page_content for doc in documents])
        
        # Generate summary
        summary_prompt = f"Summarize the following website content in 2-3 paragraphs:\n\n{full_content[:4000]}"
        summary = llm.invoke(summary_prompt).content
        
        # Chunk content
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            separators=["\n\n", "\n", ".", "!", "?", " ", ""],
        )
        chunks = splitter.split_documents(documents)
        
        # Generate embeddings
        vectors = []
        for i, chunk in enumerate(chunks):
            vector = embeddings.embed_query(chunk.page_content)
            vectors.append({
                "id": f"web_{user['id']}_{hash(url)}_{i}",
                "values": vector,
                "metadata": {
                    "user_id": user["id"],
                    "text": chunk.page_content[:500],
                    "source": url,
                    "type": "website"
                }
            })
        
        # Store in Pinecone
        index.upsert(vectors=vectors, namespace=str(user["id"]))
        print("embaddings stored in pinecone")
        # Store in database
        website_data = WebsiteData(
            user_id=user["id"],
            url=url,
            content=full_content[:10000],  # Store first 10k chars
            summary=summary,
            chunks_count=len(vectors)
        )
        db.add(website_data)
        db.commit()
        db.refresh(website_data)
        
        return {
            "message": "Website data loaded successfully!",
            "website_id": website_data.id,
            "url": url,
            "summary": summary,
            "chunks_stored": len(vectors)
        }
        
    except Exception as e:
        raise HTTPException(500, f"Failed to process website: {str(e)}")


@router.get("/")
async def list_websites(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    from app.db.models import WebsiteData
    
    websites = db.query(WebsiteData).filter(
        WebsiteData.user_id == user["id"]
    ).order_by(WebsiteData.created_at.desc()).all()
    
    return [
        {
            "id": w.id,
            "url": w.url,
            "summary": w.summary,
            "chunks_count": w.chunks_count,
            "created_at": w.created_at.isoformat()
        }
        for w in websites
    ]


@router.delete("/{website_id}")
async def delete_website(
    website_id: int,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    from app.db.models import WebsiteData
    
    website = db.query(WebsiteData).filter(
        WebsiteData.id == website_id,
        WebsiteData.user_id == user["id"]
    ).first()
    
    if not website:
        raise HTTPException(404, "Website not found")
    
    db.delete(website)
    db.commit()
    
    return {"message": "Website deleted successfully"}


