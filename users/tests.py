import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
class TestUser:
    def test_user_registration(self, api_client):
        data = {
            'username': 'newuser',
            'email': 'newuser@test.com',
            'password': 'strongpass123',
            'password2': 'strongpass123'
        }
        response = api_client.post('/api/register/', data)
        assert response.status_code == 201
        assert User.objects.count() == 1
        assert User.objects.get().username == 'newuser'

    def test_user_registration_password_mismatch(self, api_client):
        data = {
            'username': 'newuser',
            'email': 'newuser@test.com',
            'password': 'strongpass123',
            'password2': 'differentpass123'
        }
        response = api_client.post('/api/register/', data)
        assert response.status_code == 400
        assert User.objects.count() == 0

    def test_user_login(self, api_client, regular_user):
        response = api_client.post('/api/token/', {
            'username': 'user',
            'password': 'user123'
        })
        assert response.status_code == 200
        assert 'access' in response.data
        assert 'refresh' in response.data

    def test_invalid_login(self, api_client):
        response = api_client.post('/api/token/', {
            'username': 'nonexistent',
            'password': 'wrongpass'
        })
        assert response.status_code == 401