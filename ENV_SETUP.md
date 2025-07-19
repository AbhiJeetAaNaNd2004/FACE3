# Environment Configuration Setup Guide

## 🎯 Overview

The Face Recognition Attendance System uses multiple `.env` files for configuration:

- **`.env`** - Root configuration (shared settings)
- **`backend/.env`** - Backend-specific settings
- **`frontend/.env`** - Frontend React app settings

## 🚀 Quick Setup

### 1. Copy Template Files
```bash
# Copy all template files
cp .env.example .env
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

### 2. Configure Database
```bash
# Edit root configuration
nano .env

# Edit backend configuration  
nano backend/.env
```

### 3. Verify Configuration
```bash
# Check all environment settings
npm run check:env
```

## 📋 Configuration Files

### Root .env File
Contains shared configuration for the entire system:

```env
# Database Configuration - PostgreSQL
DB_TYPE=postgresql
DB_HOST=localhost
DB_PORT=5432
DB_NAME=face_attendance_db
DB_USER=postgres
DB_PASSWORD=your_secure_password_here

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
FTS_STARTUP_DELAY=2
FACE_TRACKING_AUTO_START=true

# Logging Configuration
LOG_ROTATION=1 day
LOG_RETENTION=30 days
```

### Backend .env File
Backend-specific configuration:

```env
# Database Configuration - PostgreSQL
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
ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000,http://localhost:5173,http://127.0.0.1:5173

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

# Logging Configuration
LOG_FILE=logs/app.log
LOG_ROTATION=1 day
LOG_RETENTION=30 days

# Face Tracking System Configuration
FTS_AUTO_START=true
FTS_STARTUP_DELAY=2
FACE_TRACKING_AUTO_START=true
```

### Frontend .env File
React app configuration:

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

## 🗄️ Database Setup (PostgreSQL)

### 1. Install PostgreSQL
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install postgresql postgresql-contrib

# Start PostgreSQL service
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

### 2. Configure PostgreSQL
```bash
# Switch to postgres user
sudo -u postgres psql

# Create database and user
CREATE DATABASE face_attendance_db;
CREATE USER postgres WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE face_attendance_db TO postgres;
\q
```

### 3. Automated Setup
```bash
# Use our automated setup script
npm run setup:postgresql
```

## 🔧 Configuration Options

### Security Settings
- **SECRET_KEY**: JWT signing key (change in production!)
- **ALGORITHM**: JWT algorithm (HS256 recommended)
- **ACCESS_TOKEN_EXPIRE_MINUTES**: Token expiration time

### Face Recognition Settings
- **FACE_RECOGNITION_TOLERANCE**: Recognition sensitivity (0.4-0.8)
- **FACE_DETECTION_MODEL**: Detection algorithm (hog/cnn)
- **FACE_ENCODING_MODEL**: Encoding quality (small/large)

### Camera Settings
- **DEFAULT_CAMERA_ID**: Default camera index (0 for built-in)
- **MAX_CONCURRENT_STREAMS**: Maximum simultaneous camera streams
- **STREAM_QUALITY**: Video quality (low/medium/high)

### File Storage
- **UPLOAD_DIR**: Directory for file uploads
- **FACE_IMAGES_DIR**: Directory for face images
- **MAX_FILE_SIZE**: Maximum upload file size in bytes

## 🔍 Validation & Testing

### Check Configuration
```bash
# Validate all .env files
npm run check:env

# Test database connection
npm run setup:postgresql

# Check server startup
npm run start --dry-run
```

### Common Issues

#### Database Connection Errors
```bash
# Check PostgreSQL status
sudo systemctl status postgresql

# Test connection manually
psql -h localhost -U postgres -d face_attendance_db
```

#### Port Conflicts
```bash
# Check what's using port 8000
npm run cleanup:port

# Use different port
REACT_APP_API_URL=http://localhost:8001 npm start
```

#### Environment Variable Not Loading
```bash
# Check file exists and has correct permissions
ls -la .env backend/.env frontend/.env

# Verify content
npm run check:env
```

## 📝 Production Considerations

### Security
- [ ] Change SECRET_KEY to a strong, unique value
- [ ] Use environment-specific database credentials
- [ ] Set DEBUG=false
- [ ] Configure proper CORS origins
- [ ] Use HTTPS URLs in production

### Performance
- [ ] Set appropriate FACE_RECOGNITION_TOLERANCE
- [ ] Configure MAX_CONCURRENT_STREAMS based on hardware
- [ ] Set LOG_LEVEL=WARNING or ERROR in production
- [ ] Enable GENERATE_SOURCEMAP=false for frontend

### Database
- [ ] Use separate database for production
- [ ] Configure database connection pooling
- [ ] Set up database backups
- [ ] Monitor database performance

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'dotenv'` | Install python3-dotenv: `sudo apt install python3-dotenv` |
| Database connection failed | Check PostgreSQL service and credentials |
| Port 8000 already in use | Run `npm run cleanup:port` or use different port |
| Frontend can't connect to API | Check REACT_APP_API_URL in frontend/.env |
| Face recognition not working | Verify camera permissions and face recognition settings |

## 📚 Reference

### Required Environment Variables
- ✅ DB_HOST, DB_NAME, DB_USER, DB_PASSWORD
- ✅ SECRET_KEY
- ✅ REACT_APP_API_URL

### Optional Environment Variables
- FACE_RECOGNITION_TOLERANCE (default: 0.6)
- MAX_CONCURRENT_STREAMS (default: 5)
- LOG_LEVEL (default: INFO)
- DEFAULT_CAMERA_ID (default: 0)

### Useful Commands
```bash
npm run check:env          # Validate configuration
npm run setup:postgresql   # Setup PostgreSQL database
npm run start:force        # Start with port cleanup
npm run cleanup:port       # Clean up port conflicts
```