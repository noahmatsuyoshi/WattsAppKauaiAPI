from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

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

    poster = models.ForeignKey('auth.User', related_name='issues', on_delete=models.CASCADE)

    #name = models.CharField(max_length=50, blank=True)
    #phone = PhoneNumberField(blank=True)
    #email = models.EmailField(blank=True)

    

    def __str__(self):
        return self.description