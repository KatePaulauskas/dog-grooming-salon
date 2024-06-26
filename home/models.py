from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class About(models.Model):
    image = CloudinaryField('image', default='placeholder')
    welcome_message = title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()


    """
    Add Meta class to the models to avoid 's'
    Being appended at the end of the model name in the Django admin panel
    Source: https://docs.djangoproject.com/en/5.0/ref/
    models/options/#verbose-name-plural
    """
    class Meta:
        verbose_name_plural = "About"

class Services(models.Model):
    id = models.AutoField(primary_key=True)
    service_image = CloudinaryField('image', default='placeholder')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name
