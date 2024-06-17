from django.db import models
from django.contrib.auth.models import User
from home.models import Services
from groomers.models import GroomerSchedule, Groomers
# Import the time and timezone classes
from datetime import time
from django.utils import timezone



class Appointment(models.Model):

    """
    Sourse: https://zerotobyte.com/django-choices-best-practices/
    """
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    groomer = models.ForeignKey(Groomers, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=time(9, 0))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.service.name} - {self.date} {self.time} - {self.get_status_display()}"