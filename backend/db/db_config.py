import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import logging
from typing import Generator

# Load environment variables from backend/.env and root .env
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))  # backend/.env
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))  # root .env

# Import the Base from our models
from .db_models import Base

# Database configuration - supports both PostgreSQL and SQLite
DATABASE_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432'),
    'database': os.getenv('DB_NAME', 'face_attendance_db'),
    'username': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'password')
}

# Check if DATABASE_URL is set in environment, otherwise use PostgreSQL config
DATABASE_URL = os.getenv('DATABASE_URL', f"postgresql://{DATABASE_CONFIG['username']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}")

# Create engine with appropriate settings based on database type
if DATABASE_URL.startswith('sqlite'):
    # SQLite configuration
    engine = create_engine(
        DATABASE_URL,
        echo=False,
        connect_args={"check_same_thread": False}
    )
else:
    # PostgreSQL configuration
    engine = create_engine(
        DATABASE_URL,
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True,
        pool_recycle=3600,
        echo=False,
        connect_args={
            "options": "-c timezone=utc"
        }
    )

# Create sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_session(database_url: str = None) -> Generator:
    """Get database session generator for dependency injection"""
    if database_url:
        # Create a new engine for the provided URL
        temp_engine = create_engine(database_url)
        temp_session = sessionmaker(autocommit=False, autoflush=False, bind=temp_engine)
        db = temp_session()
    else:
        db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()

def close_db_session(db):
    """Close database session safely"""
    try:
        db.close()
    except Exception as e:
        logging.error(f"Error closing database session: {e}")

def create_tables():
    """Create all database tables"""
    try:
        Base.metadata.create_all(bind=engine)
        logging.info("Database tables created successfully")
    except Exception as e:
        logging.error(f"Error creating database tables: {e}")
        raise e

def get_db():
    """Get database session for dependency injection"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_connection():
    """Test database connection"""
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True
    except Exception as e:
        logging.error(f"Database connection failed: {e}")
        return False