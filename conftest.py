import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from events.models import Event
from django.utils import timezone

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def admin_user():
    return User.objects.create_superuser('admin', 'admin@test.com', 'admin123')

@pytest.fixture
def regular_user():
    return User.objects.create_user('user', 'user@test.com', 'user123')

@pytest.fixture
def event_data():
    return {
        'title': 'Test Event',
        'description': 'Test Description',
        'date': timezone.now(),
        'venue': 'Test Venue',
        'total_tickets': 100,
        'available_tickets': 100,
        'price': 99.99
    }

@pytest.fixture
def created_event(event_data):
    return Event.objects.create(**event_data)