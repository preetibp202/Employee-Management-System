# Employee Management System  
https://employee-management-system-1-hd2h.onrender.com/home/

A full-stack web application built with **Python and Django** for managing employee records and testimonials. The system provides CRUD functionality through a clean, responsive interface and uses Django ORM for database operations.

## ✨ Features

* Employee management with complete **CRUD operations**
* Add, view, update, and delete employee records
* Manage employee ID, name, email, department, address, phone, and working status
* Testimonial management with ratings and image uploads
* Django Forms and server-side form handling
* Django ORM for database operations
* Responsive user interface using Bootstrap
* Static and media file handling
* Django Admin integration

## 🛠️ Tech Stack

| Category   | Technologies             |
| ---------- | ------------------------ |
| Backend    | Python, Django 5.2       |
| Frontend   | HTML5, CSS3, Bootstrap 5 |
| Database   | SQLite                   |
| ORM        | Django ORM               |
| Tools      | Git, GitHub, VS Code     |
| Deployment | Render                   |

## 🏗️ Project Architecture

The application follows Django's **MVT (Model-View-Template)** architecture.

```text
User
  │
  ▼
Django URLs
  │
  ▼
Views
  │
  ├──── Templates ──── HTML / Bootstrap / CSS
  │
  ▼
Models
  │
  ▼
Django ORM
  │
  ▼
SQLite Database
```

## 📌 Main Modules

### Employee Management

The employee module allows users to:

* Add employee records
* View all employees
* Update employee information
* Delete employees
* Track employee working status
* Manage department and contact information

### Testimonial Management

The testimonial module provides:

* Testimonial creation
* Rating management
* Image upload
* Testimonial listing
* Update and delete functionality

## 📂 Project Structure

```text
employee-management-system/
│
├── Employee/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── emp/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── static/
│   └── css/
│
├── media/
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/employee-management-system.git
cd employee-management-system
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## 🔐 Admin Panel

Create an administrator account:

```bash
python manage.py createsuperuser
```

Then access:

```text
http://127.0.0.1:8000/admin/
```

## 📚 Key Django Concepts Used

* Django MVT Architecture
* URL Routing
* Views
* Models
* Django ORM
* Forms
* Templates
* CRUD Operations
* Database Migrations
* Static Files
* Media Files
* Django Admin

## 🚀 Future Enhancements

* User authentication and authorization
* Employee search and filtering
* Employee dashboard with statistics
* PostgreSQL integration
* Django REST Framework API
* Cloud-based media storage
* Production deployment

## 👩‍💻 Author

**Preeti Patil**

B.Tech Computer Science & Engineering | 2026

---

⭐ If you find this project useful, consider giving the repository a star.
