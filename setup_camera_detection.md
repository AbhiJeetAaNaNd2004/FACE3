# Camera Detection Setup Guide

## Current Status

### ✅ What Works Now:
- Camera management (CRUD operations)
- Network camera discovery via ONVIF
- Database operations for cameras
- Frontend camera management interface
- Basic camera configuration

### ⚠️ What Needs Setup:
- Face detection and recognition
- Live video processing
- Real-time face tracking

## Required Dependencies

Install the missing computer vision dependencies:

```bash
# Install computer vision libraries
pip install opencv-python>=4.8.0
pip install insightface>=0.7.3
pip install faiss-cpu>=1.7.4  # or faiss-gpu for GPU
pip install onnxruntime>=1.15.0
pip install numpy>=1.24.0
pip install Pillow>=10.0.0

# Or install all at once
pip install -r requirements.txt
```

## Hardware Requirements

### For CPU-Only Setup:
- At least 4GB RAM
- Multi-core processor recommended
- Network access to IP cameras

### For GPU-Accelerated Setup:
```bash
# Install GPU versions instead
pip install faiss-gpu>=1.7.4
pip install onnxruntime-gpu>=1.15.0
```

## Camera Requirements

### Supported Camera Types:
1. **IP Cameras with RTSP**:
   - Format: `rtsp://username:password@ip:554/stream1`
   - Common ports: 554, 8554

2. **ONVIF-Compatible Cameras**:
   - Auto-discovery supported
   - Manufacturer info extracted

3. **USB/Webcams**:
   - Use camera ID (0, 1, 2, etc.)

### Test Camera Configuration:
The system comes with 3 pre-configured test cameras:
- Main Entrance (192.168.1.100)
- Exit Door (192.168.1.101)  
- Conference Room (192.168.1.102)

## Network Setup

### Camera Network Access:
1. Ensure cameras are on accessible network
2. Configure camera credentials in database
3. Test RTSP stream connectivity:
   ```bash
   # Test with VLC or ffplay
   ffplay rtsp://admin:password@192.168.1.100:554/stream1
   ```

### Firewall Configuration:
- Open port 8000 for API
- Open port 3000 for frontend
- Allow outbound RTSP connections (port 554)

## Verification Steps

1. **Start System**:
   ```bash
   python start_unified_server.py --enable-fts
   ```

2. **Check Logs**:
   - Look for "Face Tracking System initialized successfully"
   - Verify camera connections in logs

3. **Test Frontend**:
   - Go to Camera Management
   - Verify cameras are listed
   - Check camera status indicators

4. **Test Face Detection**:
   - Navigate to Live Monitor
   - Should see camera feeds with face detection boxes

## Troubleshooting

### Common Issues:

1. **"ModuleNotFoundError: No module named 'cv2'"**:
   ```bash
   pip install opencv-python
   ```

2. **"Cannot connect to camera"**:
   - Check IP address and credentials
   - Verify RTSP URL format
   - Test network connectivity

3. **"Face detection not working"**:
   - Ensure InsightFace models are downloaded
   - Check GPU availability for acceleration

4. **"FTS system not starting"**:
   - Check environment variable: `FTS_AUTO_START=true`
   - Review startup logs for errors

### Performance Optimization:

1. **For Better Performance**:
   ```bash
   # Use GPU acceleration if available
   pip install faiss-gpu onnxruntime-gpu
   ```

2. **Reduce CPU Usage**:
   - Lower camera FPS in configuration
   - Reduce resolution for processing
   - Use frame skipping

## Expected Functionality After Setup

### ✅ Full Working Features:
- Real-time face detection on camera feeds
- Face recognition against employee database
- Attendance tracking via face recognition
- Live video streaming with detection overlays
- Tripwire crossing detection
- Multi-camera processing
- Real-time activity updates via WebSocket

### 📊 Performance Expectations:
- **CPU-only**: 5-15 FPS per camera
- **GPU-accelerated**: 20-30 FPS per camera
- **Memory usage**: 2-4GB RAM baseline + 1-2GB per active camera