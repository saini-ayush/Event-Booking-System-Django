# Event Booking System 

A Django REST Framework application for managing events and bookings with role-based access control.

## Features 

- **Event Management**
  - Create, update, and delete events (Admin only)
  - View available events
  - Track ticket availability

- **Booking Management**
  - Book tickets for events
  - Cancel bookings
  - View booking history

- **User Management**
  - JWT Authentication
  - Role-based access control (Admin/User)
  - User registration and login

## Tech Stack 💻

- Python 3.8+
- Django 5.0.2
- Django REST Framework 3.14.0
- PostgreSQL
- JWT Authentication
- pytest for testing

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/saini-ayush/Event-Booking-System-Django.git
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Setup .env File
```bash
SECRET_KEY='xxxxxxxx'
DB_NAME=event_booking_db
DB_USER=postgres
DB_PASSWORD=12345678
DB_HOST=localhost
DB_PORT=5433
JWT_SECRET_KEY='xxxxxxxxx'
JWT_ACCESS_TOKEN_LIFETIME=1
JWT_REFRESH_TOKEN_LIFETIME=7
```

5. Set up PostgreSQL database:
```bash
createdb event_booking_db
```

6. Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Create superuser:
```bash
python manage.py createsuperuser
```

8. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication Endpoints
- `POST /api/register/` - Register new user
- `POST /api/token/` - Obtain JWT token
- `POST /api/token/refresh/` - Refresh JWT token

### Admin Endpoints
- `POST /api/events/` - Create event
- `PUT /api/events/{id}/` - Update event
- `DELETE /api/events/{id}/` - Delete event
- `GET /api/events/` - View all events
- `GET /api/bookings/` - View all bookings

### User Endpoints
- `GET /api/events/` - View available events
- `POST /api/bookings/` - Book tickets
- `DELETE /api/bookings/{id}/` - Cancel booking
- `GET /api/bookings/` - View booking history

## Authentication

The API uses JWT (JSON Web Token) authentication. Include the token in request headers:
```
Authorization: Bearer <your_access_token>
```

## Testing 

Run tests using pytest:
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov

# Run specific tests
pytest events/tests.py
pytest bookings/tests.py
pytest users/tests.py
```

## Folder Structure

```
└── 📁EventManagementDjango
    └── 📁booking
        └── __init__.py
        └── admin.py
        └── apps.py
        └── models.py
        └── serializers.py
        └── tests.py
        └── views.py
    └── 📁config
        └── __init__.py
        └── asgi.py
        └── settings.py
        └── urls.py
        └── wsgi.py
    └── 📁events
        └── __init__.py
        └── admin.py
        └── apps.py
        └── models.py
        └── serializers.py
        └── tests.py
        └── views.py
    └── 📁users
        └── __init__.py
        └── admin.py
        └── apps.py
        └── models.py
        └── serializers.py
        └── tests.py
        └── views.py
    └── .env
    └── .gitignore
    └── conftest.py
    └── manage.py
    └── pytest.ini
    └── README.md
    └── requirements.txt
```