# 🎯 Face Recognition Attendance System

A comprehensive face recognition-based attendance tracking system with real-time detection, web interface, and role-based access control.

## 🌟 Features

### ✅ Core Functionality
- **Real-time Face Detection & Recognition** - AI-powered attendance tracking
- **Multi-Camera Support** - Process multiple camera feeds simultaneously  
- **Role-Based Access Control** - Super Admin, Admin, and Employee roles
- **Web Dashboard** - Modern React frontend with real-time updates
- **RESTful API** - FastAPI backend with OpenAPI documentation
- **Camera Management** - Auto-discovery and configuration of IP cameras
- **Attendance Tracking** - Automated check-in/check-out with reporting
- **Employee Management** - Complete CRUD operations for staff
- **Live Monitoring** - Real-time camera feeds with detection overlays

### 🔧 Technical Features
- **ONVIF Camera Discovery** - Automatic network camera detection
- **Tripwire Detection** - Configurable entry/exit zones
- **WebSocket Support** - Real-time activity updates
- **Database Management** - SQLite with SQLAlchemy ORM
- **JWT Authentication** - Secure token-based authentication
- **Docker Support** - Containerized deployment option

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <repository-url>
cd face-recognition-attendance-system

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Start the System

```bash
# Start the unified server with face tracking enabled
python start_unified_server.py --enable-fts

# Or start API only (without face detection)
python start_server.py
```

### 3. Access the Application

- **Web Interface**: http://localhost:3000
- **API Documentation**: http://localhost:8000/docs
- **Admin Panel**: Login with super admin credentials

### 4. Default Login Credentials

```
Username: admin
Password: admin
Role: Super Admin
```

## 📋 System Requirements

### Minimum Requirements
- **OS**: Windows 10/11, Ubuntu 18+, macOS 10.14+
- **Python**: 3.8 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 2GB free space
- **Network**: For IP camera connectivity

### Recommended Requirements
- **RAM**: 16GB+ for multiple cameras
- **GPU**: NVIDIA GPU for accelerated processing
- **CPU**: Multi-core processor (Intel i5/AMD Ryzen 5+)

## 🔧 Detailed Installation

### Method 1: Standard Installation

```bash
# Install core dependencies first
pip install fastapi uvicorn sqlalchemy requests

# Install computer vision libraries
pip install opencv-python numpy Pillow

# Install face recognition libraries
pip install onnxruntime faiss-cpu insightface
```

### Method 2: GPU Accelerated Installation

```bash
# For NVIDIA GPU acceleration
pip install faiss-gpu onnxruntime-gpu

# Verify CUDA compatibility
python -c "import torch; print(torch.cuda.is_available())"
```

### Method 3: Docker Installation

```bash
# Build the container
docker build -t face-recognition-attendance .

# Run the container
docker run -p 8000:8000 -p 3000:3000 face-recognition-attendance
```

## 🎛️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Database Configuration
DATABASE_URL=sqlite:///./backend/face_attendance.db

# Security Settings
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# FTS Settings
FTS_AUTO_START=true
FTS_STARTUP_DELAY=3

