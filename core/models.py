from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    ROLE_CHOICES = [
        ('organiser', 'Organiser'),
        ('participant', 'Participant'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    capacity = models.PositiveIntegerField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('CANCELLED', 'Cancelled'),
        ('CHECKED_IN', 'Checked In'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    ticket_id = models.CharField(max_length=100, unique=True)
    qr_code_path = models.CharField(max_length=255, null=True, blank=True)

class Payment(models.Model):
    STATUS_CHOICES = [
        ('INITIATED', 'Initiated'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    ]
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_gateway = models.CharField(max_length=50)
    payment_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    payment_time = models.DateTimeField(auto_now_add=True)

class CheckinLog(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    scanned_by = models.ForeignKey(User, on_delete=models.CASCADE)
    checkin_time = models.DateTimeField(auto_now_add=True)
