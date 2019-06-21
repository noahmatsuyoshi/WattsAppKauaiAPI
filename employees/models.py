from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Employee(AbstractUser):
    name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=14, blank=True)
    admin = models.BooleanField()
    passwordChange = models.BooleanField()
    newIssueNotifications = models.BooleanField()

    def __str__(self):
        return self.name
    
