from django.db import models
from django.contrib.auth.models import User
from events.models import Event

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateTimeField(auto_now_add=True)
    number_of_tickets = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"

    def save(self, *args, **kwargs):
        if not self.pk:  # Only for new bookings
            self.event.available_tickets -= self.number_of_tickets
            self.event.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.event.available_tickets += self.number_of_tickets
        self.event.save()
        super().delete(*args, **kwargs)