from django.db import models
from django.utils import timezone
from phonenumber_field.serializerfields import PhoneNumberField
from drf_extra_fields.fields import Base64ImageField
from PIL import Image
import io
import base64



# Create your models here.
class Issue(models.Model):
    def date_time_posted_default():
        return timezone.now()

    description = models.TextField()
    issueType = models.CharField(max_length=50)
    image = models.ImageField(upload_to='issueImage')
    thumbnail = models.ImageField(upload_to='issueImage', blank=True, null=True)
    date_time_posted = models.DateTimeField(default=date_time_posted_default)
    latitude = models.DecimalField(max_digits=25,decimal_places=5)
    longitude = models.DecimalField(max_digits=25,decimal_places=5)
    notes = models.TextField(blank=True)
    resolved = models.BooleanField(default=False)

    posterName = models.CharField(max_length=100, blank=True)
    posterPhone = models.CharField(max_length=14, blank=True)
    posterEmail = models.EmailField(blank=True)

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

    def __str__(self):
        return self.description