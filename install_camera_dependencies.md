# Camera Dependencies Installation Guide

## Dependency Conflict Resolution

The error you're seeing is caused by conflicting package versions. Here's how to resolve it:

## Method 1: Clean Installation (Recommended)

### Step 1: Create a Fresh Environment
```bash
# Create a new virtual environment
python -m venv face_recognition_env
cd face_recognition_env/Scripts  # Windows
# source face_recognition_env/bin/activate  # Linux/Mac
activate  # Windows
```

### Step 2: Install Core Dependencies First
```bash
# Install basic requirements
pip install fastapi uvicorn sqlalchemy requests psutil
pip install python-jose[cryptography] passlib[bcrypt]
```

### Step 3: Install Computer Vision Libraries
```bash
# Install OpenCV first (essential for camera functionality)
pip install opencv-python>=4.8.0

# Install NumPy (required by most CV libraries)
pip install numpy>=1.24.0

# Install Pillow for image processing
pip install Pillow>=10.0.0
```

### Step 4: Install Face Recognition Libraries (One by One)
```bash
# Install ONNX Runtime for model inference
pip install onnxruntime>=1.15.0

# Install FAISS for face embedding search
pip install faiss-cpu>=1.7.4

# Install InsightFace (may take time to download models)
pip install insightface>=0.7.3
```

## Method 2: Resolve Current Environment

### Step 1: Check Conflicting Packages
```bash
pip list | grep -E "(scipy|albumentations|opencv|insightface)"
```

### Step 2: Uninstall Conflicting Packages
```bash
# Remove packages causing conflicts
pip uninstall scipy albumentations -y

# Install compatible versions
pip install scipy>=1.10.0
```

### Step 3: Install Camera Dependencies
```bash
pip install -r requirements_camera.txt
```

## Method 3: Minimal Installation (For Testing)

If you just want to test camera management without face detection:

```bash
# Install only basic camera functionality
pip install opencv-python numpy Pillow requests sqlalchemy fastapi uvicorn
```

This will enable:
- ✅ Camera management interface
- ✅ Camera discovery
- ✅ Basic video streaming
- ❌ Face detection (requires additional libraries)

## Method 4: Alternative Face Recognition Libraries

If InsightFace conflicts persist, try alternatives:

```bash
# Option A: Use face_recognition library instead
pip install face_recognition

# Option B: Use MediaPipe for face detection
pip install mediapipe
```

## Verification Steps

After installation, test the setup:

```bash
# Test Python imports
python -c "import cv2; print('OpenCV:', cv2.__version__)"
python -c "import numpy; print('NumPy:', numpy.__version__)"

# Test face recognition (if installed)
python -c "import insightface; print('InsightFace: OK')"
python -c "import faiss; print('FAISS: OK')"
```

## Common Issues and Solutions

### Issue 1: "Microsoft Visual C++ 14.0 is required"
**Solution (Windows):**
```bash
# Install Microsoft C++ Build Tools
# Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
```

### Issue 2: "No module named 'cv2'"
**Solution:**
```bash
pip uninstall opencv-python opencv-contrib-python opencv-headless
pip install opencv-python
```

### Issue 3: InsightFace model download fails
**Solution:**
```bash
# Set environment variable for model downloads
set INSIGHTFACE_MODEL_PATH=./models  # Windows
export INSIGHTFACE_MODEL_PATH=./models  # Linux/Mac
```

### Issue 4: FAISS installation fails
**Solution:**
```bash
# Try CPU version first
pip install faiss-cpu

# For GPU support (requires CUDA)
pip install faiss-gpu
```

## Testing Installation

Run this test script to verify everything works:

```python
# test_camera_setup.py
try:
    import cv2
    print("✅ OpenCV installed:", cv2.__version__)
except ImportError:
    print("❌ OpenCV not installed")

try:
    import numpy as np
    print("✅ NumPy installed:", np.__version__)
except ImportError:
    print("❌ NumPy not installed")

try:
    import insightface
    print("✅ InsightFace installed")
except ImportError:
    print("❌ InsightFace not installed")

try:
    import faiss
    print("✅ FAISS installed")
except ImportError:
    print("❌ FAISS not installed")

# Test camera access
try:
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        print("✅ Camera access working")
        cap.release()
    else:
        print("⚠️ No camera detected (normal if no USB camera)")
except:
    print("❌ Camera access failed")
```

## Alternative: Docker Installation

For a clean, isolated installation:

```dockerfile
# Dockerfile
FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libgl1-mesa-glx

COPY requirements_camera.txt .
RUN pip install -r requirements_camera.txt

WORKDIR /app
COPY . .
CMD ["python", "start_unified_server.py", "--enable-fts"]
```

Choose the method that works best for your environment!