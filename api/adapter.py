from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError
from rest_framework.exceptions import PermissionDenied
import logging

class ConfirmEmployeeAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form):
        if not request.user.admin:
            raise PermissionDenied()
        user.email = request.data.get('email')
        user.admin = request.data.get('admin')
        user.passwordChange = True
        user.newIssueNotifications = True
        
        

        return DefaultAccountAdapter.save_user(self, request, user, form) # For other default validations.