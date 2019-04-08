from rest_framework import serializers
from .models import Issue
from django.contrib.auth.models import User
from drf_extra_fields.fields import Base64ImageField

class IssueSerializer(serializers.ModelSerializer):
    #poster = serializers.ReadOnlyField(source='poster.username')
    image = Base64ImageField()
    class Meta:
        model = Issue
        fields = ('id', 'description', 'issueType', 'image', 'date_time_posted', 'latitude', 'longitude', 'resolved', 'posterName', 'posterPhone', 'posterEmail')

    