# 🚀 Django Job Portal

A full-stack Job Portal built with **Django**, **Django REST Framework**, **PostgreSQL**, and **Tailwind CSS**. The platform allows recruiters to post jobs and manage applicants while candidates can search and apply for jobs.

---

## 🌐 Live Demo

https://jobportal1-w6b9.onrender.com/

---

# ✨ Features

### Authentication
- Custom User Model
- User Registration
- User Login & Logout
- Recruiter and Candidate Roles
- JWT Authentication (SimpleJWT)

### Recruiter Features
- Create Job
- Update Job
- Delete Job
- View Posted Jobs
- View Applicants for Each Job

### Candidate Features
- Browse Jobs
- Search Jobs
- Filter Jobs
- Order Jobs
- View Job Details
- Apply to Jobs
- View Applied Jobs

### REST API
- JWT Login
- JWT Refresh Token
- Job APIs
- Application APIs
- Recruiter APIs
- Pagination
- Filtering
- Ordering

---

# 🛠 Tech Stack

### Backend
- Python
- Django
- Django REST Framework

### Database
- PostgreSQL

### Authentication
- Django Authentication
- Simple JWT

### Frontend
- HTML
- Tailwind CSS
- JavaScript

### Deployment
- Render
- Gunicorn
- WhiteNoise

### Version Control
- Git
- GitHub

---

# 📂 Project Structure

```
jobportal/
│
├── core/
│   ├── models.py
│   ├── views.py
│   ├── api_views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── api_urls.py
│   ├── templates/
│   ├── static/
│
├── jobportal/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/UdayM07/jobportal.git
```

```bash
cd jobportal
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Database

Create a PostgreSQL database and update `settings.py`.

---

## Apply Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Run Development Server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000
```

---

# 🔑 API Authentication

Obtain Access Token

```
POST /api/token/
```

Refresh Token

```
POST /api/token/refresh/
```

Use

```
Authorization: Bearer <access_token>
```

---

# 📋 Main APIs

### Authentication

- Register User
- Login User
- JWT Token
- Refresh Token

### Jobs

- List Jobs
- Job Details
- Create Job
- Update Job
- Delete Job

### Applications

- Apply Job
- My Applications
- Recruiter Applicants

---

# 🚀 Deployment

This project is deployed on **Render** using:

- Gunicorn
- WhiteNoise
- PostgreSQL
- Environment Variables

Deployment steps included:

- Production settings
- Static file collection
- Database migration
- Environment variable configuration
- Gunicorn configuration
- PostgreSQL connection
- Render Web Service

---

# 📚 Concepts Used

- Django ORM
- Model Relationships
- Custom User Model
- Authentication
- Authorization
- Model Forms
- CRUD Operations
- Django Templates
- Static Files
- Django REST Framework
- Serializers
- Generic API Views
- JWT Authentication
- Pagination
- Filtering
- Ordering
- PostgreSQL
- Git
- GitHub
- Deployment

---

# 🔮 Future Improvements

- Email Verification
- Resume Upload
- Company Dashboard
- Bookmark Jobs
- AI Resume Analyzer
- Job Recommendation System
- Email Notifications

---

# 👨‍💻 Author

**Uday M**

GitHub:
https://github.com/UdayM07

---

# ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.