# 📹 Enhanced Camera Management System Guide

## 🚀 **New Features Overview**

The Face Recognition System now includes comprehensive camera management capabilities with automatic detection and granular configuration options.

## 🔧 **Key Features**

### **1. Automatic Camera Detection on FTS Startup**
- **When FTS starts**, it automatically scans for all connected cameras
- Detects USB cameras, built-in webcams, and network IP cameras
- Automatically configures detected cameras with default settings
- No manual intervention required for basic setup

### **2. Manual Camera Auto-Detection**
- Super admins can trigger camera detection anytime
- Available in both Super Admin Dashboard and Camera Management
- Comprehensive scanning of all camera types
- Real-time feedback on detection results

### **3. Individual Camera Settings Configuration**
- **Camera Name**: Set custom display names
- **Resolution**: Choose from presets or set custom resolutions
- **Frame Rate (FPS)**: Adjust from 1-120 FPS with preset options
- **Location Description**: Physical location information
- **Active Status**: Enable/disable cameras individually

### **4. Tripwire Configuration**
- Set virtual detection lines for entry/exit monitoring
- Position and spacing adjustments
- Direction-based detection (horizontal/vertical)
- Individual camera tripwire management

## 📋 **How to Use**

### **Automatic Detection on Startup**
```bash
# FTS automatically detects cameras when started
python start_unified_server.py --enable-fts

# Or start FTS only
python start_fts_only.py
```

### **Manual Camera Detection**

#### **Option 1: Super Admin Dashboard**
1. Login as Super Admin
2. Go to **Super Admin Dashboard**
3. Click **"Auto-Detect Cameras"** in Quick Actions
4. Click **"Start Detection"**
5. View results and check Camera Management

#### **Option 2: Camera Management**
1. Go to **Admin** → **Camera Management**
2. Click **"🔍 Auto-Detect Cameras"** button
3. System scans for all available cameras
4. Detected cameras appear in the list

### **Configure Individual Camera Settings**
1. Go to **Admin** → **Camera Management**
2. Find the camera you want to configure
3. Click **"⚙️ Settings"** button
4. Configure the following:

#### **Camera Name**
- Set a descriptive name (e.g., "Main Entrance", "Office Floor 2")
- Used throughout the system for identification

#### **Resolution Settings**
Choose from presets:
- **VGA**: 640 × 480 (4:3)
- **HD 720p**: 1280 × 720 (16:9)
- **Full HD 1080p**: 1920 × 1080 (16:9) ⭐ Recommended
- **QHD 1440p**: 2560 × 1440 (16:9)
- **4K UHD**: 3840 × 2160 (16:9)

Or set **Custom Resolution**:
- Width: 320-4096 pixels
- Height: 240-2160 pixels

#### **Frame Rate (FPS)**
Preset options: 5, 10, 15, 20, 24, 25, 30, 60 FPS
- **Recommended**: 30 FPS for balanced performance
- **High Performance**: 60 FPS (requires more processing power)
- **Power Saving**: 15 FPS for basic monitoring
- **Custom**: 1-120 FPS

#### **Location Description**
- Physical location details
- Helps with camera identification and management

#### **Camera Status**
- **Active**: Camera participates in face detection
- **Inactive**: Camera is disabled and not used

5. Click **"Save Settings"**

### **Tripwire Configuration**
1. In Camera Management, click **"Edit"** on a camera
2. Configure tripwire settings:
   - **Position**: Where the detection line appears (0.0-1.0)
   - **Spacing**: Width of detection zone
   - **Direction**: Horizontal or Vertical
   - **Name**: Descriptive name for the tripwire

## 🎯 **Recommended Settings**

### **For Office Environments**
- **Resolution**: 1920×1080 (Full HD)
- **FPS**: 30
- **Tripwire**: Horizontal at entrance doors

### **For High-Traffic Areas**
- **Resolution**: 1280×720 (HD 720p)
- **FPS**: 30-60
- **Multiple tripwires**: Entry and exit detection

### **For Low-Power Systems**
- **Resolution**: 1280×720 (HD 720p)
- **FPS**: 15-20
- **Single tripwire**: Main detection point

