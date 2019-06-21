from rest_framework import serializers
from .models import Issue
from django.contrib.auth.models import User
from drf_extra_fields.fields import Base64ImageField

class IssueListSerializer(serializers.ModelSerializer):
    thumbnail = Base64ImageField(represent_in_base64=True)
    class Meta:
        model = Issue
        fields = ('pk', 'description', 'issueType', 'date_time_posted', 'latitude', 'longitude', 'resolved', 'posterName', 'posterPhone', 'posterEmail', 'notes', 'thumbnail')

class IssueViewSerializer(serializers.ModelSerializer):
    image = Base64ImageField(represent_in_base64=True)
    class Meta:
        model = Issue
        fields = ('pk', 'description', 'issueType', 'date_time_posted', 'latitude', 'longitude', 'resolved', 'posterName', 'posterPhone', 'posterEmail', 'notes', 'image')

class IssueSaveSerializer(serializers.ModelSerializer):
    image = Base64ImageField(represent_in_base64=True)
    thumbnail = Base64ImageField(represent_in_base64=True)
    class Meta:
        model = Issue
        fields = ('pk', 'description', 'issueType', 'date_time_posted', 'latitude', 'longitude', 'resolved', 'posterName', 'posterPhone', 'posterEmail', 'notes', 'image', 'thumbnail')
   