#!/usr/bin/env python3
"""
Migration script to create all database tables.
Run this script to initialize the database schema.

Usage: python3 create_tables.py
"""

from app.db.database import engine, Base
from app.db.models import (
    User,
    ChatSession,
    ChatMessage,
    Document,
    TextInformation,
    AudioRecording,
    WebsiteData,
    Ticket
)

def create_all_tables():
    """Create all tables defined in models"""
    print("Creating database tables...")
    try:
        Base.metadata.create_all(bind=engine)
        print("✓ All tables created successfully!")
        print("\nCreated tables:")
        print("  - users")
        print("  - chat_sessions")
        print("  - chat_messages")
        print("  - documents")
        print("  - text_information")
        print("  - audio_recordings")
        print("  - website_data")
        print("  - tickets")
    except Exception as e:
        print(f"✗ Error creating tables: {e}")
        raise

if __name__ == "__main__":
    create_all_tables()
