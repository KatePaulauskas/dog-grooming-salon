from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class About(models.Model):
    image = models.ImageField
    welcome_message = title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()

class Services(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()