# Server Settings
DEBUG=true
CORS_ORIGINS=["http://localhost:3000"]
```

### Camera Configuration

The system comes with pre-configured test cameras:

```python
# Test cameras (modify IP addresses for your network)
Main Entrance Camera: 192.168.1.100
Exit Door Camera: 192.168.1.101
Conference Room Camera: 192.168.1.102
```

## 📖 Usage Guide

### Super Admin Functions

1. **User Management**
   - Create/edit/delete user accounts
   - Assign roles and permissions
   - View user activity logs

2. **Camera Management**
   - Discover network cameras
   - Configure camera settings
   - Set up tripwire detection zones
   - Monitor camera status

3. **System Management**
   - Start/stop face tracking system
   - View system performance metrics
   - Access system logs

### Admin Functions

1. **Employee Management**
   - Add/edit employee profiles
   - Upload employee photos for recognition
   - Manage department assignments

2. **Attendance Monitoring**
   - View real-time attendance status
   - Generate attendance reports
   - Monitor entry/exit activities

3. **Live Monitoring**
   - View live camera feeds
   - See real-time face detection
   - Monitor system alerts

### Employee Functions

1. **Personal Dashboard**
   - View personal attendance history
   - Check current status (in/out)
   - Update profile information

## 🔍 Camera Setup

### Supported Camera Types

1. **IP Cameras with RTSP**
   ```
   Format: rtsp://username:password@ip:554/stream1
   Ports: 554, 8554 (common)
   ```

2. **ONVIF Compatible Cameras**
   - Auto-discovery supported
   - Manufacturer info extraction
   - Stream URL detection

3. **USB/Webcams**
   - Use camera ID (0, 1, 2, etc.)
   - Local video devices

### Camera Discovery

1. Navigate to Camera Management
2. Click "Discover Cameras"
3. Enter network range (e.g., 192.168.1.0/24)
4. System will auto-detect compatible cameras
5. Configure discovered cameras

### Manual Camera Configuration

```python
# Example camera configuration
{
    "camera_name": "Main Entrance",
    "camera_type": "entry",
    "ip_address": "192.168.1.100",
    "stream_url": "rtsp://admin:password@192.168.1.100:554/stream1",
    "username": "admin",
    "password": "password",
    "resolution_width": 1920,
    "resolution_height": 1080,
    "fps": 30,
    "is_active": true
}
```

## 🧪 Testing Installation

Run these commands to verify your setup:

```bash
# Test Python imports
python -c "import cv2; print('OpenCV:', cv2.__version__)"
python -c "import numpy; print('NumPy:', numpy.__version__)"
python -c "import insightface; print('InsightFace: OK')"
python -c "import faiss; print('FAISS: OK')"

# Test camera access (if USB camera available)
python -c "import cv2; cap = cv2.VideoCapture(0); print('Camera:', cap.isOpened()); cap.release()"

# Test server startup
python -c "from backend.app.main import app; print('FastAPI: OK')"
```

## 🔧 Troubleshooting

### Common Installation Issues

#### Issue 1: "ModuleNotFoundError: No module named 'cv2'"
```bash
pip uninstall opencv-python opencv-contrib-python opencv-headless
pip install opencv-python
```

#### Issue 2: "Microsoft Visual C++ 14.0 is required" (Windows)
- Download and install Microsoft C++ Build Tools
- Or install Visual Studio Community with C++ support

#### Issue 3: Dependency conflicts with scipy/albumentations
```bash
# Remove conflicting packages
pip uninstall scipy albumentations -y

# Install compatible versions
pip install scipy>=1.10.0

# Retry installation
pip install -r requirements.txt
```

#### Issue 4: FAISS installation fails
```bash
# Try CPU version first
pip install faiss-cpu

# For GPU support (requires CUDA)
pip install faiss-gpu
```

#### Issue 5: InsightFace model download fails
```bash
# Set environment variable for model downloads
export INSIGHTFACE_MODEL_PATH=./models  # Linux/Mac
set INSIGHTFACE_MODEL_PATH=./models     # Windows
```

### Runtime Issues

#### Camera Connection Problems
1. Check camera IP address and credentials
2. Verify RTSP URL format
3. Test connectivity: `ping <camera-ip>`
4. Check firewall settings
5. Verify camera is ONVIF compatible

#### Face Detection Not Working
1. Ensure all AI libraries are installed
2. Check GPU drivers if using GPU acceleration
3. Verify camera resolution and FPS settings
4. Check system resources (RAM/CPU usage)

#### Performance Issues
1. **Reduce camera resolution** - Lower from 1080p to 720p
2. **Decrease FPS** - Set to 15-20 FPS instead of 30
3. **Enable GPU acceleration** - Install GPU versions of libraries
4. **Limit active cameras** - Process fewer cameras simultaneously

### Development Issues

#### Port Conflicts
```bash
# Kill processes using ports 8000 or 3000
python cleanup_port.py
# or manually:
netstat -ano | findstr :8000  # Windows
lsof -ti:8000 | xargs kill -9  # Linux/Mac
```

#### Database Issues
```bash
# Reset database
rm backend/face_attendance.db
python backend/init_db.py
```

## 📊 Performance Optimization

### CPU Optimization
```python
# Reduce frame processing
FRAME_SKIP = 2  # Process every 2nd frame
DETECTION_INTERVAL = 0.1  # 100ms between detections

