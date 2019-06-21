from django.shortcuts import render
from rest_framework import viewsets, generics, permissions, status, views
from rest_framework.response import Response
from .models import IssueType
from .serializers import IssueTypeSerializer
from django.contrib.auth.models import User

# Create your views here.
class IssueTypesView(generics.ListCreateAPIView):
    queryset = IssueType.objects.all()
    serializer_class = IssueTypeSerializer

    def get(self, request, format=None):
        issueTypes = IssueType.objects.all()
        serializer = IssueTypeSerializer(issueTypes, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        if not request.user.admin:
            return super().permission_denied(self.request, message='You must be an admin to perform this action')
        return super().create(request, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        if not request.user.admin:
            return super().permission_denied(request, message='You must be an admin to perform this action')
        issueType = IssueType.objects.get(pk=pk)
        issueType.delete()
        return Response(data="Issue Type Deleted!", status=status.HTTP_204_NO_CONTENT)

    
    