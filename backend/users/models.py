from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    available_seats = models.IntegerField()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    num_bookings = models.IntegerField()