# Lower resolution
CAMERA_WIDTH = 1280  # Instead of 1920
CAMERA_HEIGHT = 720   # Instead of 1080
```

### GPU Acceleration
```bash
# Install GPU versions
pip install faiss-gpu onnxruntime-gpu torch torchvision

# Verify GPU availability
python -c "import torch; print('CUDA available:', torch.cuda.is_available())"
```

### Memory Management
- **Monitor RAM usage**: Task Manager/htop
- **Limit concurrent cameras**: Max 4 cameras on 8GB RAM
- **Enable frame buffering**: Reduce memory spikes

## 🐳 Docker Deployment

### Build Container
```bash
# Build the image
docker build -t face-recognition-system .

# Run the container
docker run -d \
  --name face-attendance \
  -p 8000:8000 \
  -p 3000:3000 \
  -v $(pwd)/data:/app/data \
  face-recognition-system
```

### Docker Compose
```yaml
version: '3.8'
services:
  face-attendance:
    build: .
    ports:
      - "8000:8000"
      - "3000:3000"
    volumes:
      - ./data:/app/data
      - ./models:/app/models
    environment:
      - FTS_AUTO_START=true
      - DEBUG=false
```

## 🔐 Security Considerations

### Production Deployment
1. **Change default credentials** immediately
2. **Use strong SECRET_KEY** in environment variables
3. **Enable HTTPS** with SSL certificates
4. **Configure firewall** rules for camera networks
5. **Regular security updates** for dependencies

### Data Privacy
- Face embeddings are stored as mathematical vectors
- Original images are not permanently stored
- Employee data is encrypted in database
- Access logs track all system interactions

## 📈 Monitoring and Logging

### System Logs
```bash
# View application logs
tail -f backend/logs/app.log

# View face tracking logs
tail -f backend/logs/fts.log

# Check system status
curl http://localhost:8000/system/status
```

### Performance Metrics
- CPU/Memory usage via `/system/status` endpoint
- Camera processing rates in logs
- Face detection accuracy metrics
- Database query performance

## 🤝 Contributing

### Development Setup
```bash
# Install development dependencies
pip install -r requirements.txt
pip install black flake8 mypy

# Run tests
pytest

# Format code
black .

# Type checking
mypy backend/
```

### Project Structure
```
├── backend/          # FastAPI backend
│   ├── app/         # Main application
│   ├── core/        # Face tracking system
│   ├── db/          # Database models
│   └── utils/       # Utilities
├── frontend/        # React frontend
│   ├── src/         # Source code
│   └── public/      # Static files
├── models/          # AI models (auto-downloaded)
└── data/           # Application data
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

### Getting Help
1. **Check this README** - Most issues are covered here
2. **Review logs** - Check console output for error details
3. **Test installation** - Use the test commands provided
4. **Check GitHub Issues** - Search for similar problems

### Creating Issues
When reporting bugs, include:
- Operating system and Python version
- Complete error messages
- Steps to reproduce the issue
- Output of test commands

## 🚀 What's Next?

### Planned Features
- [ ] Mobile app for employee check-in
- [ ] Advanced analytics and reporting
- [ ] Integration with HR systems
- [ ] Cloud deployment options
- [ ] Multi-tenant support
- [ ] Advanced face anti-spoofing

### Current Status
- ✅ Core face recognition system
- ✅ Web dashboard and API
- ✅ Camera management
- ✅ Real-time monitoring
- ✅ Role-based access control
- ⚠️ AI model optimization (ongoing)
- ⚠️ Performance tuning (ongoing)

---

**Ready to get started?** Run `python start_unified_server.py --enable-fts` and open http://localhost:3000!