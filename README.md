# 🛒 Marketplace API

**Marketplace API** is a web application built with **Django 5.1.4** and **Django REST Framework**. It allows users to create and manage item listings, connect with other users, leave reviews, and more. The API provides robust functionality for a fully-featured online marketplace.

This project was developed as part of the **SoftUni Django Advanced Course**.

---

### 🚀 Features

- User authentication and JWT token management
- CRUD operations for item listings
- User profile management
- Reviews and ratings system
- Admin panel for managing listings, users, and reviews
- API documentation via **DRF Spectacular**

---

## 🛠️ Technologies Used

- [Django 5.1.4](https://www.djangoproject.com/) — High-level Python web framework for rapid development
- [Django REST Framework](https://www.django-rest-framework.org/) — Toolkit for building APIs
- [Django Filter](https://django-filter.readthedocs.io/en/stable/) — Filtering for Django models and QuerySets
- [django-silk](https://github.com/jazzband/django-silk) — Profiling and performance monitoring for Django
- [djangorestframework-simplejwt](https://github.com/jazzband/django-rest-framework-simplejwt) — JWT-based authentication for DRF
- [drf-spectacular](https://github.com/tfranzel/drf-spectacular) — OpenAPI 3.0 schema generation for Django REST Framework
- [Pillow](https://python-pillow.org/) — Image processing library for handling uploaded images
- [Redis](https://redis.io/) — In-memory data structure store for caching and session management
- [PyJWT](https://pyjwt.readthedocs.io/en/stable/) — JSON Web Token library
- [django-extensions](https://django-extensions.readthedocs.io/en/latest/) — Useful extensions for Django
- [django-silk](https://github.com/jazzband/django-silk) — Performance profiling and analysis
- [isort](https://pycqa.github.io/isort/) — Sorting Python imports
- [autopep8](https://github.com/hhatto/autopep8) — Automatic PEP 8 code formatting
- [sqlparse](https://github.com/andialbrecht/sqlparse) — SQL parser for Python
- [tzdata](https://pypi.org/project/tzdata/) — Time zone data for Python


## 📦 Installation

To set up and run **Marketplace API** locally, follow these steps:

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Ivaylo1992/marketplace_api.git
cd marketplace_api
```

### 2. Create and activate a virtual environment (macOS/Linux)

To create a virtual environment and activate it, run the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2.1 Create and activate a virtual environment (Windows)

To create a virtual environment and activate it, run the following commands:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install project dependencies

Once your virtual environment is activated, you need to install the required project dependencies. Run the following command:

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory of the project to store sensitive information such as your **JWT secret**, **Redis connection**, and **database credentials**.

Example `.env` file:

```bash
DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/DBNAME
JWT_SECRET_KEY=your_jwt_secret_key
REDIS_URL=redis://localhost:6379/0
```

### 5. Run database migrations

To set up the database schema and apply necessary migrations, run the following command:

```bash
python manage.py migrate
```

### 6. Create a superuser (admin account)

To access the Django admin panel and manage the application, create a superuser by running the following command:

```bash
python manage.py createsuperuser
```

### 7. Start the development server

To start the server and run the application locally, execute the following command:

```bash
python manage.py runserver
```

### 8. Access the application

Once the development server is running, you can access the application through your web browser at: http://localhost:8000

## 📖 API Documentation

The **Marketplace API** is documented using **DRF Spectacular**. To view the full API documentation, navigate to the following URL:

http://localhost:8000/api/schema/


This URL will generate and display a complete **OpenAPI 3.0** specification for all the available endpoints, including request/response examples, parameter details, and more.

### Features of the Documentation:

- **Interactive UI**: The OpenAPI documentation is fully interactive, allowing you to test endpoints directly from the browser.
- **Endpoint Overview**: All available API endpoints will be listed, including detailed descriptions, required parameters, and response formats.
- **Authentication**: The documentation provides information on how to authenticate and pass tokens for accessing protected endpoints.

> **Note**: Make sure the server is running (`python manage.py runserver`) to access the documentation at `http://localhost:8000/api/schema/`.

---

This section directs users to the auto-generated, interactive API documentation for easy reference and testing. Let me know if you'd like any additional details or adjustments! 🚀

## 📦 Requirements

Before running the project, ensure you have the following installed:

- **Python 3.8+**
- **PostgreSQL** (or another database supported by Django)
- **Redis** (for caching and queue management, optional but recommended)
- **pip** (Python package installer)

### Installing Dependencies

To install all the required dependencies, simply run:

```bash
pip install -r requirements.txt
```


