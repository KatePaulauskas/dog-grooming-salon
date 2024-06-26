from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Gallery"
