from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError
from rest_framework.exceptions import PermissionDenied
import logging

class ConfirmEmployeeAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form):
        if not request.user.admin:
            raise PermissionDenied()
        user.admin = request.data.get('admin')
        user.name = request.data.get('name')
        user.email = request.data.get('email')
        user.phone = request.data.get('phone')
        

        return DefaultAccountAdapter.save_user(self, request, user, form) # For other default validations.