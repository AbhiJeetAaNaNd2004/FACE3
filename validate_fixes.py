#!/usr/bin/env python3
"""
Validation Script for Face Tracking System Fixes
This script checks that all potential issues have been addressed.
"""

import os
import sys
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if a file exists"""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} - NOT FOUND")
        return False

def check_sqlite_removed():
    """Check that SQLite files have been removed"""
    print("🔍 Checking SQLite cleanup...")
    
    sqlite_files = [
        "backend/face_attendance.db",
        "face_attendance.db"
    ]
    
    found_sqlite = False
    for filepath in sqlite_files:
        if os.path.exists(filepath):
            print(f"❌ SQLite file still exists: {filepath}")
            found_sqlite = True
    
    if not found_sqlite:
        print("✅ No SQLite files found - good!")
    
    return not found_sqlite

def check_memory_fixes():
    """Check that memory optimization files exist"""
    print("\n🔍 Checking memory optimization fixes...")
    
    files_to_check = [
        ("fix_memory_and_ports.py", "Memory and port fix script"),
        ("start_system_fixed.py", "Fixed startup script"),
        ("start_backend_only.py", "Backend-only startup script"),
        ("start_frontend_only.py", "Frontend-only startup script"),
        ("start_fts_only.py", "FTS-only startup script"),
        ("start_camera_detection.py", "Camera detection script")
    ]
    
    all_good = True
    for filepath, description in files_to_check:
        if not check_file_exists(filepath, description):
            all_good = False
    
    return all_good

def check_pytorch_fixes():
    """Check that PyTorch memory fixes are in place"""
    print("\n🔍 Checking PyTorch memory fixes...")
    
    files_to_check = [
        "backend/core/fts_system.py",
        "backend/core/face_enroller.py"
    ]
    
    fixes_found = 0
    for filepath in files_to_check:
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if "torch.multiprocessing.set_sharing_strategy('file_system')" in content:
                print(f"✅ PyTorch multiprocessing fix found in {filepath}")
                fixes_found += 1
            else:
                print(f"❌ PyTorch multiprocessing fix NOT found in {filepath}")
        else:
            print(f"❌ File not found: {filepath}")
    
    return fixes_found == len(files_to_check)

def check_readme_updated():
    """Check that README has been updated"""
    print("\n🔍 Checking README updates...")
    
    if not os.path.exists("README.md"):
        print("❌ README.md not found")
        return False
    
    with open("README.md", 'r', encoding='utf-8') as f:
        content = f.read()
    
    required_sections = [
        "Running Components Separately",
        "Memory & Performance Fixes",
        "start_system_fixed.py",
        "start_backend_only.py",
        "start_frontend_only.py"
    ]
    
    all_found = True
    for section in required_sections:
        if section in content:
            print(f"✅ README section found: {section}")
        else:
            print(f"❌ README section missing: {section}")
            all_found = False
    
    return all_found

def check_potential_issues():
    """Check for other potential issues"""
    print("\n🔍 Checking for potential issues...")
    
    issues_found = []
    
    # Check for hardcoded SQLite references
    python_files = []
    for root, dirs, files in os.walk('.'):
        # Skip certain directories
        if any(skip in root for skip in ['.git', '__pycache__', 'node_modules', '.env']):
            continue
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    
    sqlite_references = 0
    for filepath in python_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'sqlite' in content.lower() and 'no sqlite' not in content.lower():
                    if filepath not in ['validate_fixes.py']:  # Exclude this file
                        sqlite_references += 1
                        print(f"⚠️ Potential SQLite reference in: {filepath}")
        except:
            continue
    
    if sqlite_references == 0:
        print("✅ No problematic SQLite references found")
    
    # Check for multiprocessing issues
    multiprocessing_files = []
    for filepath in python_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'multiprocessing' in content and 'Process(' in content:
                    multiprocessing_files.append(filepath)
        except:
            continue
    
    if multiprocessing_files:
        print("⚠️ Files using multiprocessing (check for memory issues):")
        for filepath in multiprocessing_files:
            print(f"   - {filepath}")
    else:
        print("✅ No problematic multiprocessing usage found")
    
    return len(issues_found)

def main():
    print("🎯 Face Tracking System Fixes Validation")
    print("=" * 50)
    
    checks = [
        ("SQLite cleanup", check_sqlite_removed),
        ("Memory fix scripts", check_memory_fixes),
        ("PyTorch memory fixes", check_pytorch_fixes),
        ("README updates", check_readme_updated)
    ]
    
    passed = 0
    total = len(checks)
    
    for check_name, check_func in checks:
        print(f"\n📋 {check_name}:")
        if check_func():
            passed += 1
        else:
            print(f"❌ {check_name} failed")
    
    # Additional checks
    issue_count = check_potential_issues()
    
    print("\n" + "=" * 50)
    print(f"📊 VALIDATION SUMMARY")
    print(f"✅ Passed: {passed}/{total} main checks")
    
    if passed == total and issue_count == 0:
        print("🎉 ALL FIXES VALIDATED SUCCESSFULLY!")
        print("\n💡 Ready to use:")
        print("   python start_system_fixed.py")
    else:
        print("⚠️ Some issues found - please review above")
        
    print("\n🔧 Available scripts:")
    print("   python fix_memory_and_ports.py    # Fix memory/port issues")
    print("   python start_system_fixed.py      # Start with all fixes")
    print("   python start_backend_only.py      # Backend API only")
    print("   python start_frontend_only.py     # Frontend only")
    print("   python start_fts_only.py          # Face Tracking only")
    print("   python start_camera_detection.py  # Camera testing")

if __name__ == "__main__":
    main()