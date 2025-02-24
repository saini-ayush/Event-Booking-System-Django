import pytest
from django.utils import timezone
from .models import Event

@pytest.mark.django_db
class TestEvent:
    def test_event_creation(self, event_data):
        event = Event.objects.create(**event_data)
        assert event.title == "Test Event"
        assert event.available_tickets == 100

    def test_create_event_admin(self, api_client, admin_user, event_data):
        api_client.force_authenticate(user=admin_user)
        response = api_client.post('/api/events/', event_data)
        assert response.status_code == 201
        assert Event.objects.count() == 1

    def test_create_event_user(self, api_client, regular_user, event_data):
        api_client.force_authenticate(user=regular_user)
        response = api_client.post('/api/events/', event_data)
        assert response.status_code == 403

    def test_list_events(self, api_client, regular_user, created_event):
        api_client.force_authenticate(user=regular_user)
        response = api_client.get('/api/events/')
        assert response.status_code == 200
        assert len(response.data) == 1

    def test_delete_event_admin(self, api_client, admin_user, created_event):
        api_client.force_authenticate(user=admin_user)
        response = api_client.delete(f'/api/events/{created_event.id}/')
        assert response.status_code == 204
        assert Event.objects.count() == 0

    def test_update_event_admin(self, api_client, admin_user, created_event):
        api_client.force_authenticate(user=admin_user)
        update_data = {'title': 'Updated Event'}
        response = api_client.patch(f'/api/events/{created_event.id}/', update_data)
        assert response.status_code == 200
        assert Event.objects.get(id=created_event.id).title == 'Updated Event'
