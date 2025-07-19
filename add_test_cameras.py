#!/usr/bin/env python3
"""
Script to add test cameras to the database for testing purposes
"""

import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backend'))

from backend.db.db_manager import DatabaseManager
from backend.db.db_models import CameraConfig

def add_test_cameras():
    """Add test cameras to the database"""
    db_manager = DatabaseManager()
    
    # Test cameras data
    test_cameras = [
        {
            'camera_id': 1,
            'camera_name': 'Main Entrance Camera',
            'camera_type': 'entry',
            'ip_address': '192.168.1.100',
            'stream_url': 'rtsp://192.168.1.100:554/stream1',
            'username': 'admin',
            'password': 'admin123',
            'resolution_width': 1920,
            'resolution_height': 1080,
            'fps': 30,
            'gpu_id': 0,
            'status': 'configured',
            'is_active': True,
            'location_description': 'Main entrance of the building',
            'manufacturer': 'Hikvision',
            'model': 'DS-2CD2085G1-I',
            'firmware_version': 'V5.7.3',
            'onvif_supported': True
        },
        {
            'camera_id': 2,
            'camera_name': 'Exit Door Camera',
            'camera_type': 'exit',
            'ip_address': '192.168.1.101',
            'stream_url': 'rtsp://192.168.1.101:554/stream1',
            'username': 'admin',
            'password': 'admin123',
            'resolution_width': 1920,
            'resolution_height': 1080,
            'fps': 30,
            'gpu_id': 0,
            'status': 'configured',
            'is_active': True,
            'location_description': 'Exit door of the building',
            'manufacturer': 'Dahua',
            'model': 'IPC-HFW4831E-SE',
            'firmware_version': 'V2.800.0000016.0.R',
            'onvif_supported': True
        },
        {
            'camera_id': 3,
            'camera_name': 'Conference Room Camera',
            'camera_type': 'general',
            'ip_address': '192.168.1.102',
            'stream_url': 'rtsp://192.168.1.102:554/stream1',
            'username': 'admin',
            'password': 'admin123',
            'resolution_width': 1280,
            'resolution_height': 720,
            'fps': 25,
            'gpu_id': 0,
            'status': 'configured',
            'is_active': False,
            'location_description': 'Conference room monitoring',
            'manufacturer': 'Axis',
            'model': 'M3046-V',
            'firmware_version': '9.80.1',
            'onvif_supported': True
        }
    ]
    
    session = db_manager.Session()
    
    try:
        # Check if cameras already exist
        existing_cameras = session.query(CameraConfig).all()
        if existing_cameras:
            print(f"Found {len(existing_cameras)} existing cameras. Skipping creation.")
            return
        
        # Add test cameras
        for camera_data in test_cameras:
            camera = CameraConfig(**camera_data)
            session.add(camera)
        
        session.commit()
        print(f"Successfully added {len(test_cameras)} test cameras to the database.")
        
        # Display added cameras
        for camera_data in test_cameras:
            print(f"  - {camera_data['camera_name']} (ID: {camera_data['camera_id']}) - {camera_data['ip_address']}")
            
    except Exception as e:
        session.rollback()
        print(f"Error adding test cameras: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    print("Adding test cameras to the database...")
    add_test_cameras()
    print("Done.")