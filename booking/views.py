from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from rest_framework import serializers
from django.db import transaction


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(user=self.request.user)

    @transaction.atomic
    def perform_create(self, serializer):
        event = serializer.validated_data['event']
        tickets = serializer.validated_data['number_of_tickets']
        
        if event.available_tickets < tickets:
            raise serializers.ValidationError("Not enough tickets available")
            
        serializer.save(user=self.request.user)

    @transaction.atomic
    def perform_destroy(self, instance):
        instance.delete()  # This will trigger the delete method in the model