### **For High-Quality Recording**
- **Resolution**: 3840×2160 (4K UHD)
- **FPS**: 30
- **Note**: Requires powerful hardware

## 🔍 **Camera Detection Details**

### **Supported Camera Types**
✅ **USB Cameras**: Webcams, USB security cameras  
✅ **Built-in Cameras**: Laptop webcams, integrated cameras  
✅ **IP Cameras**: Network cameras with ONVIF support  
✅ **RTSP Streams**: Network video streams  

### **Detection Process**
1. **USB/Built-in**: Tests camera indices (0, 1, 2, etc.)
2. **Network**: ONVIF discovery and port scanning
3. **Validation**: Verifies camera functionality
4. **Configuration**: Auto-creates database entries

### **Auto-Configuration**
- **Default Resolution**: 1920×1080
- **Default FPS**: 30
- **Default Tripwire**: Horizontal detection line
- **Status**: Active by default

## 🛠️ **Technical Implementation**

### **Backend Endpoints**
- `POST /cameras/auto-detect` - Trigger auto-detection
- `GET /cameras/detected` - Get detected cameras
- `PUT /cameras/{id}/settings` - Update camera settings
- `GET /cameras/{id}/resolutions` - Get supported resolutions

### **Frontend Components**
- `CameraSettingsModal` - Individual camera configuration
- `CameraSwitcher` - Multi-camera selection (Live Monitor)
- Enhanced Camera Management with auto-detect

### **Database Integration**
- Automatic camera record creation
- Settings persistence across restarts
- Tripwire configuration storage
- Historical settings tracking

## 🔧 **Troubleshooting**

### **Camera Not Detected**
1. **USB Cameras**: Check connection and drivers
2. **Network Cameras**: Verify network connectivity
3. **Permissions**: Ensure camera access permissions
4. **Conflicts**: Close other applications using cameras

### **Poor Performance**
1. **Lower Resolution**: Reduce from 4K to 1080p
2. **Reduce FPS**: Lower from 60 to 30 FPS
3. **Disable Unused Cameras**: Set inactive cameras to inactive
4. **Check Hardware**: Ensure adequate processing power

### **FTS Not Starting**
1. **Auto-Detection Timeout**: May take 30-60 seconds
2. **Camera Conflicts**: Close other camera applications
3. **Database Issues**: Check PostgreSQL connection
4. **Memory**: Ensure sufficient RAM (4GB+ recommended)

## 📊 **System Requirements**

### **Minimum (Single Camera)**
- **RAM**: 4GB
- **CPU**: Dual-core 2.5GHz
- **Resolution**: 720p @ 15 FPS

### **Recommended (Multiple Cameras)**
- **RAM**: 8GB+
- **CPU**: Quad-core 3.0GHz
- **GPU**: Dedicated graphics (optional but recommended)
- **Resolution**: 1080p @ 30 FPS

### **High-Performance (4K, Multiple Cameras)**
- **RAM**: 16GB+
- **CPU**: 8-core 3.5GHz+
- **GPU**: NVIDIA GTX 1060+ or equivalent
- **Resolution**: 4K @ 30-60 FPS

## 🎉 **Benefits**

✅ **Zero-Configuration Setup**: FTS automatically finds and configures cameras  
✅ **Flexible Configuration**: Adjust settings per camera needs  
✅ **Performance Optimization**: Fine-tune for your hardware  
✅ **Easy Management**: Visual interface for all settings  
✅ **Real-time Updates**: Changes apply immediately to running FTS  
✅ **Professional Interface**: Intuitive camera management  

## 🔄 **Integration with FTS**

- **Live Reload**: Settings changes apply to running FTS without restart
- **Performance Monitoring**: Real-time FPS and system stats
- **Error Handling**: Graceful handling of camera failures
- **Multi-Camera Support**: Up to 16+ cameras simultaneously
- **Load Balancing**: Automatic GPU assignment for multiple cameras

This enhanced camera management system provides complete control over your face recognition setup while maintaining ease of use and professional reliability.