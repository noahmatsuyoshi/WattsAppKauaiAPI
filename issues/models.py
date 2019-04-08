from django.db import models
from django.utils import timezone
from phonenumber_field.serializerfields import PhoneNumberField


# Create your models here.
class Issue(models.Model):
    def date_time_posted_default():
        return timezone.now()

    description = models.TextField()
    issueType = models.CharField(max_length=50)
    image = models.ImageField()
    date_time_posted = models.DateTimeField(default=date_time_posted_default)
    latitude = models.DecimalField(max_digits=25,decimal_places=5)
    longitude = models.DecimalField(max_digits=25,decimal_places=5)
    resolved = models.BooleanField(default=False)

    posterName = models.CharField(max_length=100, blank=True)
    posterPhone = models.CharField(max_length=14, blank=True)
    posterEmail = models.EmailField(blank=True)

    def __str__(self):
        return self.description