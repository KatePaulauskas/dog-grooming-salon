from django.db import models
from django.contrib.auth.models import User
from home.models import Services
from groomers.models import Groomers

class Appointment(models.Model):

    # Sourse: https://zerotobyte.com/django-choices-best-practices/
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    groomer = models.ForeignKey(Groomers, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.service.name} - {self.datetime} - {self.get_status_display()}"


