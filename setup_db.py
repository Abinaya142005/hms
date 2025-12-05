#!/usr/bin/env python
"""
Setup script for HMS - Hospital Management System
This script initializes the database and creates a superuser
"""

import os
import sys
import django

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Setup Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hms_project.settings')
django.setup()

from django.core.management import call_command
from django.contrib.auth.models import User

def run_migrations():
    """Run Django migrations"""
    print("Running migrations...")
    call_command('migrate')
    print("✓ Migrations completed!")

def create_superuser():
    """Create a superuser account"""
    if not User.objects.filter(username='admin').exists():
        print("\nCreating superuser...")
        User.objects.create_superuser('admin', 'admin@hms.com', 'admin123')
        print("✓ Superuser created!")
        print("  Username: admin")
        print("  Password: admin123")
    else:
        print("\n✓ Superuser already exists!")

def main():
    print("=" * 50)
    print("HMS - Hospital Management System Setup")
    print("=" * 50)
    
    try:
        run_migrations()
        create_superuser()
        
        print("\n" + "=" * 50)
        print("Setup completed successfully!")
        print("=" * 50)
        print("\nTo start the server:")
        print("  python manage.py runserver")
        print("\nThen open: http://127.0.0.1:8000")
        print("\nAdmin credentials:")
        print("  Username: admin")
        print("  Password: admin123")
        
    except Exception as e:
        print(f"\n✗ Error during setup: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
