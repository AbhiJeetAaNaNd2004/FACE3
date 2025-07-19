#!/usr/bin/env python3
"""
Start Face Tracking System Only
This script starts only the Face Tracking System without the API or frontend.
"""

import os
import sys
import time
import signal
import threading
from pathlib import Path

def setup_environment():
    """Set up environment variables for FTS"""
    print("🔧 Setting up FTS environment...")
    
    # PyTorch memory optimization
    os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:128'
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'  # Use only first GPU
    os.environ['OMP_NUM_THREADS'] = '1'
    os.environ['MKL_NUM_THREADS'] = '1'
    os.environ['NUMEXPR_NUM_THREADS'] = '1'
    os.environ['PYTORCH_JIT'] = '0'
    
    print("✅ FTS environment configured")

def start_fts_system():
    """Start the Face Tracking System"""
    print("🚀 Starting Face Tracking System...")
    
    try:
        # Change to backend directory for imports
        backend_path = Path(__file__).parent / "backend"
        sys.path.insert(0, str(backend_path))
        os.chdir(backend_path)
        
        # Import FTS functions
        from core.fts_system import start_tracking_service, shutdown_tracking_service, is_tracking_running, get_system_status
        
        # Start the tracking service
        start_tracking_service()
        
        if is_tracking_running:
            print("✅ Face Tracking System started successfully!")
            print("")
            print("🎯 FTS Status:")
            print("   • Face Detection: Active")
            print("   • Face Recognition: Active") 
            print("   • Multi-Camera Tracking: Active")
            print("   • Attendance Logging: Active")
            print("")
            print("📊 System will display statistics periodically...")
            print("🛑 Press Ctrl+C to stop FTS")
            print("")
            
            # Create shutdown handler
            def signal_handler(signum, frame):
                print("\n🛑 Shutting down Face Tracking System...")
                shutdown_tracking_service()
                print("✅ FTS stopped gracefully")
                sys.exit(0)
            
            signal.signal(signal.SIGINT, signal_handler)
            signal.signal(signal.SIGTERM, signal_handler)
            
            # Run status monitoring loop
            try:
                while is_tracking_running:
                    time.sleep(10)  # Check every 10 seconds
                    
                    try:
                        status = get_system_status()
                        uptime_hours = status.get('uptime', 0) / 3600
                        
                        print(f"📊 FTS Status - Uptime: {uptime_hours:.1f}h | "
                              f"Cameras: {status.get('cam_count', 0)} | "
                              f"Faces: {status.get('faces_detected', 0)} | "
                              f"Attendance: {status.get('attendance_count', 0)}")
                              
                    except Exception as e:
                        print(f"⚠️ Status check error: {e}")
                        
            except KeyboardInterrupt:
                print("\n🛑 Stopping Face Tracking System...")
                shutdown_tracking_service()
                print("✅ FTS stopped")
                
        else:
            print("❌ Failed to start Face Tracking System")
            return False
            
    except ImportError as e:
        print(f"❌ Failed to import FTS modules: {e}")
        print("💡 Make sure you're in the correct directory and dependencies are installed")
        return False
    except Exception as e:
        print(f"❌ Error starting FTS: {e}")
        return False
    
    return True

def check_requirements():
    """Check if FTS requirements are available"""
    print("🔍 Checking FTS requirements...")
    
    required_packages = ['torch', 'cv2', 'insightface', 'faiss', 'numpy']
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'cv2':
                import cv2
            else:
                __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package}")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"⚠️ Missing packages: {', '.join(missing_packages)}")
        print("💡 Install them with: pip install " + " ".join(missing_packages))
        return False
    
    print("✅ All FTS requirements available")
    return True

def check_cameras():
    """Check if cameras are configured"""
    print("🔍 Checking camera configuration...")
    
    try:
        backend_path = Path(__file__).parent / "backend"
        sys.path.insert(0, str(backend_path))
        
        from utils.camera_config_loader import load_active_camera_configs
        
        cameras = load_active_camera_configs()
        
        if cameras:
            print(f"✅ Found {len(cameras)} configured camera(s)")
            for cam in cameras:
                print(f"   • Camera {cam.camera_id} ({cam.camera_type})")
        else:
            print("⚠️ No cameras configured")
            print("💡 Configure cameras through the web interface first")
            
        return len(cameras) > 0
        
    except Exception as e:
        print(f"⚠️ Could not check camera configuration: {e}")
        return True  # Continue anyway

def main():
    print("🎯 Face Recognition System - Face Tracking System Only")
    print("=" * 60)
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    print()
    
    # Check cameras
    check_cameras()
    print()
    
    # Set up environment
    setup_environment()
    print()
    
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description="Start Face Tracking System Only")
    parser.add_argument("--no-camera-check", action="store_true", 
                       help="Skip camera configuration check")
    
    args = parser.parse_args()
    
    if not args.no_camera_check:
        print("💡 Note: Make sure cameras are configured in the database")
        print("   Use the web interface or backend API to configure cameras first")
        print("")
    
    # Start FTS
    if start_fts_system():
        print("✅ FTS session completed!")
    else:
        print("❌ Failed to start FTS")
        sys.exit(1)

if __name__ == "__main__":
    main()