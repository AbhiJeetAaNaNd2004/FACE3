# Face Recognition Attendance System

A complete, production-ready Face Recognition Attendance System built with FastAPI backend and React frontend. This system provides real-time face recognition for employee attendance tracking with a modern, responsive web interface.

## 🌟 Features

### Backend Features
- **FastAPI-based RESTful API** with automatic documentation
- **Real-time Face Recognition** using OpenCV and face_recognition library
- **JWT Authentication** with role-based access control
- **Database Integration** with SQLAlchemy ORM
- **WebSocket Support** for real-time updates
- **Camera Management** with RTSP/HTTP stream support
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
                        │   Database      │
                        │                 │
                        │ • Users         │
                        │ • Employees     │
                        │ • Attendance    │
                        │ • Cameras       │
                        └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ 
- Node.js 16+
- npm or yarn
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd face-recognition-attendance-system
   ```

2. **Set up the development environment**
   ```bash
   chmod +x setup_dev.sh
   ./setup_dev.sh
   ```

3. **Start the unified server (Backend + Face Tracking)**
   ```bash
   python start_unified_server.py
   ```

4. **Start the frontend development server**
   ```bash
   npm run frontend
   ```

5. **Access the application**
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
│   └── requirements.txt         # Python dependencies
├── frontend/                    # React frontend
│   ├── public/                  # Static assets
│   ├── src/
│   │   ├── components/          # Reusable UI components
│   │   │   ├── ui/              # Base UI components
│   │   │   ├── layout/          # Layout components
│   │   │   └── camera/          # Camera-specific components
│   │   ├── pages/               # Page components
│   │   │   ├── login/           # Login page
│   │   │   ├── super-admin/     # Super admin pages
│   │   │   ├── admin/           # Admin pages
│   │   │   └── employee/        # Employee pages
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

## 📊 Key Features Deep Dive

### Face Recognition System
- **Real-time Processing**: Processes camera feeds in real-time
- **High Accuracy**: Uses state-of-the-art face recognition algorithms
- **Confidence Scoring**: Provides confidence levels for each recognition
- **Multiple Cameras**: Supports multiple camera streams simultaneously
- **Auto-enrollment**: Easy face enrollment process with image upload

### Dashboard Analytics
- **Live Statistics**: Real-time employee count and attendance rates
- **Historical Data**: Comprehensive attendance history and analytics
- **Visual Insights**: Charts and graphs for attendance patterns
- **Export Capabilities**: Export attendance data for reporting

### Real-time Features
- **WebSocket Integration**: Live updates without page refresh
- **Activity Feed**: Real-time stream of recognition events
- **Camera Monitoring**: Live camera feeds with face detection overlays
- **Status Indicators**: Real-time system and camera status

### Security
- **JWT Authentication**: Secure token-based authentication
- **Role-based Access**: Granular permissions based on user roles
- **Password Hashing**: Secure password storage with bcrypt
- **API Security**: Protected endpoints with proper authorization

## 🔧 Configuration

### Environment Variables

Create `.env` files in both backend and frontend directories:

**Backend (.env)**
```env
DATABASE_URL=sqlite:///./attendance.db
SECRET_KEY=your-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=30
FACE_TRACKING_AUTO_START=true
FRONTEND_URL=http://localhost:3000
```

**Frontend (.env)**
```env
REACT_APP_API_URL=http://localhost:8000
```

### Camera Configuration
- Supports RTSP, HTTP, and USB cameras
- Configure camera streams in the Camera Management section
- Auto-discovery feature for network cameras
- Customizable detection zones and sensitivity

### Database Configuration
- Default: SQLite for development
- Production: PostgreSQL/MySQL support available
- Automatic database initialization with sample data
- Migration support for schema updates

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
   - Configure production database
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

## 📚 API Documentation

The API documentation is automatically generated and available at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Key Endpoints

- `POST /auth/login` - User authentication
- `GET /auth/me` - Get current user info
- `GET /employees/` - List all employees
- `POST /employees/enroll` - Enroll new employee
- `GET /attendance/all` - Get all attendance records
- `GET /cameras/` - List all cameras
- `POST /cameras/` - Add new camera
- `GET /system/status` - Get system status

## 🔍 Troubleshooting

### Common Issues

1. **Camera not detected**
   - Check camera permissions
   - Verify stream URL format
   - Test camera connectivity

2. **Face recognition not working**
   - Ensure good lighting conditions
   - Check if face images are properly enrolled
   - Verify camera positioning

3. **Database connection errors**
   - Check database URL in environment variables
   - Ensure database server is running
   - Verify database permissions

4. **Frontend build errors**
   - Clear npm cache: `npm cache clean --force`
   - Delete node_modules and reinstall
   - Check Node.js version compatibility

### Performance Optimization

- **Database**: Use connection pooling for production
- **Camera Processing**: Adjust frame rate and resolution
- **Frontend**: Enable production build optimizations
- **Caching**: Implement Redis for session management

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

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenCV** for computer vision capabilities
- **FastAPI** for the high-performance backend framework
- **React** for the modern frontend framework
- **Tailwind CSS** for the utility-first CSS framework
- **face_recognition** library for facial recognition algorithms

## 📞 Support

For questions, issues, or contributions:
- Create an issue on GitHub
- Check the documentation at `/docs`
- Review the troubleshooting section above

---

**Built with ❤️ for modern attendance management**