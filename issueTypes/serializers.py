from rest_framework import serializers
from .models import IssueType
from django.contrib.auth.models import User

class IssueTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueType
        fields = ('issueType', 'pk', )

    