from sqlalchemy import Column, Integer, String, DateTime, Text, func
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    company_name = Column(String(255), nullable=True)
    hashed_password = Column(String(255), nullable=False)
    pinecone_namespace = Column(String(255), unique=True, nullable=False)
    bot_token = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    session_id = Column(String(100), index=True, nullable=False)
    summary = Column(Text, nullable=True)   # ADD THIS
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True)
    session_id = Column(String(100), index=True)
    role = Column(String(20), nullable=False)  # user, assistant  <-- ADD THIS
    sender = Column(String(20), nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    filename = Column(String(255), nullable=False)
    file_size = Column(Integer, nullable=False)
    file_type = Column(String(100), nullable=False)
    content = Column(Text, nullable=True)
    chunks_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class TextInformation(Base):
    __tablename__ = "text_information"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    chunks_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class AudioRecording(Base):
    __tablename__ = "audio_recordings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    filename = Column(String(255), nullable=False)
    file_size = Column(Integer, nullable=False)
    file_type = Column(String(100), nullable=False)
    audio_url = Column(String(500), nullable=False)
    transcribed_text = Column(Text, nullable=False)
    duration = Column(Integer, default=0)
    chunks_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class WebsiteData(Base):
    __tablename__ = "website_data"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    url = Column(String(500), nullable=False)
    content = Column(Text, nullable=True)
    summary = Column(Text, nullable=False)
    chunks_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


from sqlalchemy import Column, Integer, String, DateTime, Text, func, Enum, ForeignKey
from app.db.database import Base

# existing models...

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(String(50), unique=True, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    session_id = Column(String(100), index=True, nullable=False)
    visitor_name = Column(String(255), nullable=False)
    visitor_email = Column(String(255), nullable=False)
    visitor_phone = Column(String(50), nullable=True)
    issue = Column(Text, nullable=False)
    status = Column(String(50), nullable=False, default="open")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
