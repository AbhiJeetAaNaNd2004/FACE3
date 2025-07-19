# Face Recognition Attendance System

A comprehensive, production-ready face recognition attendance system with a FastAPI backend and React frontend. This system provides real-time face detection, tracking, and attendance management with role-based access control.

## 🚀 Features

### Backend Features
- **Unified Server Architecture**: Face tracking system integrated as a background service within FastAPI
- **Role-Based Authentication**: Super Admin, Admin, and Employee access levels
- **Real-Time Face Recognition**: Advanced face detection and tracking using InsightFace
- **Camera Management**: Multi-camera support with tripwire configuration
- **Attendance Tracking**: Automated attendance logging with confidence scoring
- **RESTful API**: Comprehensive API with automatic documentation
- **Database Integration**: PostgreSQL with SQLAlchemy ORM

### Frontend Features
- **Modern React Interface**: TypeScript-based with Tailwind CSS styling
- **Role-Based Dashboards**: Customized interfaces for each user role
- **Real-Time System Control**: Start/stop face recognition system
- **Live Camera Feeds**: Monitor camera streams with annotations
- **Employee Management**: Complete CRUD operations for employee data
- **Attendance Dashboard**: View and manage attendance records
- **Responsive Design**: Mobile-friendly interface

## 📋 System Requirements

### Backend Requirements
- Python 3.8+
- PostgreSQL 12+
- CUDA-compatible GPU (recommended for face recognition)
- Cameras with RTSP/HTTP streams

### Frontend Requirements
- Node.js 16+
- npm or yarn package manager

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd face-recognition-attendance-system
```

### 2. Backend Setup

#### Install Python Dependencies
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Database Setup
1. Install PostgreSQL and create a database:
```sql
CREATE DATABASE face_tracking;
CREATE USER face_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE face_tracking TO face_user;
```

2. Create environment configuration:
```bash
# Create .env file in backend directory
cd backend
cp .env.example .env
```

3. Update `.env` with your database credentials:
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=face_tracking
DB_USER=face_user
DB_PASSWORD=your_password
SECRET_KEY=your-secret-key-here
```

#### Initialize Database
```bash
# Initialize database tables and sample data
python start_unified_server.py --init-db
```

### 3. Frontend Setup

#### Install Node.js Dependencies
```bash
cd frontend
npm install
```

#### Environment Configuration
Create a `.env` file in the frontend directory:
```env
REACT_APP_API_URL=http://localhost:8000
```

## 🚀 Running the Application

### Option 1: Unified Server (Recommended)
Run both backend and face recognition system together:

```bash
# From project root
python start_unified_server.py

# For development with auto-reload
python start_unified_server.py --reload

# To disable face tracking auto-start
python start_unified_server.py --no-fts
```

### Option 2: Separate Components (Legacy)
If you prefer to run components separately:

```bash
# Terminal 1: Backend API
cd backend
python -m uvicorn app.main:app --reload

# Terminal 2: Face Recognition System
python start_face_detection.py start
```

### Frontend Development Server
```bash
cd frontend
npm start
```

The application will be available at:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 👥 Default User Accounts

The system initializes with the following default accounts:

| Username | Password | Role | Description |
|----------|----------|------|-------------|
| `superadmin` | `admin123` | Super Admin | Full system access |
| `admin` | `admin123` | Admin | Employee and attendance management |
| `employee` | `employee123` | Employee | Personal attendance view |

**⚠️ Important**: Change these default passwords in production!

## 🏗️ System Architecture

### Backend Architecture
```
FastAPI Application
├── Face Tracking System (Background Service)
├── Authentication & Authorization
├── Employee Management
├── Camera Management
├── Attendance Tracking
└── System Control
```

### Frontend Architecture
```
React Application
├── Authentication (Zustand Store)
├── Role-Based Routing
├── Dashboard Layouts
├── Component Library (Tailwind + Custom)
└── API Service Layer (Axios)
```

