from django.shortcuts import render
from rest_framework import generics
from push_notifications.models import APNSDevice
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q

# Create your views here.
class SendPushNotification(generics.CreateAPIView):
    
    def create(self, request, *args, **kwargs):
        if not request.user.admin:
            return super().permission_denied(self.request, message='You must be an admin to perform this action')
        queryset = APNSDevice.objects.all()
        if(request.data['admins'] == False):
            queryset = queryset.exclude(user__admin=True)
        if(request.data['members'] == False):
            queryset = queryset.exclude(user__email="guest@kiuc.coop")
        if(request.data['employees'] == False):
            queryset = queryset.exclude(
                ~Q(user__email="guest@kiuc.coop"),
                Q(user__admin=False)
            )
        if(request.data['newIssue']):
            queryset = queryset.exclude(user__newIssueNotifications=False)
        queryset.send_message(request.data['message'])
        return Response({},status.HTTP_200_OK)
