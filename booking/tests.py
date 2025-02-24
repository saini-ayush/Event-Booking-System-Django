import pytest
from .models import Booking

@pytest.mark.django_db
class TestBooking:
    def test_create_booking(self, api_client, regular_user, created_event):
        api_client.force_authenticate(user=regular_user)
        initial_tickets = created_event.available_tickets
        response = api_client.post('/api/bookings/', {
            'event': created_event.id,
            'number_of_tickets': 2
        })
        assert response.status_code == 201
        assert Booking.objects.count() == 1
        
        created_event.refresh_from_db()
        assert created_event.available_tickets == initial_tickets - 2

    def test_cancel_booking(self, api_client, regular_user, created_event):
        api_client.force_authenticate(user=regular_user)
        initial_tickets = created_event.available_tickets
        
        # Create booking
        booking = Booking.objects.create(
            user=regular_user, 
            event=created_event, 
            number_of_tickets=2
        )
        
        created_event.refresh_from_db()
        assert created_event.available_tickets == initial_tickets - 2
        
        # Cancel booking
        response = api_client.delete(f'/api/bookings/{booking.id}/')
        assert response.status_code == 204
        assert Booking.objects.count() == 0
        
        created_event.refresh_from_db()
        assert created_event.available_tickets == initial_tickets

    def test_booking_with_no_tickets(self, api_client, regular_user, created_event):
        created_event.available_tickets = 0
        created_event.save()
        api_client.force_authenticate(user=regular_user)
        response = api_client.post('/api/bookings/', {
            'event': created_event.id,
            'number_of_tickets': 2
        })
        assert response.status_code == 400
