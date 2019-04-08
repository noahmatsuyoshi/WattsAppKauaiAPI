from django.shortcuts import render
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from .models import Issue
from .serializers import IssueSerializer
from django.contrib.auth.models import User

# Create your views here.
class IssueView(viewsets.ModelViewSet):

    def get(self, request, format=None):
        issues = Issue.objects.all()
        serializer = IssueSerializer(issues, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    def perform_create(self, serializer):
        serializer.save()

