# Hospital Management System (HMS)

A comprehensive Django-based Hospital Management System with a stunning modern UI for managing patient records, prescriptions, and medical information.

## 🌟 Features

- **User Authentication**: Secure login and registration system
- **Patient Management**: Add, view, edit, and delete patient records
- **Prescription Management**: Create and manage prescriptions for patients
- **Search & Filter**: Quick search functionality for patients
- **Responsive UI**: Beautiful, modern interface with gradient designs and animations
- **MySQL Database**: Scalable database for storing patient and prescription data
- **Admin Panel**: Django admin interface for system administration
- **User Roles**: Multi-user support with different access levels

## 📋 Prerequisites

Before setting up HMS, ensure you have:

- Python 3.8 or higher
- MySQL Server (8.0 or higher recommended)
- pip (Python package manager)
- Virtual environment support

## 🚀 Installation & Setup

### 1. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure MySQL Database

First, create a MySQL database:

```sql
CREATE DATABASE hms_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Optional: Create a dedicated MySQL user:

```sql
CREATE USER 'hms_user'@'localhost' IDENTIFIED BY 'hms_password';
GRANT ALL PRIVILEGES ON hms_db.* TO 'hms_user'@'localhost';
FLUSH PRIVILEGES;
```

### 4. Update Database Configuration

Edit `hms_project/settings.py` and update the DATABASES section:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hms_db',
        'USER': 'root',          # Change if using custom user
        'PASSWORD': '',          # Add password if set
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

Or use the automated setup script:

```bash
python setup_db.py
```

Default credentials:
- Username: `admin`
- Password: `admin123`

### 7. Run Development Server

```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000`

## 📱 UI Highlights

### Modern Design Features
- **Gradient Backgrounds**: Beautiful purple and blue gradient theme
- **Smooth Animations**: Slide-up and fade-in animations
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Interactive Cards**: Hover effects and transitions
- **Professional Color Scheme**: Easy on the eyes with accessibility in mind

### Key Pages
1. **Login/Register**: Authentication with beautiful card layout
2. **Dashboard**: Overview of system statistics and recent patients
3. **Patients List**: Searchable patient directory with pagination
4. **Patient Detail**: Complete patient information with prescriptions
5. **Add/Edit Patient**: Form-based patient management
6. **Prescriptions**: Manage all prescriptions in the system

## 🗂️ Project Structure

```
hms_project/
├── manage.py
├── requirements.txt
├── setup_db.py
├── hms_project/
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── users/
│   │   ├── views.py         # Authentication views
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── models.py
│   ├── patients/
│   │   ├── models.py        # Patient model
│   │   ├── views.py         # CRUD operations
│   │   ├── forms.py
│   │   ├── admin.py
│   │   └── urls.py
│   └── prescriptions/
│       ├── models.py        # Prescription model
│       ├── views.py         # CRUD operations
│       ├── forms.py
│       ├── admin.py
│       └── urls.py
├── templates/
│   ├── base.html            # Base template
│   ├── dashboard.html
│   ├── auth/
│   │   ├── login.html
│   │   └── register.html
│   ├── patients/
│   │   ├── patient_list.html
│   │   ├── patient_detail.html
│   │   └── patient_form.html
│   └── prescriptions/
│       ├── prescription_list.html
│       ├── prescription_detail.html
│       └── prescription_form.html
└── static/
    └── css/
        └── style.css        # Custom styling
```

## 🔐 Security Features

- CSRF Protection on all forms
- Password validation
- Email verification support
- Input validation and sanitization
- Secure password hashing with Django's default algorithm

## 📊 Database Models

### Patient Model
- Patient ID (Auto-increment)
- Personal Information (Name, DOB, Gender, Email, Phone)
- Medical Information (Blood Group, Allergies, Medical History)
- Address Information (City, State, Postal Code)
- Emergency Contact
- Timestamps (Created, Updated)

### Prescription Model
- Prescription ID (Auto-increment)
- Patient Foreign Key
- Medicine Name
- Dosage
- Frequency (Once Daily, Twice Daily, etc.)
- Duration & Duration Unit
- Instructions & Side Effects
- Prescribed By (User Foreign Key)
- Notes
- Timestamps (Prescribed Date, Created, Updated)

## 🎨 Customization

### Change Color Theme
Edit `static/css/style.css` and modify the CSS variables:

```css
:root {
    --primary-color: #6366f1;
    --secondary-color: #ec4899;
    --success-color: #10b981;
    /* ... other colors ... */
}
```

### Update Database
To add new fields or make schema changes:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 🧪 Testing

Run tests with:

```bash
python manage.py test
```

## 📝 Available Endpoints

### Authentication
- `GET /auth/login/` - Login page
- `POST /auth/login/` - Process login
- `GET /auth/register/` - Registration page
- `POST /auth/register/` - Create new user
- `GET /auth/logout/` - Logout user

### Dashboard
- `GET /dashboard/` - Main dashboard

### Patients
- `GET /patients/` - List all patients
- `GET /patients/<id>/` - View patient details
- `GET /patients/create/` - Add patient form
- `POST /patients/create/` - Save new patient
- `GET /patients/<id>/update/` - Edit patient form
- `POST /patients/<id>/update/` - Update patient
- `POST /patients/<id>/delete/` - Delete patient

### Prescriptions
- `GET /prescriptions/` - List all prescriptions
- `GET /prescriptions/patient/<id>/create/` - Add prescription form
- `POST /prescriptions/patient/<id>/create/` - Save prescription
- `GET /prescriptions/<id>/update/` - Edit prescription form
- `POST /prescriptions/<id>/update/` - Update prescription
- `POST /prescriptions/<id>/delete/` - Delete prescription

## 🐛 Troubleshooting

### MySQL Connection Error
```
Error: "No module named 'MySQLdb'"
Solution: pip install mysqlclient
```

### Database Error
```
Error: "Unknown database 'hms_db'"
Solution: Create the database using MySQL commands above
```

### Static Files Not Loading
```
Solution: python manage.py collectstatic
```

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📞 Support

For issues and questions, please create an issue in the repository.

## 🎯 Future Enhancements

- [ ] Appointment scheduling
- [ ] Medical reports generation
- [ ] Billing and invoice system
- [ ] SMS/Email notifications
- [ ] Multi-user roles and permissions
- [ ] Patient portal for self-service
- [ ] Mobile app integration
- [ ] Analytics and reporting dashboard
- [ ] Backup and recovery system
- [ ] Two-factor authentication

---

**Happy Healthcare Management! 🏥**
