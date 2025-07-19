"""
Face Recognition Attendance System API
A FastAPI-based backend for face recognition attendance tracking
"""

from fastapi import FastAPI, HTTPException, Depends, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from fastapi.websockets import WebSocket, WebSocketDisconnect
import logging
import time
from contextlib import asynccontextmanager
from typing import List
import jwt
from datetime import datetime

from app.config import settings
from app.routers import auth, employees, departments, attendance, cameras, embeddings, streaming, system
from db.db_manager import DatabaseManager
from utils.logging import get_logger

# Set up logging
logger = get_logger(__name__)

# Global WebSocket connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        try:
            await websocket.send_text(message)
        except:
            self.disconnect(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections[:]:  # Create a copy to iterate safely
            try:
                await connection.send_text(message)
            except:
                self.disconnect(connection)

manager = ConnectionManager()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("🚀 Starting Face Recognition Attendance System API")
    
    # Initialize database
    try:
        db_manager = DatabaseManager()
        db_manager.create_tables()
        logger.info("✅ Database tables initialized")
    except Exception as e:
        logger.error(f"❌ Database initialization failed: {e}")
        raise e
    
    logger.info("🎯 Face Recognition Attendance System API is ready!")
    
    yield
    
    # Shutdown
    logger.info("🛑 Shutting down Face Recognition Attendance System API")
    logger.info("✅ Shutdown complete")

# Create FastAPI app with lifespan events
app = FastAPI(
    title="Face Recognition Attendance System API",
    description="API for managing face recognition-based attendance tracking system",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add trusted host middleware for production
if not settings.DEBUG:
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=settings.ALLOWED_HOSTS
    )

# Request timing middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    
    logger.info(f"{request.method} {request.url.path} - {response.status_code} - {process_time:.4f}s")
    return response

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(employees.router, prefix="/employees", tags=["Employee Management"])
app.include_router(departments.router, prefix="/departments", tags=["Department Management"])
app.include_router(attendance.router, prefix="/attendance", tags=["Attendance Tracking"])
app.include_router(cameras.router, prefix="/cameras", tags=["Camera Management"])
app.include_router(embeddings.router, prefix="/embeddings", tags=["Face Embeddings"])
app.include_router(streaming.router, prefix="/streaming", tags=["Video Streaming"])
app.include_router(system.router, prefix="/system", tags=["System Management"])

# WebSocket endpoint for real-time activity updates
@app.websocket("/ws/activity")
async def websocket_activity(websocket: WebSocket, token: str = None):
    """WebSocket endpoint for real-time activity updates"""
    if not token:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return
    
    try:
        # Verify JWT token
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
            return
    except jwt.JWTError:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return
    
    await manager.connect(websocket)
    try:
        while True:
            # Keep connection alive and listen for messages
            data = await websocket.receive_text()
            # Echo back for now - in a real implementation, this would process activity data
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Face Recognition Attendance System API",
        "version": "1.0.0",
        "documentation": "/docs",
        "health": "/health"
    }

# Custom exception handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail, "status_code": exc.status_code}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "status_code": 500}
    )
