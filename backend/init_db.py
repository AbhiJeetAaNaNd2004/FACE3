#!/usr/bin/env python3
"""
Database Initialization Script for Face Recognition Attendance System
Creates tables and inserts sample data
"""

import sys
import os
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).parent
sys.path.insert(0, str(backend_path))

from db.db_config import create_tables, get_db, test_connection
from db.db_models import Employee, UserAccount, CameraConfig
from app.security import get_password_hash
from datetime import date
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def initialize_database():
    """Initialize database with tables and sample data"""
    
    print("🗄️  Face Recognition Attendance System - Database Initialization")
    print("=" * 70)
    
    # Test database connection first
    print("🔍 Testing database connection...")
    if not test_connection():
        print("❌ Database connection failed. Please check your configuration.")
        return False
    
    print("✅ Database connection successful")
    
    # Create tables
    print("🏗️  Creating database tables...")
    try:
        create_tables()
        print("✅ Database tables created successfully")
    except Exception as e:
        print(f"❌ Error creating tables: {e}")
        return False
    
    # Insert sample data
    print("📝 Inserting sample data...")
    
    db = next(get_db())
    try:
        # Check if admin user already exists
        existing_admin = db.query(UserAccount).filter(UserAccount.username == "admin").first()
        if not existing_admin:
            # Create super admin user
            admin_user = UserAccount(
                username="admin",
                hashed_password=get_password_hash("admin123"),
                role="super_admin",
                is_active=True
            )
            db.add(admin_user)
            print("✅ Created super admin user (username: admin, password: admin123)")
        else:
            print("ℹ️  Super admin user already exists")
        
        # Check if sample employees exist
        existing_employee = db.query(Employee).filter(Employee.employee_id == "EMP001").first()
        if not existing_employee:
            # Create sample employees
            employees = [
                Employee(
                    employee_id="EMP001",
                    name="John Doe",
                    department="Engineering",
                    role="Software Developer",
                    date_joined=date(2023, 1, 15),
                    email="john.doe@company.com",
                    phone="+1234567890",
                    is_active=True
                ),
                Employee(
                    employee_id="EMP002",
                    name="Jane Smith",
                    department="HR",
                    role="HR Manager",
                    date_joined=date(2023, 2, 1),
                    email="jane.smith@company.com",
                    phone="+1234567891",
                    is_active=True
                ),
                Employee(
                    employee_id="EMP003",
                    name="Mike Johnson",
                    department="Engineering",
                    role="Senior Developer",
                    date_joined=date(2023, 3, 10),
                    email="mike.johnson@company.com",
                    phone="+1234567892",
                    is_active=True
                )
            ]
            
            for employee in employees:
                db.add(employee)
            
            print("✅ Created sample employees")
        else:
            print("ℹ️  Sample employees already exist")
        
        # Check if sample camera exists
        existing_camera = db.query(CameraConfig).filter(CameraConfig.camera_id == 0).first()
        if not existing_camera:
            # Create sample camera configuration
            camera = CameraConfig(
                camera_id=0,
                camera_name="Main Entrance Camera",
                camera_type="entry",
                resolution_width=640,
                resolution_height=480,
                fps=30,
                status="discovered",
                is_active=True,
                location_description="Main entrance door"
            )
            db.add(camera)
            print("✅ Created sample camera configuration")
        else:
            print("ℹ️  Sample camera already exists")
        
        # Commit all changes
        db.commit()
        print("✅ Sample data inserted successfully")
        
        return True
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error inserting sample data: {e}")
        return False
    finally:
        db.close()

def main():
    """Main function"""
    print("Starting database initialization...")
    
    success = initialize_database()
    
    if success:
        print("\n🎉 Database initialization completed successfully!")
        print("=" * 70)
        print("📋 Summary:")
        print("   • Database tables created")
        print("   • Super admin user: admin / admin123")
        print("   • Sample employees added")
        print("   • Sample camera configuration added")
        print("=" * 70)
        print("🚀 You can now start the server!")
    else:
        print("\n❌ Database initialization failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()