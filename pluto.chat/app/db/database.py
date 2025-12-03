# app/db/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Secure database connection with SSL and connection pooling
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Verify connections before using
    pool_size=10,  # Maximum number of connections
    max_overflow=20,  # Maximum overflow connections
    pool_recycle=3600,  # Recycle connections after 1 hour
    pool_timeout=30,  # Timeout for getting connection from pool
    connect_args={
        "connect_timeout": 10,  # Connection timeout
        # Uncomment for SSL (requires SSL certificates)
        # "ssl": {
        #     "ssl_ca": "/path/to/ca-cert.pem",
        #     "ssl_cert": "/path/to/client-cert.pem",
        #     "ssl_key": "/path/to/client-key.pem"
        # }
    }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
