# 🎯 Face Recognition Attendance System - Complete Setup Guide

## 📋 Table of Contents

1. [System Overview](#-system-overview)
2. [Prerequisites](#-prerequisites)
3. [Quick Start (5 Minutes)](#-quick-start-5-minutes)
4. [Detailed Setup](#-detailed-setup)
5. [Database Configuration](#️-database-configuration)
6. [Environment Variables](#-environment-variables)
7. [Installation & Dependencies](#-installation--dependencies)
8. [Starting the System](#-starting-the-system)
9. [Default Credentials](#-default-credentials)
10. [Verification & Testing](#-verification--testing)
11. [Troubleshooting](#-troubleshooting)
12. [Production Deployment](#-production-deployment)
13. [System Architecture](#-system-architecture)
14. [API Documentation](#-api-documentation)
15. [Face Recognition Setup](#-face-recognition-setup)

---

## 🎯 System Overview

The **Face Recognition Attendance System** is a full-stack application with:

### **Technology Stack**
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

### **Core Features**
- 👤 **Real-time Face Recognition** using InsightFace and OpenCV
- 📊 **Attendance Tracking** with automatic check-in/check-out
- 🎥 **Multi-Camera Support** with live streaming
- 👥 **User Management** with role-based access (Super Admin, Admin, Employee)
- 📈 **Dashboard & Analytics** with real-time statistics
- 🔐 **JWT Authentication** with secure token management
- 🌐 **REST API** with comprehensive endpoints
- 📱 **Responsive Web Interface** with modern UI

---

## 🔧 Prerequisites

### **System Requirements**
| Component | Requirement |
|-----------|-------------|
| **OS** | Linux (Ubuntu 20.04+), Windows 10+, macOS 10.15+ |
| **CPU** | Intel i5 / AMD Ryzen 5 or better |
| **RAM** | 8GB minimum, 16GB recommended |
| **GPU** | Optional: NVIDIA GPU with CUDA for better performance |
| **Storage** | 10GB free space minimum |
| **Camera** | USB/IP camera for face recognition |

### **Software Dependencies**
```bash
# Core requirements
Python 3.8+         # Backend runtime
Node.js 16+         # Frontend build tools
PostgreSQL 12+      # Database server
Git                 # Version control

# Optional (for GPU acceleration)
CUDA Toolkit 11.x   # For GPU-accelerated face recognition
```

---

## ⚡ Quick Start (5 Minutes)

### **1. Clone & Setup**
```bash
# Clone repository
git clone <repository-url>
cd face-recognition-attendance-system

# Copy environment templates
cp .env.example .env
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

### **2. Install Dependencies**
```bash
# Install all dependencies automatically
npm run install:all

# OR manually:
pip3 install -r requirements.txt  # Backend
cd frontend && npm install        # Frontend
```

### **3. Setup Database**
```bash
# Setup PostgreSQL database
npm run setup:postgresql

# Initialize database with sample data
npm run init:db
```

### **4. Start System**
```bash
# Start both frontend and backend
npm run dev

# OR start individually:
npm run dev:backend    # Backend only (http://localhost:8000)
npm run dev:frontend   # Frontend only (http://localhost:3000)
```

### **5. Access System**
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

### **Default Login:**
- **Super Admin**: `admin` / `admin123`
- **HR Manager**: `hr_manager` / `hr123`
- **Employee**: `john.doe` / `john123`

---

## 🛠️ Detailed Setup

### **Step 1: Clone Repository**
```bash
git clone <repository-url>
cd face-recognition-attendance-system
```

### **Step 2: Environment Setup**
```bash
# Check system requirements
python3 --version    # Should be 3.8+
node --version       # Should be 16+
psql --version       # Should be 12+

# Verify Python dependencies can be installed
python3 verify_imports.py

# Test installation
python3 test_installation.py
```

### **Step 3: Environment Variables**
```bash
# Copy templates
cp .env.example .env
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# Edit configurations
nano .env                 # Root configuration
nano backend/.env         # Backend settings
nano frontend/.env        # Frontend settings

# Validate configuration
npm run check:env
```

### **Step 4: PostgreSQL Setup**
```bash
# Install PostgreSQL (Ubuntu/Debian)
sudo apt update
sudo apt install postgresql postgresql-contrib

# Start PostgreSQL
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Create database and user
sudo -u postgres psql
CREATE DATABASE face_attendance_db;
CREATE USER postgres WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE face_attendance_db TO postgres;
\q

# OR use automated setup
npm run setup:postgresql
```

### **Step 5: Install Dependencies**

#### **Backend Dependencies**
```bash
# Core FastAPI dependencies
pip3 install fastapi>=0.116.0
pip3 install uvicorn[standard]>=0.35.0
pip3 install sqlalchemy>=2.0.30
pip3 install python-dotenv>=1.0.0

# Face Recognition dependencies (requires additional setup)
# Note: These may require manual installation
pip3 install opencv-python
pip3 install insightface
pip3 install torch torchvision
pip3 install faiss-cpu  # or faiss-gpu for GPU support

# Install all at once
pip3 install -r requirements.txt
```

#### **Frontend Dependencies**
```bash
cd frontend
npm install

# Key dependencies installed:
# - React 19
# - TypeScript
# - Tailwind CSS
# - Axios (API calls)
# - React Router (routing)
# - Zustand (state management)
```

### **Step 6: Database Initialization**
```bash
# Initialize database tables and sample data
python3 start_unified_server.py --init-db

# OR use the dedicated script
cd backend
python3 init_db.py

# Verify database setup
npm run check:env
```

---

## 🗄️ Database Configuration

### **PostgreSQL Setup (Recommended)**
```env
# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=face_attendance_db
DB_USER=postgres
DB_PASSWORD=your_secure_password
```

### **Database Schema**
The system creates these main tables:
- `employees` - Employee information
- `user_accounts` - Authentication data
- `departments` - Organizational structure
- `attendance_logs` - Attendance records
- `face_embeddings` - Face recognition data
- `camera_configs` - Camera configurations

### **Sample Data Created**
- **Departments**: Engineering, HR, Sales
- **Employees**: John Doe, Jane Smith, Mike Johnson
- **User Accounts**: Admin, HR Manager, Employee users
- **Camera**: Main Entrance Camera (ID: 0)

---

## 🔧 Environment Variables

### **Root .env File**
```env
# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=face_attendance_db
DB_USER=postgres
DB_PASSWORD=your_password

# Security
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# Face Recognition
FACE_RECOGNITION_TOLERANCE=0.6
FACE_DETECTION_MODEL=hog
FACE_ENCODING_MODEL=large

# Camera Settings
DEFAULT_CAMERA_ID=0
MAX_CONCURRENT_STREAMS=5

# Application
DEBUG=true
ENVIRONMENT=development
LOG_LEVEL=INFO
```

### **Frontend .env File**
```env
# API Configuration
REACT_APP_API_URL=http://localhost:8000
REACT_APP_API_BASE_URL=http://localhost:8000

# Build Configuration
GENERATE_SOURCEMAP=false
SKIP_PREFLIGHT_CHECK=true

# Performance
FAST_REFRESH=true
```

---

## 📦 Installation & Dependencies

### **Backend Requirements**
```txt
# Core FastAPI dependencies
fastapi>=0.116.0              # Web framework
uvicorn[standard]>=0.35.0     # ASGI server
python-multipart>=0.0.20     # File uploads

# Database
sqlalchemy>=2.0.30           # ORM
alembic>=1.13.0              # Migrations

# Authentication
python-jose[cryptography]>=3.3.0  # JWT
passlib[bcrypt]>=1.7.4            # Password hashing

# Configuration
pydantic>=2.10.0             # Data validation
pydantic-settings>=2.5.0     # Settings management
python-dotenv>=1.0.0         # Environment variables

# AI/Computer Vision (require manual setup)
opencv-python                # Computer vision
insightface                  # Face recognition
torch                        # Deep learning
faiss-cpu                    # Vector similarity search
```

### **Frontend Dependencies**
```json
{
  "dependencies": {
    "react": "^19.1.0",
    "react-dom": "^19.1.0",
    "typescript": "^4.9.5",
    "react-router-dom": "^7.7.0",
    "axios": "^1.10.0",
    "zustand": "^5.0.6",
    "@headlessui/react": "^2.2.4",
    "@heroicons/react": "^2.2.0",
    "tailwindcss": "^3.4.17"
  }
}
```

### **System Dependencies (Ubuntu/Debian)**
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

# Optional: CUDA for GPU acceleration
# Follow NVIDIA CUDA installation guide
```

---

## 🚀 Starting the System

### **Development Mode (Recommended)**
```bash
# Start both frontend and backend with hot reload
npm run dev

# This runs:
# - Backend: python3 start_unified_server.py --reload (port 8000)
# - Frontend: cd frontend && npm start (port 3000)
```

### **Individual Components**
```bash
# Backend only
npm run dev:backend
# OR
python3 start_unified_server.py --reload

# Frontend only
npm run dev:frontend
# OR
cd frontend && npm start

# Production backend
npm start
# OR
python3 start_unified_server.py
```

### **Advanced Startup Options**
```bash
# Force start (kills conflicting processes)
npm run start:force

# Start on different port
python3 start_unified_server.py --port 8001

# Start with specific number of workers
python3 start_unified_server.py --workers 4

# Initialize database only
python3 start_unified_server.py --init-db

# Start without Face Tracking System
python3 start_unified_server.py --no-fts

# Skip pre-startup checks
python3 start_unified_server.py --skip-checks
```

### **Available NPM Scripts**
```bash
npm run dev                # Start both frontend & backend
npm run dev:backend        # Backend development server
npm run dev:frontend       # Frontend development server
npm run build              # Build frontend for production
npm run start              # Start production backend
npm run start:force        # Force start (cleanup ports)
npm run install:all        # Install all dependencies
npm run init:db            # Initialize database
npm run setup:postgresql   # Setup PostgreSQL
npm run check:env          # Validate environment
npm run cleanup:port       # Clean up port conflicts
npm run test:frontend      # Run frontend tests
npm run test:backend       # Run backend tests
```

---

## 👤 Default Credentials

### **User Accounts Created**
| Username | Password | Role | Description |
|----------|----------|------|-------------|
| `admin` | `admin123` | Super Admin | Full system access |
| `hr_manager` | `hr123` | Admin | HR management access |
| `john.doe` | `john123` | Employee | Employee access |
| `mike.johnson` | `mike123` | Employee | Employee access |

### **Employee Records**
| Employee ID | Name | Department | Role |
|-------------|------|------------|------|
| EMP001 | John Doe | Engineering | Software Engineer |
| EMP002 | Jane Smith | HR | HR Manager |
| EMP003 | Mike Johnson | Engineering | Senior Developer |

### **Access Levels**
- **Super Admin**: User management, system configuration, all features
- **Admin**: Employee management, attendance tracking, camera management
- **Employee**: Personal dashboard, attendance history, profile management

---

## ✅ Verification & Testing

### **1. System Health Check**
```bash
# Check all configurations
npm run check:env

# Test database connection
python3 setup_postgresql.py

# Verify imports
python3 verify_imports.py

# Full installation test
python3 test_installation.py
```

### **2. Service Status**
```bash
# Check if services are running
curl http://localhost:8000/health      # Backend health
curl http://localhost:3000             # Frontend accessibility

# Check specific endpoints
curl http://localhost:8000/docs        # API documentation
curl http://localhost:8000/auth/test   # Authentication test
```

### **3. Face Recognition Test**
```bash
# Test camera access
python3 -c "import cv2; cap = cv2.VideoCapture(0); print('Camera:', cap.isOpened())"

# Test face recognition dependencies
python3 -c "import cv2, insightface; print('Face recognition dependencies OK')"
```

### **4. Database Verification**
```bash
# Connect to database
psql -h localhost -U postgres -d face_attendance_db

# Check tables
\dt

# Check sample data
SELECT * FROM employees;
SELECT username, role FROM user_accounts;
```

---

## 🔧 Troubleshooting

### **Common Issues & Solutions**

#### **Port Already in Use (Error 10048)**
```bash
# Quick fix
npm run start:force

# Manual cleanup
npm run cleanup:port

# Use different port
python3 start_unified_server.py --port 8001
```

#### **Database Connection Failed**
```bash
# Check PostgreSQL status
sudo systemctl status postgresql

# Start PostgreSQL
sudo systemctl start postgresql

# Test connection
psql -h localhost -U postgres -d face_attendance_db

# Reset database
npm run init:db
```

#### **Import Errors**
```bash
# Install missing dependencies
pip3 install -r requirements.txt

# System dependencies (Ubuntu)
sudo apt install python3-dev build-essential

# Clear Python cache
find . -name "__pycache__" -type d -exec rm -rf {} +
```

#### **Face Recognition Issues**
```bash
# Install OpenCV
pip3 install opencv-python

# Install InsightFace (may need manual setup)
pip3 install insightface

# Check camera permissions
sudo usermod -a -G video $USER

# Test camera
ls /dev/video*
```

#### **Frontend Build Issues**
```bash
# Clear cache
cd frontend
rm -rf node_modules package-lock.json
npm install

# Fix permissions
npm audit fix

# Use specific Node version
nvm use 16
```

#### **Environment Variables Not Loading**
```bash
# Check file existence
ls -la .env backend/.env frontend/.env

# Validate configuration
npm run check:env

# Check file permissions
chmod 644 .env backend/.env frontend/.env
```

### **Debug Commands**
```bash
# Backend debug mode
DEBUG=true python3 start_unified_server.py --reload

# Frontend debug
cd frontend
REACT_APP_DEBUG=true npm start

# Database debug
python3 -c "from backend.db.db_config import test_connection; test_connection()"

# Check logs
tail -f backend/logs/app.log
tail -f backend/backend.log
```

---

## 🚀 Production Deployment

### **Environment Setup**
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

### **Backend Deployment**
```bash
# Install production dependencies
pip3 install -r requirements.txt

# Build optimized
python3 -m compileall .

# Start with multiple workers
python3 start_unified_server.py --workers 4 --port 8000

# OR use gunicorn
pip3 install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

### **Frontend Deployment**
```bash
cd frontend

# Build for production
npm run build

# Serve static files (nginx/apache)
# OR use serve
npx serve -s build -l 3000
```

### **Nginx Configuration**
```nginx
server {
    listen 80;
    server_name your-domain.com;

    # Frontend
    location / {
        root /path/to/frontend/build;
        try_files $uri $uri/ /index.html;
    }

    # Backend API
    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # WebSocket support
    location /ws {
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

### **Docker Deployment**
```dockerfile
# Backend Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "start_unified_server.py"]
```

```yaml
# docker-compose.yml
version: '3.8'
services:
  backend:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DB_HOST=postgres
    depends_on:
      - postgres

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"

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

---

## 🏗️ System Architecture

### **Project Structure**
```
face-recognition-attendance-system/
├── 📁 backend/                 # FastAPI backend
│   ├── 📁 app/                 # Application core
│   │   ├── 📄 main.py          # FastAPI app instance
│   │   ├── 📄 config.py        # Configuration settings
│   │   ├── 📄 schemas.py       # Pydantic models
│   │   ├── 📄 security.py      # Authentication logic
│   │   └── 📁 routers/         # API endpoints
│   │       ├── 📄 auth.py      # Authentication routes
│   │       ├── 📄 employees.py # Employee management
│   │       ├── 📄 attendance.py# Attendance tracking
│   │       ├── 📄 cameras.py   # Camera management
│   │       └── 📄 streaming.py # Video streaming
│   ├── 📁 core/                # Core functionality
│   │   ├── 📄 fts_system.py    # Face Tracking System
│   │   └── 📄 face_enroller.py # Face enrollment
│   ├── 📁 db/                  # Database layer
│   │   ├── 📄 db_models.py     # SQLAlchemy models
│   │   ├── 📄 db_config.py     # Database configuration
│   │   └── 📄 db_manager.py    # Database operations
│   └── 📁 utils/               # Utilities
│       ├── 📄 camera_discovery.py
│       └── 📄 logging.py
├── 📁 frontend/                # React frontend
│   ├── 📁 src/
│   │   ├── 📄 App.tsx          # Main application
│   │   ├── 📁 components/      # Reusable components
│   │   ├── 📁 pages/           # Page components
│   │   ├── 📁 services/        # API services
│   │   ├── 📁 store/           # State management
│   │   └── 📁 types/           # TypeScript types
│   └── 📄 package.json
├── 📄 start_unified_server.py  # Main startup script
├── 📄 requirements.txt         # Python dependencies
├── 📄 package.json            # NPM scripts
├── 📄 .env                    # Root configuration
└── 📄 README.md               # Documentation
```

### **API Routes**
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

---

## 📚 API Documentation

### **Access API Docs**
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

### **Authentication**
```bash
# Login
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=admin123"

# Use token
curl -H "Authorization: Bearer your_token_here" \
  "http://localhost:8000/employees"
```

### **Example API Calls**
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

---

## 👁️ Face Recognition Setup

### **Required Models**
The system uses InsightFace models that are automatically downloaded:
- **Detection Model**: RetinaFace or SCRFD
- **Recognition Model**: ArcFace (ResNet50/ResNet100)
- **Age/Gender Model**: Optional for demographics

### **Model Installation**
```bash
# Install InsightFace
pip3 install insightface

# Download models (automatic on first run)
python3 -c "from insightface.app import FaceAnalysis; app = FaceAnalysis(); app.prepare(ctx_id=0)"
```

### **Face Enrollment Process**
1. **Navigate to Employee Management**
2. **Select Employee → Enroll Face**
3. **Capture/Upload Face Images**
4. **System generates face embeddings**
5. **Face is ready for recognition**

### **Camera Configuration**
1. **Go to Camera Management**
2. **Add Camera**: USB (ID: 0,1,2...) or IP Camera
3. **Configure Settings**: Resolution, FPS, Location
4. **Test Camera**: Preview live feed
5. **Activate Camera**: Enable for face recognition

### **Recognition Settings**
```env
# Adjust for accuracy vs speed
FACE_RECOGNITION_TOLERANCE=0.6  # Lower = stricter
FACE_DETECTION_MODEL=hog        # hog (fast) or cnn (accurate)
FACE_ENCODING_MODEL=large       # small (fast) or large (accurate)
```

---

## 🎉 Quick Reference

### **Essential Commands**
```bash
# Setup & Start
npm run install:all              # Install dependencies
npm run setup:postgresql         # Setup database
npm run init:db                  # Initialize data
npm run dev                      # Start development

# Maintenance
npm run check:env                # Validate config
npm run start:force              # Force start
npm run cleanup:port             # Fix port issues

# Testing
python3 test_installation.py     # Test installation
python3 verify_imports.py        # Test imports
npm run test:frontend            # Frontend tests
```

### **Important URLs**
- **Frontend**: http://localhost:3000
- **Backend**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

### **Default Logins**
- **Super Admin**: `admin` / `admin123`
- **Admin**: `hr_manager` / `hr123`
- **Employee**: `john.doe` / `john123`

### **Support Files**
- `ENV_SETUP.md` - Environment configuration guide
- `PORT_CONFLICT_FIX.md` - Port conflict solutions
- `README.md` - General documentation

---

## 📞 Support

### **Debug & Logs**
```bash
# Check logs
tail -f backend/logs/app.log
tail -f backend/backend.log

# Debug mode
DEBUG=true npm run dev:backend
```

### **Common Fixes**
```bash
# Fix dependencies
npm run install:all

# Fix database
npm run setup:postgresql

# Fix ports
npm run cleanup:port

# Reset everything
rm -rf node_modules backend/__pycache__
npm run install:all
npm run init:db
```

🎯 **Your Face Recognition Attendance System is now ready to use!**