# Face Recognition Attendance System

A complete, production-ready Face Recognition Attendance System built with FastAPI backend and React frontend. This system provides real-time face recognition for employee attendance tracking with a modern, responsive web interface.

## 📋 Table of Contents

- [Features](#-features)
- [System Architecture](#️-system-architecture)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [User Roles & Permissions](#-user-roles--permissions)
- [Camera Management](#-camera-management)
- [Face Detection System](#-face-detection-system)
- [Configuration](#-configuration)
- [Development](#️-development)
- [API Documentation](#-api-documentation)
- [Troubleshooting](#-troubleshooting)
- [System Status](#-system-status)
- [Deployment](#-deployment)
- [Contributing](#-contributing)

## 🌟 Features

### Backend Features
- **FastAPI-based RESTful API** with automatic documentation
- **Real-time Face Recognition** using OpenCV and face_recognition library
- **JWT Authentication** with role-based access control
- **PostgreSQL Database** with SQLAlchemy ORM
- **WebSocket Support** for real-time updates
- **Camera Management** with ONVIF discovery and RTSP/HTTP stream support
- **Employee Enrollment** with face image processing
- **Attendance Tracking** with confidence scoring
- **User Management** with multiple role levels
- **Unified Server Architecture** with background face tracking

### Frontend Features
- **Modern React UI** with TypeScript
- **Tailwind CSS** styling with responsive design
- **Role-based Dashboard** (Super Admin, Admin, Employee)
- **Real-time Camera Feeds** with live face detection
- **Employee Management** with face enrollment
- **Attendance Monitoring** with detailed analytics
- **User Management** for administrators
- **Live Activity Feed** with WebSocket integration
- **File Upload** with drag-and-drop support
- **Data Tables** with sorting, filtering, and search

## 🏗️ System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React Frontend │    │  FastAPI Backend │    │   Face Tracking │
│                 │    │                 │    │     System      │
│ • Authentication│◄──►│ • REST API      │◄──►│ • OpenCV        │
│ • Dashboards    │    │ • WebSocket     │    │ • Face Detection│
│ • Real-time UI  │    │ • Database      │    │ • Recognition   │
│ • File Upload   │    │ • JWT Auth      │    │ • Camera Stream │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                        ┌─────────────────┐
                        │ PostgreSQL DB   │
                        │                 │
                        │ • Users         │
                        │ • Employees     │
                        │ • Attendance    │
                        │ • Cameras       │
                        │ • Face Data     │
                        └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ 
- Node.js 16+
- PostgreSQL 12+
- npm or yarn
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd face-recognition-attendance-system
   ```

2. **Set up PostgreSQL Database**
   ```bash
   # Create database
   createdb face_attendance_db
   
   # Update .env file with your database credentials
   ```

3. **Configure Environment Variables**
   ```bash
   # Copy and edit environment file
   cp .env.example .env
   
   # Edit .env with your database credentials:
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=face_attendance_db
   DB_USER=postgres
   DB_PASSWORD=your_password
   SECRET_KEY=your-secret-key-here
   ```

4. **Set up the development environment**
   ```bash
   chmod +x setup_dev.sh
   ./setup_dev.sh
   ```

5. **Initialize the database**
   ```bash
   python backend/init_db.py
   ```

6. **Start the unified server (Backend + Face Tracking)**
   ```bash
   python start_unified_server.py
   ```

7. **Start the frontend development server**
   ```bash
   npm run frontend
   ```

8. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Default Login Credentials
- **Super Admin**: `admin` / `admin123`
- **Admin**: `manager` / `manager123`  
- **Employee**: `employee` / `employee123`

## 📁 Project Structure

```
face-recognition-attendance-system/
├── backend/                     # FastAPI backend
│   ├── app/
│   │   ├── api/                 # API routes
│   │   ├── core/                # Core configurations
│   │   ├── db/                  # Database models and setup
│   │   ├── services/            # Business logic
│   │   └── main.py              # FastAPI application
│   ├── face_recognition_system/ # Face tracking system
│   │   ├── camera_manager.py    # Camera management
│   │   ├── face_detector.py     # Face detection logic
│   │   ├── face_tracker.py      # Main tracking system
│   │   └── models/              # ML models
│   ├── utils/                   # Utility modules
│   │   ├── camera_discovery.py  # ONVIF camera discovery
│   │   └── camera_config_loader.py # Configuration loader
│   └── requirements.txt         # Python dependencies
├── frontend/                    # React frontend
│   ├── public/                  # Static assets
│   ├── src/
│   │   ├── components/          # Reusable UI components
│   │   ├── pages/               # Page components
│   │   ├── store/               # Zustand state management
│   │   ├── services/            # API service layer
│   │   ├── hooks/               # Custom React hooks
│   │   ├── types/               # TypeScript definitions
│   │   └── utils/               # Utility functions
│   ├── package.json             # Node.js dependencies
│   └── tailwind.config.js       # Tailwind CSS configuration
├── start_unified_server.py      # Unified server startup script
├── setup_dev.sh                 # Development setup script
├── package.json                 # Root package.json with scripts
└── README.md                    # This file
```

## 🎯 User Roles & Permissions

### Super Admin
- **Full system access**
- User management (create, edit, delete users)
- Employee management with face enrollment
- Camera management and configuration
- Live monitoring with multiple camera feeds
- System control (start/stop face tracking)
- Attendance analytics and reporting

### Admin
- **Administrative access**
- Employee management with face enrollment
- Camera management and configuration
- Live monitoring with camera feeds
- Attendance tracking and analytics
- Cannot manage users or system settings

### Employee
- **Limited access**
- Personal dashboard with attendance history
- View current attendance status
- See colleagues currently present
- Personal information management

## 📹 Camera Management

The system features advanced camera management with automated discovery and configuration:

### ONVIF Camera Discovery
- **Automated Network Scanning**: Discovers ONVIF-compliant cameras automatically
- **Port Scanning Fallback**: Detects non-ONVIF cameras on the network
- **Manufacturer Detection**: Identifies camera brands and models
- **Stream URL Discovery**: Automatically finds RTSP/HTTP stream endpoints

### Camera Configuration Workflow

1. **Discovery**: Admin triggers network scan to find available cameras
2. **Configuration**: Select cameras and configure names, locations, and tripwires
3. **Activation**: Activate cameras for the face tracking system
4. **Monitoring**: Real-time monitoring and management

### Camera Management API Endpoints

- `POST /cameras/discover` - Network camera discovery
- `GET /cameras/` - List all cameras with filtering
- `POST /cameras/` - Create new camera configuration
- `PUT /cameras/{camera_id}` - Update camera configuration
- `POST /cameras/{camera_id}/configure` - Configure with tripwires
- `POST /cameras/{camera_id}/activate` - Activate/deactivate camera
- `DELETE /cameras/{camera_id}` - Delete camera configuration

### Tripwire Management

Configure detection zones for accurate face tracking:
- **Position-based Detection**: Set horizontal/vertical detection lines
- **Entry/Exit Detection**: Configure direction-based tracking
- **Customizable Spacing**: Adjust detection sensitivity
- **Zone Management**: Multiple detection zones per camera

## 🔍 Face Detection System

### Starting the Face Detection System

The Face Detection System (FTS) can be started in multiple ways:

#### Method 1: Using the Unified Server (Recommended)
```bash
python start_unified_server.py
```

#### Method 2: Using the Web API
1. Start the FastAPI server
2. Authenticate with admin credentials
3. Use the `POST /system/start` endpoint

#### Method 3: Using the Startup Script
```bash
# Update credentials in start_face_detection.py first
python start_face_detection.py start
```

### System Management Endpoints

- `POST /system/start` - Start the face detection system
- `POST /system/stop` - Stop the face detection system
- `GET /system/status` - Get system status and statistics
- `GET /system/live-faces` - Get currently detected faces
- `GET /system/attendance-data` - Get recent attendance records

### Face Recognition Features

- **Real-time Processing**: Processes camera feeds in real-time
- **High Accuracy**: Uses state-of-the-art face recognition algorithms
- **Confidence Scoring**: Provides confidence levels for each recognition
- **Multiple Cameras**: Supports multiple camera streams simultaneously
- **Auto-enrollment**: Easy face enrollment process with image upload

## 🔧 Configuration

### Environment Variables

**Backend (.env)**
```env
# Database Configuration - PostgreSQL Only
DB_HOST=localhost
DB_PORT=5432
DB_NAME=face_attendance_db
DB_USER=postgres
DB_PASSWORD=your_password

# Security Configuration
SECRET_KEY=your-secret-key-change-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Face Tracking System Configuration
FACE_TRACKING_AUTO_START=true
FRONTEND_URL=http://localhost:3000
```

**Frontend (.env)**
```env
REACT_APP_API_URL=http://localhost:8000
```

### Database Configuration

The system uses PostgreSQL as the single source of truth for all configurations:

- **Cameras**: All camera configurations stored in `camera_configs` table
- **Tripwires**: Detection zones stored in `tripwires` table with relationships
- **Employees**: Employee data and face embeddings
- **Attendance**: Comprehensive attendance tracking
- **Users**: User accounts with role-based permissions

## 🛠️ Development

### Backend Development
```bash
# Install dependencies
pip install -r backend/requirements.txt

# Run development server with auto-reload
python start_unified_server.py --reload

# Run tests
pytest backend/tests/

# Format code
black backend/
```

### Frontend Development
```bash
# Install dependencies
npm install

# Start development server
npm start

# Run tests
npm test

# Lint code
npm run lint

# Format code
npm run format
```

### Adding New Features

1. **Backend**: Add routes in `backend/app/api/`
2. **Frontend**: Add components in `frontend/src/components/`
3. **Database**: Add models in `backend/app/db/models/`
4. **Types**: Update TypeScript types in `frontend/src/types/`

### Import Structure

The project follows a consistent import pattern:
- **From application modules**: Use absolute imports
- **From database modules**: Use relative imports within db package
- **Between packages**: Use absolute imports from backend root

## 📚 API Documentation

The API documentation is automatically generated and available at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Key Endpoints

#### Authentication
- `POST /auth/login` - User authentication
- `POST /auth/logout` - User logout
- `GET /auth/me` - Get current user info

#### Employee Management
- `GET /employees/` - List all employees
- `POST /employees/enroll` - Enroll new employee
- `PUT /employees/{employee_id}` - Update employee

#### Attendance
- `GET /attendance/all` - Get all attendance records
- `POST /attendance/manual` - Manual attendance entry

#### System Management
- `GET /system/status` - Get system status
- `POST /system/start` - Start face tracking
- `POST /system/stop` - Stop face tracking

## 🔍 Troubleshooting

### Common Issues

#### 1. Database Connection Errors
```bash
# Test database connection
python -c "from backend.db.db_config import test_connection; test_connection()"

# Check PostgreSQL service
sudo systemctl status postgresql
```

#### 2. Camera Detection Issues
- **Check camera permissions**: Ensure system has access to cameras
- **Verify stream URLs**: Test RTSP/HTTP streams manually
- **Network connectivity**: Ensure cameras are reachable on network
- **ONVIF support**: Some cameras may need ONVIF enabled

#### 3. Face Recognition Not Working
- **Lighting conditions**: Ensure adequate lighting for face detection
- **Camera positioning**: Position cameras at appropriate angles
- **Face enrollment**: Verify employee faces are properly enrolled
- **Model loading**: Check if face recognition models are loaded correctly

#### 4. Import Errors
```bash
# Clear Python cache
find . -name "__pycache__" -type d -exec rm -rf {} +
find . -name "*.pyc" -delete

# Verify imports
python verify_imports.py
```

#### 5. Frontend Build Errors
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

### System Status Verification

Check system health:
```bash
# Database connectivity
python backend/test_installation.py

# All imports working
python verify_imports.py

# System status via API
curl http://localhost:8000/health
```

## 📊 System Status

### Current System Health

✅ **Backend**: FastAPI server running on port 8000  
✅ **Frontend**: React development server on port 3000  
✅ **Database**: PostgreSQL with all tables created  
✅ **Authentication**: JWT-based auth with role management  
✅ **Face Tracking**: Real-time processing available  
✅ **Camera Management**: ONVIF discovery and configuration  
✅ **API Documentation**: Available at `/docs` endpoint  

### Database Tables
- `employees` - Employee information and face data
- `camera_configs` - Camera configurations and settings
- `tripwires` - Detection zone definitions
- `attendance_logs` - Attendance records with timestamps
- `user_accounts` - User authentication and roles
- `face_embeddings` - Face recognition data
- `system_logs` - System operation logs

### Security Features
- JWT token-based authentication
- Role-based access control
- Password hashing with bcrypt
- Secure token generation
- API endpoint protection

## 🚀 Deployment

### Production Build

1. **Build Frontend**
   ```bash
   npm run build
   ```

2. **Backend Production Setup**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -k uvicorn.workers.UvicornWorker backend.app.main:app
   ```

3. **Environment Setup**
   - Configure production PostgreSQL database
   - Set secure SECRET_KEY
   - Configure CORS settings
   - Set up SSL certificates

### Docker Deployment (Optional)

```dockerfile
# Example Dockerfile for backend
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "start_unified_server.py"]
```

### Performance Optimization

- **Database**: Use connection pooling for production
- **Camera Processing**: Adjust frame rate and resolution
- **Frontend**: Enable production build optimizations
- **Caching**: Implement Redis for session management
- **Load Balancing**: Use nginx for production deployments

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow TypeScript/Python type hints
- Write tests for new features
- Update documentation for API changes
- Follow existing code style and conventions
- Test camera integration thoroughly

### Code Style
- **Python**: Follow PEP 8, use Black for formatting
- **TypeScript**: Follow project ESLint configuration
- **Git**: Use conventional commit messages
- **Documentation**: Update README for new features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenCV** for computer vision capabilities
- **FastAPI** for the high-performance backend framework
- **React** for the modern frontend framework
- **Tailwind CSS** for the utility-first CSS framework
- **face_recognition** library for facial recognition algorithms
- **ONVIF** for camera discovery protocols
- **PostgreSQL** for robust data persistence

## 📞 Support

For questions, issues, or contributions:
- Create an issue on GitHub
- Check the documentation at `/docs`
- Review the troubleshooting section above
- Test import structure with `verify_imports.py`

## 🔄 Recent Updates

### System Fixes Completed
- ✅ **Database Configuration**: Removed SQLite, PostgreSQL only
- ✅ **Authentication**: Added logout functionality
- ✅ **Camera Detection**: Real camera streaming with ONVIF discovery
- ✅ **Import Structure**: Fixed all import inconsistencies
- ✅ **Face Tracking**: Integrated with database configurations
- ✅ **Security**: Enhanced JWT authentication and role management

### Migration Support
- Camera configurations migrated from hardcoded to database
- Automatic discovery and configuration workflows
- Hot-reload capability for configuration changes
- Backward compatibility maintained

---

**Built with ❤️ for modern attendance management**