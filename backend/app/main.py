"""
Face Recognition Attendance System API
A FastAPI-based backend for face recognition attendance tracking
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from contextlib import asynccontextmanager
import time
import logging
import asyncio
import threading

from app.routers import auth, employees, attendance, embeddings, streaming, cameras
# from app.routers import system  # Temporarily disabled
from app.config import settings
from db.db_config import create_tables

# Import FTS system components - Temporarily disabled for basic functionality
# from core.fts_system import (
#     start_tracking_service, 
#     shutdown_tracking_service, 
#     is_tracking_running
# )

# Setup logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Global variable to track FTS system initialization
fts_startup_task = None

# Temporarily disabled FTS system for basic functionality
# async def initialize_fts_system():
#     """Initialize the Face Tracking System in the background"""
#     try:
#         logger.info("🔄 Initializing Face Tracking System...")
#         
#         # Run the FTS initialization in a separate thread to avoid blocking
#         def start_fts():
#             try:
#                 start_tracking_service()
#                 logger.info("✅ Face Tracking System initialized successfully")
#             except Exception as e:
#                 logger.error(f"❌ Failed to initialize Face Tracking System: {e}")
#         
#         # Start FTS in background thread
#         fts_thread = threading.Thread(target=start_fts, daemon=True)
#         fts_thread.start()
#         
#         # Give it a moment to start
#         await asyncio.sleep(settings.FTS_STARTUP_DELAY)
#         
#     except Exception as e:
#         logger.error(f"❌ Error during FTS initialization: {e}")

# async def shutdown_fts_system():
#     """Shutdown the Face Tracking System gracefully"""
#     try:
#         if is_tracking_running:
#             logger.info("🔄 Shutting down Face Tracking System...")
#             shutdown_tracking_service()
#             logger.info("✅ Face Tracking System shut down successfully")
#         else:
#             logger.info("ℹ️ Face Tracking System was not running")
#     except Exception as e:
#         logger.error(f"❌ Error during FTS shutdown: {e}")

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler for startup and shutdown events."""
    logger.info("🚀 Starting Face Recognition Attendance System API")
    
    try:
        # Initialize database tables
        create_tables()
        logger.info("✅ Database tables initialized")
        
        # Initialize Face Tracking System as a background service (if enabled)
        # Temporarily disabled for basic functionality
        # if settings.FTS_AUTO_START:
        #     await initialize_fts_system()
        
        logger.info("🎯 Face Recognition Attendance System API is ready!")
        
    except Exception as e:
        logger.error(f"❌ Failed to initialize application: {e}")
        raise
    
    yield
    
    # Shutdown procedures
    logger.info("🛑 Shutting down Face Recognition Attendance System API")
    
    # Gracefully shutdown FTS system
    # Temporarily disabled for basic functionality
    # await shutdown_fts_system()
    
    logger.info("✅ Shutdown complete")

app = FastAPI(
    title="Face Recognition Attendance System",
    description="Professional backend for face recognition-based attendance tracking with role-based access control",
    version="1.0.0",
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
    lifespan=lifespan
)

# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    
    logger.info(
        f"{request.method} {request.url.path} - {response.status_code} - {process_time:.4f}s"
    )
    
    return response

# Security middleware
if settings.ENVIRONMENT == "production":
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=["*"]  # Configure this properly for production
    )

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(employees.router)
app.include_router(attendance.router)
app.include_router(embeddings.router)
app.include_router(streaming.router)
app.include_router(cameras.router)
# app.include_router(system.router)  # Temporarily disabled

@app.get("/")
async def root():
    """Root endpoint with system information"""
    return {
        "message": "Face Recognition Attendance System API",
        "version": "1.0.0",
        "status": "running",
        # "fts_status": "running" if is_tracking_running else "stopped",  # Temporarily disabled
        "docs_url": "/docs" if settings.DEBUG else None
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "environment": settings.ENVIRONMENT,
        # "fts_running": is_tracking_running  # Temporarily disabled
    }
