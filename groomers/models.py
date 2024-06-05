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
