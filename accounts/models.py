from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import forms


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Room(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    image_url = models.CharField(max_length=2083, default="")
    price = models.FloatField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Reservation(models.Model):
    TIMESLOT = (
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    room = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)
    date = models.DateField(null=True, blank=True)
    time_slot = models.CharField(max_length=255, null=True, blank=True, choices=TIMESLOT)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