## 📱 User Interface Overview

### Super Admin Dashboard
- **System Control**: Start/stop face recognition system
- **User Management**: Create and manage user accounts
- **Camera Management**: Configure cameras and tripwires
- **System Monitoring**: View logs and system status
- **Access to All Features**: Can access admin and employee features

### Admin Dashboard
- **Employee Management**: Enroll and manage employees
- **Attendance Dashboard**: Monitor all attendance records
- **Live Camera Feed**: View real-time camera streams
- **Present Employees**: See currently present staff

### Employee Dashboard
- **Personal Attendance**: View own attendance history
- **Current Status**: See current attendance status
- **Profile Information**: Basic profile details

## 🔧 Configuration

### Camera Configuration
Cameras can be configured through the API or database. Each camera supports:
- **Stream URL**: RTSP or HTTP stream endpoint
- **Camera Type**: Entry, exit, or monitoring
- **Tripwires**: Detection zones for attendance tracking
- **Resolution & FPS**: Stream quality settings

### Face Recognition Settings
Configure face recognition parameters in the backend:
- **Detection Threshold**: Minimum confidence for face detection
- **Recognition Threshold**: Minimum confidence for face recognition
- **Tracking Parameters**: Object tracking settings
- **Quality Metrics**: Face quality assessment

## 🔒 Security Features

- **JWT Authentication**: Secure token-based authentication
- **Role-Based Access Control**: Hierarchical permission system
- **Password Hashing**: Secure password storage with bcrypt
- **CORS Protection**: Configurable cross-origin request handling
- **Input Validation**: Comprehensive request validation

## 📊 API Documentation

The system provides comprehensive API documentation available at `/docs` when the server is running. Key API endpoints include:

### Authentication
- `POST /auth/login` - User login
- `GET /auth/me` - Get current user info
- `POST /auth/users/create` - Create new user (Super Admin only)

### Employee Management
- `GET /employees/` - List all employees
- `POST /employees/enroll` - Enroll new employee with face data
- `PUT /employees/{id}` - Update employee information

### System Control
- `POST /system/start` - Start face recognition system
- `POST /system/stop` - Stop face recognition system
- `GET /system/status` - Get system status

### Camera Management
- `GET /cameras/` - List all cameras
- `POST /cameras/` - Add new camera
- `POST /cameras/discover` - Auto-discover network cameras

## 🧪 Testing

### Backend Testing
```bash
cd backend
pytest
```

### Frontend Testing
```bash
cd frontend
npm test
```

## 📦 Production Deployment

### Backend Deployment
1. Set up production database
2. Configure environment variables
3. Use production WSGI server (e.g., Gunicorn)
4. Set up reverse proxy (e.g., Nginx)
5. Configure SSL certificates

### Frontend Deployment
```bash
cd frontend
npm run build
```
Deploy the `build` folder to your web server or CDN.

## 🔧 Troubleshooting

### Common Issues

#### Face Recognition Not Starting
- Check camera connections and stream URLs
- Verify CUDA installation for GPU acceleration
- Check database connectivity
- Review system logs at `/system/logs`

#### Authentication Issues
- Verify JWT secret key configuration
- Check token expiration settings
- Ensure proper CORS configuration

#### Database Connection Issues
- Verify PostgreSQL service is running
- Check database credentials in `.env`
- Ensure database and user exist

### Performance Optimization
- Use GPU acceleration for face recognition
- Optimize camera stream resolution and FPS
- Configure database connection pooling
- Use Redis for session storage (optional)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 🆘 Support

For support and questions:
1. Check the troubleshooting section
2. Review API documentation at `/docs`
3. Create an issue on the repository
4. Check system logs for detailed error information

---

**Note**: This system is designed for professional use and includes advanced face recognition capabilities. Ensure compliance with local privacy laws and regulations when deploying in production environments.