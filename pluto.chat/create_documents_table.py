"""
Migration script to create documents table
Run this to create the documents table in your database
"""
from app.db.database import engine
from app.db.models import Base, Document

def create_documents_table():
    print("Creating documents table...")
    Base.metadata.create_all(bind=engine, tables=[Document.__table__])
    print("✅ Documents table created successfully!")

if __name__ == "__main__":
    create_documents_table()


