# Port Conflict Fix Guide

## 🚨 Problem
The error `[Errno 10048] error while attempting to bind on address ('0.0.0.0', 8000): only one usage of each socket address (protocol/network address/port) is normally permitted` occurs when:

1. Another process is already using port 8000
2. A previous server instance didn't shut down properly
3. Another application (like another web server) is bound to port 8000

## ✅ Solutions (Multiple Options)

### Option 1: Automatic Fix (Recommended)
```bash
# Force kill any process on port 8000 and start server
npm run start:force
```

### Option 2: Manual Port Cleanup
```bash
# Clean up port 8000 first, then start normally
npm run cleanup:port
npm start
```

### Option 3: Use Cleanup Scripts
```bash
# Linux/Mac:
./fix_port_conflict.sh

# Windows:
fix_port_conflict.bat
```

### Option 4: Use Different Port
```bash
# Start server on a different port (e.g., 8001)
python3 start_unified_server.py --port 8001
```

### Option 5: Manual Process Termination

#### Windows:
```cmd
# Find process using port 8000
netstat -ano | findstr :8000

# Kill the process (replace <PID> with actual process ID)
taskkill /f /pid <PID>
```

#### Linux/Mac:
```bash
# Find and kill process using port 8000
lsof -ti:8000 | xargs kill -9
```

## 🔧 What Was Fixed

### Enhanced Server Startup (`start_unified_server.py`)
- ✅ Automatic port conflict detection
- ✅ Automatic process termination on conflicting ports
- ✅ Alternative port finding if cleanup fails
- ✅ `--force` flag for aggressive cleanup
- ✅ Better error messages and user guidance

### New Tools Created
1. **`cleanup_port.py`** - Standalone port cleanup utility
2. **`fix_port_conflict.sh`** - Linux/Mac fix script
3. **`fix_port_conflict.bat`** - Windows fix script

### Enhanced Package.json Scripts
- ✅ `npm run start:force` - Force start with port cleanup
- ✅ `npm run cleanup:port` - Clean port 8000 only

### Updated Documentation
- ✅ Added troubleshooting section in README.md
- ✅ Multiple solution approaches documented

## 🎯 Prevention Tips

1. **Always use Ctrl+C to stop the server** instead of closing the terminal window
2. **Use the `--force` flag** when you know port conflicts might occur
3. **Check running processes** before starting the server if issues persist
4. **Use different ports** for multiple instances (development vs production)

## 🔍 Testing the Fix

```bash
# Test port availability
python3 cleanup_port.py 8000

# Test server startup with force cleanup
python3 start_unified_server.py --force

# Test alternative port
python3 start_unified_server.py --port 8001
```

## 📝 Command Reference

| Command | Description |
|---------|-------------|
| `npm start` | Normal server start |
| `npm run start:force` | Start with automatic port cleanup |
| `npm run cleanup:port` | Clean port 8000 only |
| `python3 start_unified_server.py --help` | Show all options |
| `python3 cleanup_port.py 8000` | Check/clean specific port |
| `./fix_port_conflict.sh` | Run automated fix script (Linux/Mac) |

The fix ensures that your Face Recognition Attendance System can start reliably without manual intervention for port conflicts!