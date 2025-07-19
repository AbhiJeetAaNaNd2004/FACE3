# Face Recognition Attendance System

A complete, production-ready Face Recognition Attendance System built with FastAPI backend and React frontend. This system provides real-time face recognition for employee attendance tracking with a modern, responsive web interface and advanced camera management capabilities.

## 📋 Table of Contents

- [Features](#-features)
- [System Architecture](#️-system-architecture)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Starting the System](#-starting-the-system)
- [User Roles & Permissions](#-user-roles--permissions)
- [API Documentation](#-api-documentation)
- [Face Recognition System](#-face-recognition-system)
- [Camera Management](#-camera-management)
- [Development](#️-development)
- [Troubleshooting](#-troubleshooting)
- [System Monitoring](#-system-monitoring)
- [Deployment](#-deployment)
- [Contributing](#-contributing)

## 🌟 Features

### Backend Features
- **FastAPI-based RESTful API** with automatic documentation
- **Real-time Face Recognition** using OpenCV and InsightFace
- **JWT Authentication** with role-based access control
- **PostgreSQL Database** with SQLAlchemy ORM
- **WebSocket Support** for real-time updates
- **ONVIF Camera Discovery** with automated network scanning
- **Employee Management** with face enrollment and department tracking
- **Attendance Tracking** with confidence scoring and detailed logs
- **Multi-GPU Support** for face recognition processing
- **FAISS Vector Search** for fast face matching
- **ByteTracker Integration** for object tracking

### Frontend Features
- **Modern React UI** with TypeScript and Tailwind CSS
- **Role-based Dashboards** (Super Admin, Admin, Employee)
- **Real-time Camera Feeds** with live face detection overlays
- **Employee Management** with drag-and-drop face enrollment
- **Attendance Analytics** with charts and reporting
- **Camera Configuration** with tripwire management
- **Department Management** with organizational structure
- **Live Activity Feed** with WebSocket integration
- **Responsive Design** optimized for all devices

## 🏗️ System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React Frontend │    │  FastAPI Backend │    │ Face Tracking   │
│   (Port 3000)   │    │   (Port 8000)    │    │    System       │
│                 │    │                 │    │                 │
│ • TypeScript    │◄──►│ • REST API      │◄──►│ • InsightFace   │
│ • Tailwind CSS  │    │ • WebSockets    │    │ • OpenCV        │
│ • Zustand Store │    │ • JWT Auth      │    │ • FAISS Index   │
│ • React Router  │    │ • SQLAlchemy    │    │ • ByteTracker   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                        ┌─────────────────┐
                        │ PostgreSQL DB   │
                        │                 │
                        │ • User Accounts │
                        │ • Employees     │
                        │ • Departments   │
                        │ • Attendance    │
                        │ • Face Data     │
                        │ • Cameras       │
                        │ • Tripwires     │
                        └─────────────────┘
```

## 📋 Prerequisites

### Required Software
- **Python 3.8+** with pip
- **Node.js 16+** with npm
- **PostgreSQL 12+** database server
- **Git** for version control

### System Requirements
- **RAM**: Minimum 4GB, Recommended 8GB+
- **Storage**: 2GB+ available space
- **GPU**: Optional but recommended for face recognition (CUDA compatible)
- **Camera**: USB webcam or IP camera with RTSP/HTTP stream support

### Python Dependencies
The system requires several computer vision and machine learning libraries:
- **OpenCV** (`cv2`) for image processing
- **InsightFace** for face recognition models
- **FAISS** for fast similarity search
- **PyTorch** for deep learning models
- **ByteTracker** for object tracking
- **FastAPI** for the web framework
- **SQLAlchemy** for database operations

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd face-recognition-attendance-system
```

### 2. Set Up PostgreSQL Database
```bash
# Install PostgreSQL (Ubuntu/Debian)
sudo apt update
sudo apt install postgresql postgresql-contrib

# Create database and user
sudo -u postgres psql
CREATE DATABASE frs_db;
CREATE USER frs_user WITH PASSWORD 'frs_password';
GRANT ALL PRIVILEGES ON DATABASE frs_db TO frs_user;
\q
```

### 3. Configure Environment Variables
```bash
# Copy and edit the environment file
cp .env.example .env

# Edit .env with your configuration:
nano .env
```

**Environment Configuration (.env):**
```env
# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=frs_db
DB_USER=frs_user
DB_PASSWORD=frs_password

# Security
SECRET_KEY=your-very-secure-secret-key-change-in-production
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24

# Application Settings
DEBUG=true
ENVIRONMENT=development
LOG_LEVEL=INFO

# Face Recognition Settings
FACE_CONFIDENCE_THRESHOLD=0.6
EMBEDDING_MODEL=facenet
FACE_DETECTION_MODEL=mtcnn

# Camera Settings
DEFAULT_CAMERA_ID=0
CAMERA_RESOLUTION_WIDTH=640
CAMERA_RESOLUTION_HEIGHT=480
CAMERA_FPS=30
```

### 4. Install Dependencies
```bash
# Run the automated setup script
chmod +x setup_dev.sh
./setup_dev.sh

# Or install manually:
# Backend dependencies
pip install -r requirements.txt

# Frontend dependencies
cd frontend && npm install && cd ..
```

### 5. Initialize Database
```bash
# Initialize database with tables and sample data
python start_unified_server.py --init-db
```

### 6. Test Installation
```bash
# Verify all components are working
python test_installation.py
```

## 📁 Project Structure

```
face-recognition-attendance-system/
├── backend/                     # FastAPI backend application
│   ├── app/                     # Main application
│   │   ├── routers/             # API route handlers
│   │   │   ├── auth.py          # Authentication endpoints
│   │   │   ├── employees.py     # Employee management
│   │   │   ├── attendance.py    # Attendance tracking
│   │   │   ├── cameras.py       # Camera management
│   │   │   ├── departments.py   # Department management
│   │   │   ├── streaming.py     # Live camera streams
│   │   │   └── system.py        # System management
│   │   ├── main.py              # FastAPI application entry point
│   │   ├── config.py            # Application configuration
│   │   ├── schemas.py           # Pydantic data models
│   │   ├── security.py          # Authentication utilities
│   │   └── dependencies.py      # Dependency injection
│   ├── core/                    # Core business logic
│   │   ├── fts_system.py        # Face Tracking System
│   │   └── face_enroller.py     # Face enrollment logic
│   ├── db/                      # Database layer
│   │   ├── db_models.py         # SQLAlchemy models
│   │   ├── db_config.py         # Database configuration
│   │   └── db_manager.py        # Database operations
│   ├── utils/                   # Utility modules
│   │   ├── camera_discovery.py  # ONVIF camera discovery
│   │   ├── camera_config_loader.py # Configuration loader
│   │   ├── logging.py           # Logging utilities
│   │   └── security.py          # Security utilities
│   ├── tasks/                   # Background tasks
│   │   └── camera_tasks.py      # Camera processing tasks
│   └── init_db.py               # Database initialization script
├── frontend/                    # React frontend application
│   ├── src/
│   │   ├── components/          # Reusable UI components
│   │   │   ├── ui/              # Base UI components
│   │   │   ├── layout/          # Layout components
│   │   │   ├── camera/          # Camera components
│   │   │   └── admin/           # Admin components
│   │   ├── pages/               # Page components
│   │   │   ├── login/           # Login page
│   │   │   ├── super-admin/     # Super admin pages
│   │   │   ├── admin/           # Admin pages
│   │   │   └── employee/        # Employee pages
│   │   ├── store/               # Zustand state management
│   │   ├── services/            # API service layer
│   │   ├── hooks/               # Custom React hooks
│   │   ├── types/               # TypeScript type definitions
│   │   └── utils/               # Utility functions
│   ├── public/                  # Static assets
│   ├── package.json             # Node.js dependencies
│   └── tailwind.config.js       # Tailwind CSS configuration
├── start_unified_server.py      # Main server startup script
├── start_face_detection.py      # Face detection startup utility
├── start_server.py              # Alternative server startup
├── setup_dev.sh                 # Development setup script
├── test_installation.py         # Installation verification
├── verify_imports.py            # Import verification utility
├── package.json                 # Root package.json with scripts
├── requirements.txt             # Python dependencies
└── README.md                    # This documentation
```

## 🔧 Configuration

### Database Configuration
The system uses PostgreSQL as the primary database. Key configuration options in `backend/app/config.py`:

- **Connection Settings**: Host, port, database name, credentials
- **Connection Pooling**: Pool size, overflow, ping settings
- **Session Management**: Auto-commit, auto-flush behavior

### Face Recognition Configuration
Advanced settings for the face recognition system:

- **Models**: InsightFace models for face detection and recognition
- **Thresholds**: Confidence thresholds for face matching
- **Processing**: GPU settings, batch size, optimization flags
- **Storage**: Face embedding storage and indexing with FAISS

### Camera Configuration
Camera system supports various input sources:

- **USB Cameras**: Direct connection via device ID (0, 1, 2...)
- **IP Cameras**: RTSP and HTTP streams with authentication
- **ONVIF Cameras**: Professional cameras with discovery protocol
- **Network Cameras**: Custom URL configurations

## 🎮 Starting the System

### Quick Start (Recommended)
```bash
# Start both backend and frontend
npm run dev
```

### Individual Components
```bash
# Backend only (with face tracking)
python start_unified_server.py

# Backend with auto-reload (development)
python start_unified_server.py --reload

# Frontend only
cd frontend && npm start

# Initialize database only
python start_unified_server.py --init-db
```

### Using Package Scripts
```bash
# Install all dependencies
npm run install:all

# Start development servers
npm run dev

# Build for production
npm run build

# Run tests
npm run test:frontend
npm run test:backend
```

### Access URLs
- **Frontend Application**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Alternative API Docs**: http://localhost:8000/redoc

### Default Login Credentials
| Role | Username | Password | Permissions |
|------|----------|----------|-------------|
| Super Admin | `superadmin` | `admin123` | Full system access |
| Admin | `admin` | `admin123` | Employee & camera management |
| Employee | `employee` | `employee123` | Personal dashboard only |

## 🎯 User Roles & Permissions

### Super Admin
- **Complete System Control**: All features and settings
- **User Management**: Create, edit, delete user accounts
- **System Configuration**: Database, cameras, global settings
- **Department Management**: Create and manage organizational structure
- **Advanced Analytics**: Comprehensive reporting and insights
- **Camera Discovery**: Network scanning and ONVIF discovery

### Admin
- **Employee Management**: Enroll faces, manage employee data
- **Attendance Tracking**: View and manage attendance records
- **Camera Management**: Configure cameras and tripwires
- **Department Access**: Manage assigned departments
- **Live Monitoring**: Real-time face detection and tracking
- **Basic Analytics**: Attendance reports and statistics

### Employee
- **Personal Dashboard**: View own attendance history
- **Attendance Status**: Check current status and daily summary
- **Colleague Presence**: See who's currently present
- **Profile Management**: Update personal information
- **Limited Analytics**: Personal attendance patterns

## 📚 API Documentation

### Core Endpoints

#### Authentication (`/auth`)
- `POST /auth/login` - User authentication with JWT tokens
- `POST /auth/logout` - Secure logout and token invalidation
- `GET /auth/me` - Get current user profile and permissions

#### Employee Management (`/employees`)
- `GET /employees/` - List employees with filtering and pagination
- `POST /employees/` - Create new employee record
- `PUT /employees/{id}` - Update employee information
- `DELETE /employees/{id}` - Remove employee (admin only)
- `POST /employees/enroll` - Enroll face with image upload

#### Attendance (`/attendance`)
- `GET /attendance/` - Get attendance records with filters
- `POST /attendance/manual` - Manual attendance entry
- `GET /attendance/summary` - Attendance statistics and summaries
- `GET /attendance/employee/{id}` - Individual employee history

#### Camera Management (`/cameras`)
- `POST /cameras/discover` - ONVIF network camera discovery
- `GET /cameras/` - List configured cameras
- `POST /cameras/` - Add new camera configuration
- `PUT /cameras/{id}` - Update camera settings
- `DELETE /cameras/{id}` - Remove camera configuration
- `POST /cameras/{id}/tripwires` - Configure detection zones

#### Departments (`/departments`)
- `GET /departments/` - List all departments
- `POST /departments/` - Create new department
- `PUT /departments/{id}` - Update department information
- `DELETE /departments/{id}` - Remove department

#### System Management (`/system`)
- `GET /system/status` - System health and statistics
- `POST /system/start` - Start face tracking system
- `POST /system/stop` - Stop face tracking system
- `GET /system/logs` - System operation logs

#### Streaming (`/stream`)
- `GET /stream/feed/{camera_id}` - Live camera feed with overlays
- `GET /stream/cameras` - Available camera streams
- `POST /stream/test` - Test camera connectivity

## 🔍 Face Recognition System

### Core Technologies
- **InsightFace**: State-of-the-art face recognition models
- **FAISS**: Fast similarity search for face embeddings
- **OpenCV**: Computer vision and image processing
- **ByteTracker**: Multi-object tracking for video streams

### Face Processing Pipeline
1. **Face Detection**: Locate faces in camera frames
2. **Face Alignment**: Normalize face pose and size
3. **Feature Extraction**: Generate face embeddings
4. **Database Matching**: Search against enrolled faces using FAISS
5. **Tracking**: Maintain face identity across frames
6. **Attendance Recording**: Log recognized employees

### Performance Features
- **Multi-GPU Support**: Distribute processing across multiple GPUs
- **Batch Processing**: Process multiple faces simultaneously
- **Real-time Processing**: Low-latency face recognition (< 100ms)
- **Quality Filtering**: Ensure high-quality face captures
- **Confidence Scoring**: Reliability metrics for each recognition

### Starting Face Recognition
```bash
# Automatic start with server
python start_unified_server.py

# Manual start via API
curl -X POST "http://localhost:8000/system/start" \
  -H "Authorization: Bearer <admin_token>"

# Using utility script
python start_face_detection.py start
```

## 📹 Camera Management

### Supported Camera Types
- **USB Webcams**: Direct connection via device ID (0, 1, 2...)
- **IP Cameras**: RTSP and HTTP streams with authentication
- **ONVIF Cameras**: Professional cameras with discovery protocol
- **Network Cameras**: Custom URL configurations

### ONVIF Discovery
Automatic network scanning to discover professional cameras:

```bash
# Discover cameras on network
curl -X POST "http://localhost:8000/cameras/discover" \
  -H "Authorization: Bearer <admin_token>" \
  -H "Content-Type: application/json" \
  -d '{"network_range": "192.168.1.0/24", "timeout": 10}'
```

### Tripwire Configuration
Set up detection zones for accurate attendance tracking:

- **Horizontal Lines**: Detect people crossing doorways
- **Vertical Lines**: Monitor hallway traffic
- **Entry/Exit Zones**: Distinguish between arrivals and departures
- **Multiple Zones**: Complex area monitoring

### Camera Management Workflow
1. **Discovery**: Scan network for available cameras
2. **Configuration**: Set names, locations, and stream settings
3. **Tripwire Setup**: Define detection zones
4. **Activation**: Enable cameras for face tracking
5. **Monitoring**: Real-time status and performance tracking

## 🛠️ Development

### Backend Development
```bash
# Install development dependencies
pip install -r requirements.txt

# Start with auto-reload
python start_unified_server.py --reload

# Run specific module
python -m backend.app.main

# Database migrations
alembic revision --autogenerate -m "Description"
alembic upgrade head

# Run tests
cd backend && pytest tests/

# Code formatting
black backend/
isort backend/
```

### Frontend Development
```bash
# Install dependencies
cd frontend && npm install

# Start development server
npm start

# Build for production
npm run build

# Run tests
npm test

# Lint and format
npm run lint
npm run format

# Type checking
npx tsc --noEmit
```

### Code Style Guidelines
- **Python**: PEP 8 compliance, Black formatting, type hints
- **TypeScript**: ESLint configuration, Prettier formatting
- **Git**: Conventional commit messages
- **Documentation**: Comprehensive docstrings and comments

### Adding New Features
1. **Backend Routes**: Add to `backend/app/routers/`
2. **Database Models**: Update `backend/db/db_models.py`
3. **Frontend Components**: Add to `frontend/src/components/`
4. **API Types**: Update `frontend/src/types/`
5. **Tests**: Add unit and integration tests

## 🔍 Troubleshooting

### Common Issues

#### Database Connection Errors
```bash
# Test connection
python -c "from backend.db.db_config import test_connection; test_connection()"

# Check PostgreSQL status
sudo systemctl status postgresql

# Reset database
python start_unified_server.py --init-db
```

#### Face Recognition Issues
- **Poor Lighting**: Ensure adequate lighting for face detection
- **Camera Quality**: Use cameras with at least 720p resolution
- **Face Enrollment**: Verify faces are properly enrolled with good quality images
- **GPU Memory**: Monitor GPU memory usage for multi-camera setups

#### Camera Connection Problems
```bash
# Test camera access
python -c "import cv2; cap = cv2.VideoCapture(0); print(cap.isOpened())"

# Check camera permissions
sudo usermod -a -G video $USER

# List available cameras
ls /dev/video*
```

#### Import Errors
```bash
# Clear Python cache
find . -name "__pycache__" -type d -exec rm -rf {} +
find . -name "*.pyc" -delete

# Verify imports
python verify_imports.py

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

#### Frontend Issues
```bash
# Clear npm cache
npm cache clean --force

# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install

# Check for port conflicts
lsof -i :3000
```

### System Health Checks
```bash
# Complete system verification
python test_installation.py

# Check all services
curl http://localhost:8000/health
curl http://localhost:3000  # Should serve React app

# Monitor logs
tail -f backend/logs/app.log
```

## 📊 System Monitoring

### Real-time Metrics
- **System Status**: CPU, memory, GPU utilization
- **Camera Performance**: Frame rates, detection accuracy
- **Face Recognition**: Processing speed, match confidence
- **Database Performance**: Query times, connection pool status
- **Network Activity**: Stream bandwidth, API response times

### Logging
- **Application Logs**: `backend/logs/app.log`
- **Access Logs**: HTTP request/response logging
- **Error Tracking**: Detailed error messages and stack traces
- **Performance Metrics**: Processing times and resource usage

### Health Endpoints
- `GET /health` - Basic health check
- `GET /system/status` - Detailed system information
- `GET /system/logs` - Recent log entries

## 🚀 Deployment

### Production Preparation
1. **Environment Configuration**
   ```bash
   # Update .env for production
   DEBUG=false
   ENVIRONMENT=production
   SECRET_KEY=<secure-random-key>
   ```

2. **Database Setup**
   ```bash
   # Create production database
   createdb face_attendance_prod
   
   # Run migrations
   python start_unified_server.py --init-db
   ```

3. **Build Frontend**
   ```bash
   cd frontend
   npm run build
   ```

### Docker Deployment
```dockerfile
# Backend Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY backend/ ./backend/
CMD ["python", "start_unified_server.py"]
```

### Production Server
```bash
# Install Gunicorn
pip install gunicorn

# Start production server
gunicorn -w 4 -k uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000 \
  backend.app.main:app
```

### Performance Optimization
- **Database**: Connection pooling, query optimization
- **Caching**: Redis for session management
- **Load Balancing**: Nginx for multiple server instances
- **CDN**: Static asset delivery optimization
- **GPU**: CUDA optimization for face recognition

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes following the style guidelines
4. Add tests for new functionality
5. Commit with conventional messages: `git commit -m 'feat: add amazing feature'`
6. Push to your branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

### Code Review Process
- All changes require review from maintainers
- Automated tests must pass
- Code coverage should not decrease
- Documentation must be updated for new features

### Bug Reports
When reporting bugs, please include:
- System information (OS, Python version, Node.js version)
- Steps to reproduce the issue
- Expected vs actual behavior
- Error messages and logs
- Camera/hardware specifications if relevant

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **InsightFace** for advanced face recognition models
- **FastAPI** for the high-performance web framework
- **React** for the modern frontend framework
- **OpenCV** for computer vision capabilities
- **FAISS** for efficient similarity search
- **PostgreSQL** for robust data storage
- **Tailwind CSS** for utility-first styling
- **ByteTracker** for object tracking algorithms

## 📞 Support

For questions, issues, or contributions:
- **GitHub Issues**: Report bugs and request features
- **Documentation**: Check `/docs` endpoint for API details
- **Community**: Join discussions on GitHub
- **Email**: Contact maintainers for security issues

---

**Built with ❤️ for modern attendance management and security applications**