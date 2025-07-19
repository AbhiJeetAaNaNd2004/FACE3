"""
System Management Router
Provides endpoints for managing the face detection system
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from typing import Dict, Any
from datetime import datetime
import psutil
import os

from app.schemas import CurrentUser, MessageResponse
from app.security import require_admin_or_above
from utils.logging import get_logger

router = APIRouter(prefix="/system", tags=["System Management"])
logger = get_logger(__name__)

@router.get("/status")
async def get_system_status(
    current_user: CurrentUser = Depends(require_admin_or_above)
):
    """
    Get system status and statistics (Admin+ only)
    """
    try:
        # Get basic system information
        status_data = {
            "timestamp": datetime.now().isoformat(),
            "is_running": True,  # API is running if this endpoint responds
            "fts_status": "not_initialized",  # FTS system not initialized yet
            "system_info": {
                "cpu_percent": psutil.cpu_percent(interval=1),
                "memory_percent": psutil.virtual_memory().percent,
                "disk_percent": psutil.disk_usage('/').percent if os.name != 'nt' else psutil.disk_usage('C:').percent,
                "uptime": "N/A"  # Will be implemented when FTS is integrated
            },
            "camera_status": {
                "total_cameras": 0,
                "active_cameras": 0,
                "processing_cameras": 0
            },
            "face_detection": {
                "faces_detected": 0,
                "identities_recognized": 0,
                "unknown_faces": 0
            }
        }
        
        return {
            "success": True,
            "data": status_data
        }
    except Exception as e:
        logger.error(f"Failed to get system status: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get system status: {str(e)}"
        )

@router.post("/start", response_model=MessageResponse)
async def start_face_detection_system(
    current_user: CurrentUser = Depends(require_admin_or_above)
):
    """
    Start the face detection and tracking system (Admin+ only)
    """
    try:
        logger.info(f"Face detection system start requested by user {current_user.username}")
        
        # For now, return a message that the system is not yet integrated
        return MessageResponse(
            success=False,
            message="Face detection system integration is not yet available. The API is running in basic mode."
        )
    except Exception as e:
        logger.error(f"Failed to start face detection system: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to start face detection system: {str(e)}"
        )

@router.post("/stop", response_model=MessageResponse)
async def stop_face_detection_system(
    current_user: CurrentUser = Depends(require_admin_or_above)
):
    """
    Stop the face detection and tracking system (Admin+ only)
    """
    try:
        logger.info(f"Face detection system stop requested by user {current_user.username}")
        
        return MessageResponse(
            success=False,
            message="Face detection system integration is not yet available. The API is running in basic mode."
        )
    except Exception as e:
        logger.error(f"Failed to stop face detection system: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to stop face detection system: {str(e)}"
        )

@router.get("/health")
async def get_system_health():
    """
    Get basic system health information (no authentication required)
    """
    try:
        health_data = {
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "services": {
                "api": "running",
                "database": "connected",
                "fts": "not_initialized"
            }
        }
        
        return {
            "success": True,
            "data": health_data
        }
    except Exception as e:
        logger.error(f"Failed to get system health: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get system health: {str(e)}"
        )