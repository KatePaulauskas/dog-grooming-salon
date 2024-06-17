from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Groomers(models.Model):
    id = models.AutoField(primary_key=True)
    groomer_image = CloudinaryField('image', default='placeholder')
    name = models.CharField(max_length=200)
    description = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Groomers"

    def __str__(self):
        return self.name    


class GroomerSchedule(models.Model):
    groomer = models.OneToOneField(Groomers, on_delete=models.CASCADE, related_name='schedule')
    monday_start = models.TimeField(null=True, blank=True)
    monday_end = models.TimeField(null=True, blank=True)
    tuesday_start = models.TimeField(null=True, blank=True)
    tuesday_end = models.TimeField(null=True, blank=True)
    wednesday_start = models.TimeField(null=True, blank=True)
    wednesday_end = models.TimeField(null=True, blank=True)
    thursday_start = models.TimeField(null=True, blank=True)
    thursday_end = models.TimeField(null=True, blank=True)
    friday_start = models.TimeField(null=True, blank=True)
    friday_end = models.TimeField(null=True, blank=True)
    saturday_start = models.TimeField(null=True, blank=True)
    saturday_end = models.TimeField(null=True, blank=True)
    sunday_start = models.TimeField(null=True, blank=True)
    sunday_end = models.TimeField(null=True, blank=True)
    lunch_start = models.TimeField()
    lunch_end = models.TimeField()

    def __str__(self):
        return f"{self.groomer.name}'s schedule"
    