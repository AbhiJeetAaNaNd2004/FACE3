#!/usr/bin/env python3
"""
Test script to verify camera detection dependencies
Run this to check what's installed and working
"""

def test_imports():
    """Test importing all required packages"""
    results = {}
    
    # Test OpenCV
    try:
        import cv2
        results['opencv'] = {'status': '✅ INSTALLED', 'version': cv2.__version__}
    except ImportError as e:
        results['opencv'] = {'status': '❌ NOT INSTALLED', 'error': str(e)}
    
    # Test NumPy
    try:
        import numpy as np
        results['numpy'] = {'status': '✅ INSTALLED', 'version': np.__version__}
    except ImportError as e:
        results['numpy'] = {'status': '❌ NOT INSTALLED', 'error': str(e)}
    
    # Test Pillow
    try:
        import PIL
        results['pillow'] = {'status': '✅ INSTALLED', 'version': PIL.__version__}
    except ImportError as e:
        results['pillow'] = {'status': '❌ NOT INSTALLED', 'error': str(e)}
    
    # Test InsightFace
    try:
        import insightface
        results['insightface'] = {'status': '✅ INSTALLED', 'version': 'OK'}
    except ImportError as e:
        results['insightface'] = {'status': '❌ NOT INSTALLED', 'error': str(e)}
    
    # Test FAISS
    try:
        import faiss
        results['faiss'] = {'status': '✅ INSTALLED', 'version': 'OK'}
    except ImportError as e:
        results['faiss'] = {'status': '❌ NOT INSTALLED', 'error': str(e)}
    
    # Test ONNX Runtime
    try:
        import onnxruntime
        results['onnxruntime'] = {'status': '✅ INSTALLED', 'version': onnxruntime.__version__}
    except ImportError as e:
        results['onnxruntime'] = {'status': '❌ NOT INSTALLED', 'error': str(e)}
    
    return results

def test_camera_access():
    """Test camera hardware access"""
    try:
        import cv2
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            ret, frame = cap.read()
            cap.release()
            if ret:
                return "✅ Camera access working - frame captured successfully"
            else:
                return "⚠️ Camera opened but no frame captured"
        else:
            return "⚠️ No camera detected (normal if no USB camera connected)"
    except Exception as e:
        return f"❌ Camera access failed: {e}"

def check_conflicting_packages():
    """Check for packages that might cause conflicts"""
    import subprocess
    import sys
    
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', 'list'], 
                              capture_output=True, text=True)
        installed_packages = result.stdout.lower()
        
        conflicts = []
        if 'albumentations' in installed_packages:
            conflicts.append('albumentations (may conflict with scipy versions)')
        if 'scipy' in installed_packages and '1.9' in installed_packages:
            conflicts.append('scipy 1.9.x (conflicts with newer packages)')
        if 'opencv-contrib-python' in installed_packages:
            conflicts.append('opencv-contrib-python (may conflict with opencv-python)')
            
        return conflicts
    except:
        return ["Could not check for conflicts"]

def print_results():
    """Print comprehensive test results"""
    print("🔍 Camera Detection Setup Test")
    print("=" * 50)
    
    # Test imports
    print("\n📦 Package Installation Status:")
    results = test_imports()
    for package, info in results.items():
        if 'version' in info:
            print(f"  {package:<12}: {info['status']} - v{info['version']}")
        else:
            print(f"  {package:<12}: {info['status']}")
            if 'error' in info:
                print(f"                Error: {info['error']}")
    
    # Test camera
    print(f"\n📹 Camera Hardware Test:")
    camera_result = test_camera_access()
    print(f"  {camera_result}")
    
    # Check conflicts
    print(f"\n⚠️ Potential Conflicts:")
    conflicts = check_conflicting_packages()
    if conflicts:
        for conflict in conflicts:
            print(f"  - {conflict}")
    else:
        print("  No known conflicts detected")
    
    # Summary
    print(f"\n📊 Summary:")
    installed = sum(1 for r in results.values() if '✅' in r['status'])
    total = len(results)
    print(f"  Packages installed: {installed}/{total}")
    
    if installed == total:
        print("  🎉 All dependencies ready! Face detection should work.")
    elif installed >= 3:  # opencv, numpy, pillow
        print("  ⚠️ Basic camera functionality ready. Install missing packages for face detection.")
    else:
        print("  ❌ Missing critical dependencies. Follow installation guide.")
    
    print(f"\n💡 Next Steps:")
    if installed < total:
        print("  1. Follow the installation guide: install_camera_dependencies.md")
        print("  2. Install missing packages one by one")
        print("  3. Run this test again to verify")
    else:
        print("  1. Start the server: python start_unified_server.py --enable-fts")
        print("  2. Open browser: http://localhost:3000")
        print("  3. Check Camera Management page")

if __name__ == "__main__":
    print_results()