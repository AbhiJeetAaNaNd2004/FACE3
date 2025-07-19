# 🎯 Face Recognition Attendance System

A comprehensive face recognition-based attendance tracking system with real-time detection, web interface, and role-based access control.

## 📋 Table of Contents

1. [Features](#-features)
2. [Quick Start](#-quick-start)
3. [System Requirements](#-system-requirements)
4. [Installation](#-installation)
5. [Configuration](#-configuration)
6. [Database Setup](#-database-setup)
7. [Starting the System](#-starting-the-system)
8. [Running Components Separately](#-running-components-separately)
9. [Memory & Performance Fixes](#-memory--performance-fixes)
10. [Default Credentials](#-default-credentials)
11. [Usage Guide](#-usage-guide)
12. [Camera Setup](#-camera-setup)
13. [Troubleshooting](#-troubleshooting)
14. [Environment Configuration](#-environment-configuration)
15. [Performance Optimization](#-performance-optimization)
16. [Production Deployment](#-production-deployment)
17. [API Documentation](#-api-documentation)
18. [Security Considerations](#-security-considerations)
19. [Contributing](#-contributing)

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
- **Database Management** - SQLite/PostgreSQL with SQLAlchemy ORM
- **JWT Authentication** - Secure token-based authentication
- **Docker Support** - Containerized deployment option

### 🏗️ Technology Stack
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│    Frontend     │◄──►│     Backend     │◄──►│   AI/Computer   │
│                 │    │                 │    │     Vision      │
│ • React 19      │    │ • FastAPI       │    │ • InsightFace   │
│ • TypeScript    │    │ • Python 3.8+  │    │ • OpenCV        │
│ • Tailwind CSS  │    │ • PostgreSQL    │    │ • PyTorch       │
│ • Zustand       │    │ • WebSockets    │    │ • FAISS         │
│ • Axios         │    │ • JWT Auth      │    │ • ByteTracker   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🚀 Quick Start

### ⚡ Option 1: Fixed Quick Start (Recommended for Memory Issues)

```bash
# 1. Clone the repository
git clone <repository-url>
cd face-recognition-attendance-system

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# 3. Install all dependencies
pip install -r requirements.txt
cd frontend && npm install && cd ..

# 4. Setup database (PostgreSQL only - no SQLite)
python setup_postgresql.py  # Creates PostgreSQL database
python backend/init_db.py   # Initializes tables and sample data

# 5. Start with memory optimizations (RECOMMENDED)
python start_system_fixed.py
```

### ⚡ Option 2: Standard Quick Start

```bash
# Follow steps 1-4 above, then:

# 5. Start the unified server with face tracking
python start_unified_server.py --enable-fts
```

### 🌐 Access Points
- **Web Interface**: http://localhost:3000
- **API Documentation**: http://localhost:8000/docs
- **Admin Panel**: Login with credentials below

### 👤 Default Login Credentials
```
Super Admin: admin / admin123
HR Manager:  hr_manager / hr123
Employee:    john.doe / john123
```

### 🛠️ Essential Commands

| Command | Description |
|---------|-------------|
| `python start_system_fixed.py` | **RECOMMENDED** - Start with memory fixes |
| `python start_unified_server.py --enable-fts` | Start with face tracking (now explicit) |
| `python start_backend_only.py` | Start API only (no face detection) |
| `python start_frontend_only.py` | Start React frontend only |
| `python start_fts_only.py` | Start Face Tracking System only |
| `python start_camera_detection.py` | Camera discovery and detection |
| `python fix_memory_and_ports.py` | Fix memory and port issues |
| `python cleanup_port.py` | Fix port 8000 conflicts |
| `python test_installation.py` | Verify installation |
| `python setup_postgresql.py` | Setup PostgreSQL database |

## 📋 System Requirements

### Minimum Requirements
- **OS**: Windows 10/11, Ubuntu 18+, macOS 10.14+
- **Python**: 3.8 or higher
- **Node.js**: 16.x or higher (for frontend development)
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 2GB free space
- **Network**: For IP camera connectivity

### Recommended Requirements
- **RAM**: 16GB+ for multiple cameras
- **GPU**: NVIDIA GPU for accelerated processing
- **CPU**: Multi-core processor (Intel i5/AMD Ryzen 5+)
- **Database**: PostgreSQL 12+ (recommended over SQLite)

### Software Dependencies
```bash
# Core requirements
Python 3.8+         # Backend runtime
Node.js 16+         # Frontend build tools (optional)
PostgreSQL 12+      # Database server (recommended)
Git                 # Version control

# Optional (for GPU acceleration)
CUDA Toolkit 11.x   # For GPU-accelerated face recognition
```

## 🔧 Installation

### Method 1: Standard Installation

```bash
# Install core dependencies
pip install fastapi uvicorn sqlalchemy requests python-dotenv

# Install computer vision libraries
pip install opencv-python numpy Pillow

# Install face recognition libraries
pip install onnxruntime faiss-cpu insightface

# Install all dependencies at once
pip install -r requirements.txt
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

### System Dependencies (Ubuntu/Debian)
```bash
# Install system packages
sudo apt update
sudo apt install -y \
  python3 python3-pip python3-dev \
  nodejs npm \
  postgresql postgresql-contrib \
  build-essential cmake \
  libopencv-dev python3-opencv \
  git curl wget
```

## 🎛️ Configuration

### Quick Configuration Setup
```bash
# Copy environment templates
cp .env.example .env
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# Validate configuration
python check_env.py
```

### Root Environment Variables (.env)

Create a `.env` file in the project root:

```env
# Database Configuration - PostgreSQL (Recommended)
DB_TYPE=postgresql
DB_HOST=localhost
DB_PORT=5432
DB_NAME=face_attendance_db
DB_USER=postgres
DB_PASSWORD=your_secure_password_here

# Alternative: SQLite (for development)
# DATABASE_URL=sqlite:///./backend/face_attendance.db

# JWT & Security Configuration
SECRET_KEY=your-secret-key-change-in-production-2024
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# Application Settings
DEBUG=true
ENVIRONMENT=development
LOG_LEVEL=INFO
LOG_FILE=logs/app.log

# Face Recognition Settings
FACE_RECOGNITION_TOLERANCE=0.6
FACE_CONFIDENCE_THRESHOLD=0.6
FACE_DETECTION_MODEL=hog
FACE_ENCODING_MODEL=large
EMBEDDING_MODEL=facenet

# Camera Settings
DEFAULT_CAMERA_ID=0
CAMERA_RESOLUTION_WIDTH=640
CAMERA_RESOLUTION_HEIGHT=480
CAMERA_FPS=30
MAX_CONCURRENT_STREAMS=5
STREAM_QUALITY=medium
FRAME_RATE=30

# CORS Configuration
FRONTEND_URL=http://localhost:3000
ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000,http://localhost:5173,http://127.0.0.1:5173

# File Storage
UPLOAD_DIR=uploads
FACE_IMAGES_DIR=face_images
MAX_FILE_SIZE=10485760

# Face Tracking System Configuration
FTS_AUTO_START=true
FTS_STARTUP_DELAY=3
FACE_TRACKING_AUTO_START=true

# Logging Configuration
LOG_ROTATION=1 day
LOG_RETENTION=30 days
```

### Backend Environment Variables (backend/.env)

```env
# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=face_attendance_db
DB_USER=postgres
DB_PASSWORD=your_secure_password_here

# Security Configuration
SECRET_KEY=your-secret-key-change-in-production-2024
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# Application Configuration
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=INFO

# CORS Configuration
FRONTEND_URL=http://localhost:3000
ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# Face Recognition Configuration
FACE_RECOGNITION_TOLERANCE=0.6
FACE_DETECTION_MODEL=hog
FACE_ENCODING_MODEL=large

# Camera Configuration
DEFAULT_CAMERA_ID=0
MAX_CONCURRENT_STREAMS=5
STREAM_QUALITY=medium
FRAME_RATE=30

# File Storage
UPLOAD_DIR=uploads
FACE_IMAGES_DIR=face_images
MAX_FILE_SIZE=10485760

# Face Tracking System Configuration
FTS_AUTO_START=true
FTS_STARTUP_DELAY=2
```

### Frontend Environment Variables (frontend/.env)

```env
# API Configuration
REACT_APP_API_URL=http://localhost:8000
REACT_APP_API_BASE_URL=http://localhost:8000

# Build Configuration
GENERATE_SOURCEMAP=false
SKIP_PREFLIGHT_CHECK=true

# Development Configuration
FAST_REFRESH=true
ESLINT_NO_DEV_ERRORS=true
DISABLE_ESLINT_PLUGIN=false

# Camera & Media Configuration
REACT_APP_DEFAULT_CAMERA_ID=0
REACT_APP_MAX_FILE_SIZE=10485760

# UI Configuration
REACT_APP_APP_NAME=Face Recognition Attendance System
REACT_APP_VERSION=1.0.0

# Performance Configuration
INLINE_RUNTIME_CHUNK=false
IMAGE_INLINE_SIZE_LIMIT=10000
```

## 🗄️ Database Setup

> **⚠️ Important Note:** This system uses **PostgreSQL only**. SQLite is not supported and has been removed. Docker deployment is not currently supported - use direct installation only.

### PostgreSQL Setup (Required)

#### 1. Install PostgreSQL
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install postgresql postgresql-contrib

# Start PostgreSQL service
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

#### 2. Configure PostgreSQL
```bash
# Switch to postgres user
sudo -u postgres psql

# Create database and user
CREATE DATABASE face_attendance_db;
CREATE USER postgres WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE face_attendance_db TO postgres;
\q
```

#### 3. Automated Setup
```bash
# Use automated setup script
python setup_postgresql.py

# Initialize database with sample data
python backend/init_db.py
```

### SQLite Setup (Alternative)

For development or testing, you can use SQLite:

```env
# In your .env file
DATABASE_URL=sqlite:///./backend/face_attendance.db
```

### Database Schema

The system creates these main tables:
- `employees` - Employee information and profiles
- `user_accounts` - Authentication and user data
- `departments` - Organizational structure
- `attendance_logs` - Attendance records and timestamps
- `face_embeddings` - Face recognition vector data
- `camera_configs` - Camera configurations and settings

### Sample Data

The initialization script creates:
- **Departments**: Engineering, HR, Sales
- **Employees**: John Doe, Jane Smith, Mike Johnson
- **User Accounts**: Admin, HR Manager, Employee users
- **Cameras**: Main Entrance Camera (ID: 0)

## 🚀 Starting the System

### Development Mode (Recommended)
```bash
# Start unified server with face tracking enabled (explicit flag required)
python start_unified_server.py --enable-fts

# This includes:
# - FastAPI backend on port 8000
# - Face tracking system
# - WebSocket support for real-time updates
```

### Production Mode
```bash
# Start production server (without development features)
python start_unified_server.py --workers 4
```

### Individual Components
```bash
# Backend API only (without face detection)
python start_server.py

# Face detection system only
python start_face_detection.py

# Development with auto-reload
python start_unified_server.py --reload
```

### Advanced Startup Options
```bash
# Start with FTS enabled (explicit flag required for stability)
python start_unified_server.py --enable-fts

# Force start (kills conflicting processes)
python start_unified_server.py --force

# Start on different port with FTS
python start_unified_server.py --port 8001 --enable-fts

# Initialize database and start
python start_unified_server.py --init-db

# Start without Face Tracking System (default behavior)
python start_unified_server.py

# Legacy disable flag (same as default now)
python start_unified_server.py --no-fts

# Skip pre-startup checks
python start_unified_server.py --skip-checks
```

> **📝 Note:** FTS is now **disabled by default** for better stability. Use `--enable-fts` to enable Face Tracking System.

### Frontend Development (Optional)
```bash
# If you want to modify the frontend
cd frontend
npm install
npm start  # Starts on http://localhost:3000
```

## 🔧 Running Components Separately

### Backend API Only
Start just the FastAPI backend without Face Tracking System:

```bash
# Start backend API only (port 8000)
python start_backend_only.py

# With custom settings
python start_backend_only.py --host 0.0.0.0 --port 8001 --reload
```

**Features Available:**
- ✅ REST API endpoints
- ✅ Authentication & authorization
- ✅ Employee management
- ✅ Database operations
- ❌ Face detection/recognition
- ❌ Camera processing

### Frontend Only
Start just the React frontend application:

```bash
# Start frontend only (port 3000)
python start_frontend_only.py

# With custom settings
python start_frontend_only.py --port 3001 --browser
```

**Prerequisites:**
- Backend must be running on http://127.0.0.1:8000
- Node.js and npm must be installed

### Face Tracking System Only
Start just the Face Tracking System without API or frontend:

```bash
# Start FTS only
python start_fts_only.py

# Skip camera configuration check
python start_fts_only.py --no-camera-check
```

**Features:**
- ✅ Face detection & recognition
- ✅ Multi-camera tracking
- ✅ Attendance logging to database
- ❌ Web interface
- ❌ REST API

### Camera Detection & Discovery
Discover and test cameras without full system:

```bash
# Discover ONVIF cameras
python start_camera_detection.py --discover

# Test USB cameras
python start_camera_detection.py --test-usb

# Run basic face detection
python start_camera_detection.py --discover --detect

# Test specific camera
python start_camera_detection.py --camera-url rtsp://192.168.1.100:554/stream --detect
```

### Typical Development Workflow

1. **Start Backend** (Terminal 1):
   ```bash
   python start_backend_only.py --reload
   ```

2. **Start Frontend** (Terminal 2):
   ```bash
   python start_frontend_only.py
   ```

3. **Test Cameras** (Terminal 3):
   ```bash
   python start_camera_detection.py --discover
   ```

4. **Start FTS** (Terminal 4):
   ```bash
   python start_fts_only.py
   ```

## ⚠️ Memory & Performance Fixes

### Common Issues Fixed

#### PyTorch Memory Issues
**Error:** `[WinError 1455] The paging file is too small for this operation to complete. Error loading "torch\lib\shm.dll"`

**Solution:** The system now automatically applies these fixes:
- ✅ Set `torch.multiprocessing.set_sharing_strategy('file_system')`
- ✅ Limited thread usage: `torch.set_num_threads(1)`
- ✅ Reduced CUDA memory fraction to 70%
- ✅ Smaller detection size (320x320) for memory efficiency
- ✅ Automatic fallback to CPU-only mode

#### Port Binding Issues
**Error:** `[WinError 10022] An invalid argument was supplied`

**Solution:**
- ✅ Automatic port cleanup before startup
- ✅ Force single-worker mode when FTS enabled
- ✅ Better socket handling
- ✅ Alternative port detection

### Memory Optimization Scripts

```bash
# Fix memory and port issues
python fix_memory_and_ports.py

# Start with all optimizations applied
python start_system_fixed.py
```

### Environment Variables Applied
The fixes automatically set these optimizations:

```bash
PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:128
OMP_NUM_THREADS=1
MKL_NUM_THREADS=1
NUMEXPR_NUM_THREADS=1
PYTORCH_JIT=0
CUDA_VISIBLE_DEVICES=0
```

### Performance Impact

**Before Fixes:**
- ❌ Frequent memory crashes
- ❌ Port binding conflicts
- ❌ High memory usage (~4GB+)
- ❌ Unstable startup

**After Fixes:**
- ✅ Stable memory usage (~2.5GB)
- ✅ Reliable startup process
- ✅ Better error recovery
- ⚠️ Slightly slower detection (due to smaller detection size)

### Troubleshooting Memory Issues

#### If memory issues persist:
1. **Check available RAM:**
   ```bash
   python -c "import psutil; print(f'Available RAM: {psutil.virtual_memory().available / (1024**3):.2f} GB')"
   ```

2. **Try CPU-only mode:**
   ```bash
   export CUDA_VISIBLE_DEVICES=""
   python start_system_fixed.py
   ```

3. **Close memory-intensive applications**

4. **Use components separately:**
   ```bash
   # Start backend only first
   python start_backend_only.py
   
   # Then frontend
   python start_frontend_only.py
   
   # Then FTS when ready
   python start_fts_only.py
   ```

## 👤 Default Credentials

### User Accounts Created

| Username | Password | Role | Description |
|----------|----------|------|-------------|
| `admin` | `admin123` | Super Admin | Full system access, user management |
| `hr_manager` | `hr123` | Admin | HR management, employee operations |
| `john.doe` | `john123` | Employee | Personal dashboard access |
| `mike.johnson` | `mike123` | Employee | Personal dashboard access |

### Employee Records

| Employee ID | Name | Department | Role |
|-------------|------|------------|------|
| EMP001 | John Doe | Engineering | Software Engineer |
| EMP002 | Jane Smith | HR | HR Manager |
| EMP003 | Mike Johnson | Engineering | Senior Developer |

### Access Levels

- **Super Admin**: User management, system configuration, all features
- **Admin**: Employee management, attendance tracking, camera management
- **Employee**: Personal dashboard, attendance history, profile management

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

### Pre-configured Test Cameras

The system comes with test cameras configured:

```python
# Test cameras (modify IP addresses for your network)
Main Entrance Camera: 192.168.1.100
Exit Door Camera: 192.168.1.101
Conference Room Camera: 192.168.1.102
```

### Camera Discovery Process

1. Navigate to Camera Management in the web interface
2. Click "Discover Cameras"
3. Enter network range (e.g., 192.168.1.0/24)
4. System will auto-detect compatible cameras
5. Configure discovered cameras with credentials

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

### Face Enrollment Process

1. **Navigate to Employee Management**
2. **Select Employee → Enroll Face**
3. **Capture/Upload Face Images**
4. **System generates face embeddings**
5. **Face is ready for recognition**

## 🔧 Troubleshooting

### Quick Fixes for Common Issues

#### 🔥 Memory/Performance Issues (Most Common)
```bash
# FIRST: Try the optimized startup (fixes 90% of issues)
python start_system_fixed.py

# OR: Run memory fixes manually
python fix_memory_and_ports.py
```

#### 🔌 Port Conflicts
```bash
# Clean up port 8000
python cleanup_port.py

# Or kill specific port
python fix_memory_and_ports.py
```

#### 🚫 PyTorch Shared Memory Errors
**Error:** `[WinError 1455] The paging file is too small`

**Solution:** Already fixed in the optimized scripts above, but if needed manually:
```bash
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:128
export OMP_NUM_THREADS=1
python start_system_fixed.py
```

### Installation Verification

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

# Run comprehensive test
python test_installation.py
```

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

#### Database Issues
```bash
# Test database connection
python setup_postgresql.py

# Reset database
python backend/init_db.py

# Check database status
psql -h localhost -U postgres -d face_attendance_db
```

## 🚨 Port Conflict Solutions

### The Problem
The error `[Errno 10048] error while attempting to bind on address ('0.0.0.0', 8000)` occurs when:

1. Another process is already using port 8000
2. A previous server instance didn't shut down properly
3. Another application is bound to port 8000

### Solutions (Multiple Options)

#### Option 1: Automatic Fix (Recommended)
```bash
# Force start with automatic port cleanup
python start_unified_server.py --force
```

#### Option 2: Manual Port Cleanup
```bash
# Clean up port 8000 first, then start normally
python cleanup_port.py
python start_unified_server.py
```

#### Option 3: Use Cleanup Scripts
```bash
# Linux/Mac:
./fix_port_conflict.sh

# Windows:
fix_port_conflict.bat
```

#### Option 4: Use Different Port
```bash
# Start server on a different port (e.g., 8001)
python start_unified_server.py --port 8001
```

#### Option 5: Manual Process Termination

**Windows:**
```cmd
# Find process using port 8000
netstat -ano | findstr :8000

# Kill the process (replace <PID> with actual process ID)
taskkill /f /pid <PID>
```

**Linux/Mac:**
```bash
# Find and kill process using port 8000
lsof -ti:8000 | xargs kill -9
```

### Prevention Tips

1. **Always use Ctrl+C to stop the server** instead of closing the terminal window
2. **Use the `--force` flag** when you know port conflicts might occur
3. **Check running processes** before starting if issues persist
4. **Use different ports** for multiple instances

### Testing the Fix

```bash
# Test port availability
python cleanup_port.py 8000

# Test server startup with force cleanup
python start_unified_server.py --force

# Test alternative port
python start_unified_server.py --port 8001
```

## 🌍 Environment Configuration

### Configuration Validation

```bash
# Check all environment files exist
ls -la .env backend/.env frontend/.env

# Validate configuration
python check_env.py

# Test database connection
python setup_postgresql.py
```

### Configuration Options Reference

#### Security Settings
- **SECRET_KEY**: JWT signing key (change in production!)
- **ALGORITHM**: JWT algorithm (HS256 recommended)
- **ACCESS_TOKEN_EXPIRE_MINUTES**: Token expiration time

#### Face Recognition Settings
- **FACE_RECOGNITION_TOLERANCE**: Recognition sensitivity (0.4-0.8)
- **FACE_DETECTION_MODEL**: Detection algorithm (hog/cnn)
- **FACE_ENCODING_MODEL**: Encoding quality (small/large)

#### Camera Settings
- **DEFAULT_CAMERA_ID**: Default camera index (0 for built-in)
- **MAX_CONCURRENT_STREAMS**: Maximum simultaneous camera streams
- **STREAM_QUALITY**: Video quality (low/medium/high)

#### File Storage
- **UPLOAD_DIR**: Directory for file uploads
- **FACE_IMAGES_DIR**: Directory for face images
- **MAX_FILE_SIZE**: Maximum upload file size in bytes

### Common Configuration Issues

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'dotenv'` | Install python-dotenv: `pip install python-dotenv` |
| Database connection failed | Check PostgreSQL service and credentials |
| Frontend can't connect to API | Check REACT_APP_API_URL in frontend/.env |
| Face recognition not working | Verify camera permissions and face recognition settings |

## 📊 Performance Optimization

### CPU Optimization
```python
# In your configuration (.env file)
FRAME_SKIP=2  # Process every 2nd frame
DETECTION_INTERVAL=0.1  # 100ms between detections

# Lower resolution
CAMERA_WIDTH=1280  # Instead of 1920
CAMERA_HEIGHT=720   # Instead of 1080
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

## 🚀 Production Deployment

### Environment Setup
```env
# Production .env settings
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=WARNING

# Strong security
SECRET_KEY=your-very-strong-production-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Database
DB_HOST=your-production-db-host
DB_PASSWORD=your-strong-database-password

# Performance
MAX_CONCURRENT_STREAMS=3
FACE_RECOGNITION_TOLERANCE=0.5
```

### Docker Deployment

#### Build Container
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

#### Docker Compose
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
    depends_on:
      - postgres

  postgres:
    image: postgres:13
    environment:
      POSTGRES_DB: face_attendance_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### Production Considerations

#### Security
- [ ] Change SECRET_KEY to a strong, unique value
- [ ] Use environment-specific database credentials
- [ ] Set DEBUG=false
- [ ] Configure proper CORS origins
- [ ] Use HTTPS URLs in production

#### Performance
- [ ] Set appropriate FACE_RECOGNITION_TOLERANCE
- [ ] Configure MAX_CONCURRENT_STREAMS based on hardware
- [ ] Set LOG_LEVEL=WARNING or ERROR in production
- [ ] Enable GPU acceleration if available

#### Database
- [ ] Use separate database for production
- [ ] Configure database connection pooling
- [ ] Set up database backups
- [ ] Monitor database performance

## 📚 API Documentation

### Access API Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

### API Routes Overview
```
🔐 Authentication (/auth)
├── POST /login              # User login
├── POST /logout             # User logout
└── GET  /me                 # Current user info

👥 Employees (/employees)
├── GET    /employees        # List employees
├── POST   /employees        # Create employee
├── PUT    /employees/{id}   # Update employee
└── DELETE /employees/{id}   # Delete employee

📊 Attendance (/attendance)
├── GET  /attendance         # Attendance records
├── POST /attendance/checkin # Manual check-in
└── POST /attendance/checkout# Manual check-out

🎥 Cameras (/cameras)
├── GET  /cameras            # List cameras
├── POST /cameras            # Add camera
└── PUT  /cameras/{id}       # Update camera

🎦 Streaming (/streaming)
├── GET  /stream/{camera_id} # Live video stream
└── WS   /ws/video           # WebSocket video feed
```

### Authentication
```bash
# Login
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=admin123"

# Use token
curl -H "Authorization: Bearer your_token_here" \
  "http://localhost:8000/employees"
```

### Example API Calls
```bash
# Get employees
curl "http://localhost:8000/employees" \
  -H "Authorization: Bearer $TOKEN"

# Create employee
curl -X POST "http://localhost:8000/employees" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "employee_id": "EMP004",
    "name": "New Employee",
    "department_id": 1,
    "role": "Developer"
  }'

# Get attendance records
curl "http://localhost:8000/attendance" \
  -H "Authorization: Bearer $TOKEN"
```

## 🔐 Security Considerations

### Production Security Checklist
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

### Monitoring and Logging

#### System Logs
```bash
# View application logs
tail -f backend/logs/app.log

# View face tracking logs
tail -f backend/logs/fts.log

# Check system status
curl http://localhost:8000/system/status
```

#### Performance Metrics
- CPU/Memory usage via `/system/status` endpoint
- Camera processing rates in logs
- Face detection accuracy metrics
- Database query performance

## 📋 Summary & Best Practices

### ✅ Recommended Startup Sequence

1. **First Time Setup:**
   ```bash
   python setup_postgresql.py
   python backend/init_db.py
   ```

2. **Start System (Choose One):**
   ```bash
   # Option A: Fixed startup (recommended for memory issues)
   python start_system_fixed.py
   
   # Option B: Standard startup with FTS
   python start_unified_server.py --enable-fts
   
   # Option C: Separate components for development
   python start_backend_only.py    # Terminal 1
   python start_frontend_only.py   # Terminal 2
   python start_fts_only.py        # Terminal 3 (optional)
   ```

3. **Test Cameras:**
   ```bash
   python start_camera_detection.py --discover --test-usb
   ```

### 🚫 What NOT to Use

- ❌ **SQLite** - Removed, use PostgreSQL only
- ❌ **Docker** - Not supported currently
- ❌ **Multiple workers with FTS** - Causes memory conflicts
- ❌ **Standard startup if having memory issues** - Use `start_system_fixed.py`

### ⚡ Performance Tips

- ✅ Use `start_system_fixed.py` for stable operation
- ✅ Start components separately for development
- ✅ Monitor memory usage during operation
- ✅ Use CPU-only mode if GPU memory issues persist
- ✅ Close other memory-intensive applications

### 🔧 If Something Goes Wrong

1. **Memory issues:** `python start_system_fixed.py`
2. **Port conflicts:** `python fix_memory_and_ports.py`
3. **Camera issues:** `python start_camera_detection.py --discover`
4. **Database issues:** `python setup_postgresql.py`
5. **Import errors:** `python test_installation.py`

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

## 🆘 Quick Reference & Emergency Commands

### Essential Commands
```bash
# Quick Setup
python setup_postgresql.py && python backend/init_db.py

# Start System
python start_unified_server.py --enable-fts

# Fix Common Issues
python cleanup_port.py                    # Fix port conflicts
python test_installation.py              # Test installation
python verify_imports.py                 # Test imports

# Emergency Reset
rm -rf backend/__pycache__ models/
python backend/init_db.py
```

### Important URLs
- **Frontend**: http://localhost:3000
- **Backend**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

### Default Logins (Change in Production!)
- **Super Admin**: `admin` / `admin123`
- **Admin**: `hr_manager` / `hr123`
- **Employee**: `john.doe` / `john123`

### Debug Commands
```bash
# Backend debug mode
DEBUG=true python start_unified_server.py --reload

# Check logs
tail -f backend/logs/app.log

# Database debug
python -c "from backend.db.db_config import test_connection; test_connection()"
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

### Getting Help
1. **Check this README** - Most issues are covered here
2. **Review logs** - Check console output for error details
3. **Test installation** - Use `python test_installation.py`
4. **Check GitHub Issues** - Search for similar problems

### Creating Issues
When reporting bugs, include:
- Operating system and Python version
- Complete error messages
- Steps to reproduce the issue
- Output of `python test_installation.py`

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