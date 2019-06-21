from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.exclude(email="wattsappkauaiguest@kiuc.coop")
    serializer_class = EmployeeSerializer
    

    def get(self, request, *args, **kwargs):
        if not self.request.user.admin:
            return super().permission_denied(self.request, message='You must be an admin to perform this action')
        return super().get(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        if not request.user.admin:
            return super().permission_denied(self.request, message='You must be an admin to perform this action')
        return super().create(request, *args, **kwargs)

class EmployeeEdit(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def update(self, request, pk, *args, **kwargs):
        if not request.user.admin and request.user.pk != pk:
            return super().permission_denied(self.request, message='You must be an admin to perform this action')
        if not request.user.admin and 'admin' in request.data:
            del request.data['admin']
        return super().update(request, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        if not request.user.admin:
            return super().permission_denied(self.request, message='You must be an admin to perform this action')
        return super().delete(request, pk, *args, **kwargs)
    