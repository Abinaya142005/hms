# Quick Start Guide for HMS

## Windows Users

### Step 1: Install MySQL
- Download from: https://dev.mysql.com/downloads/mysql/
- Install with default settings
- Create database: `hms_db`

### Step 2: Open PowerShell and Navigate to Project
```powershell
cd "c:\Users\ABINAYA.S\Desktop\hms\hms_project"
```

### Step 3: Create Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Requirements
```powershell
pip install -r requirements.txt
```

### Step 5: Setup Database
```powershell
python setup_db.py
```

### Step 6: Run Server
```powershell
python manage.py runserver
```

### Step 7: Access Application
Open your browser and go to: `http://127.0.0.1:8000`

### Step 8: Login
- Username: `admin`
- Password: `admin123`

## MySQL Connection Issues?

If you get MySQL connection errors, update the credentials in `hms_project/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hms_db',
        'USER': 'root',        # Your MySQL username
        'PASSWORD': '',        # Your MySQL password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## Features Ready to Use

✅ User Login & Registration
✅ Add Patients with Complete Medical History
✅ Edit & Delete Patient Records
✅ Add Prescriptions for Patients
✅ Edit & Delete Prescriptions
✅ Search Patients by Name, Email, Phone
✅ Beautiful Modern UI with Animations
✅ Responsive Design for Mobile & Desktop
✅ Admin Panel for System Management
✅ MySQL Database Integration

## Admin Access

Admin panel available at: `http://127.0.0.1:8000/admin/`
- Username: `admin`
- Password: `admin123`

Enjoy! 🏥
