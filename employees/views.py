from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        if not self.request.user.admin:
            return super().permission_denied(self.request, message='You must be an admin to perform this action')
        return super().get_queryset()
    
    def create(self, request, *args, **kwargs):
        if not request.user.admin:
            return super().permission_denied(self.request, message='You must be an admin to perform this action')
        return super().create(request, *args, **kwargs)
