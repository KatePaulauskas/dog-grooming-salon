from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class About(models.Model):
    id = models.AutoField(primary_key=True)
    image = CloudinaryField('image', default='placeholder')
    welcome_message = title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)


    """
    Add Meta class to the models to avoid 's'
    Being appended at the end of the model name in the Django admin panel
    Source: Django Documentation - verbose_name
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
    created_at = models.DateTimeField()
    position = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Services"
        ordering = ['position']

    def __str__(self):
        return self.name

    """
    Convert duration (timedelta) to a string
    formatted as 'Xh Ym' representing hours and minutes.
    Source: Stack Overflow
    """
    def duration_in_hours_minutes(self):
        total_seconds = int(self.duration.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return f'{hours}h {minutes}m'
