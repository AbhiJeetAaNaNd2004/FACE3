import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import logging
from typing import Generator

# Import the Base from our models
from .db_models import Base

# Database configuration - Using SQLite for simplicity
DATABASE_TYPE = os.getenv('DATABASE_TYPE', 'sqlite')

if DATABASE_TYPE == 'sqlite':
    # SQLite configuration
    DATABASE_PATH = os.getenv('DATABASE_PATH', 'face_attendance.db')
    DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
    
    # Create engine with SQLite settings
    engine = create_engine(
        DATABASE_URL,
        poolclass=StaticPool,
        connect_args={
            "check_same_thread": False
        },
        echo=False
    )
else:
    # PostgreSQL configuration (fallback)
    DATABASE_CONFIG = {
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': os.getenv('DB_PORT', '5432'),
        'database': os.getenv('DB_NAME', 'face_attendance'),
        'username': os.getenv('DB_USER', 'postgres'),
        'password': os.getenv('DB_PASSWORD', 'password')
    }
    
    DATABASE_URL = f"postgresql://{DATABASE_CONFIG['username']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"
    
    # Create engine with PostgreSQL settings
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