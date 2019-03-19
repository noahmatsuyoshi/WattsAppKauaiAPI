from rest_framework import serializers
from .models import Issue
from django.contrib.auth.models import User

class IssueSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')
    class Meta:
        model = Issue
        fields = ('id', 'description', 'poster', 'issueType', 'image', 'date_time_posted', 'latitude', 'longitude', 'resolved')

class UserSerializer(serializers.ModelSerializer):
    issues = serializers.PrimaryKeyRelatedField(many=True, queryset=Issue.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'issues')