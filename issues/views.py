from django.shortcuts import render, redirect
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from .models import Issue
from .serializers import IssueViewSerializer, IssueListSerializer, IssueSaveSerializer
from django.contrib.auth.models import User
from django.db.models import Q
from push_notifications.models import APNSDevice
from PIL import Image
import base64
import io

# Create your views here.
class IssueListCreate(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSaveSerializer

    def get(self, request, format=None):
        if request.user.email == "wattsappkauaiguest@kiuc.coop":
            return super().permission_denied(self.request, message='You must be an employee to perform this action')
        issues = Issue.objects.filter(resolved=False)
        serializer = IssueListSerializer(issues, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        pushqueryset = APNSDevice.objects.all()
        pushqueryset = pushqueryset.exclude(
           ~Q(user__email="wattsappkauaiguest@kiuc.coop"),
           Q(user__admin=False)
        )
        pushqueryset = pushqueryset.exclude(user__newIssueNotifications=False)
        pushqueryset.send_message("New Issue of type " + str(request.data['issueType']) + " has been posted!")
        
        imgdata = base64.b64decode(request.data['image'])
        image = Image.open(io.BytesIO(imgdata))
        image = image.resize((64, 64), Image.ANTIALIAS)
        image = image.rotate(-90)
        #image.save(self.image.path + '.thumbnail')
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")

        request.data['thumbnail'] = base64.b64encode(buffered.getvalue()).decode('UTF-8')
        response = super().create(request, *args, **kwargs)
        return response

class IssueListResolved(generics.ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueListSerializer

    def get(self, request, format=None):
        if request.user.email == "wattsappkauaiguest@kiuc.coop":
            return super().permission_denied(self.request, message='You must be an employee to perform this action')
        response = super().get(request, format)
        return response

class IssueViewUpdate(generics.RetrieveAPIView, generics.UpdateAPIView):
    serializer_class = IssueViewSerializer
    queryset = Issue.objects.all()

    def get(self, request, pk, format=None):
        if request.user.email == "wattsappkauaiguest@kiuc.coop":
            return super().permission_denied(self.request, message='You must be an employee to perform this action')
        response = super().get(request, pk, format)
        return response

    # Updating thumbnail will not work
    def update(self, request, pk, *args, **kwargs):
        if request.user.email == "wattsappkauaiguest@kiuc.coop":
            return super().permission_denied(self.request, message='You must be an employee to perform this action')
        if not request.user.admin and (len(request.data) > 1 or not 'resolved' in request.data):
            return super().permission_denied(self.request, message='You must be an admin to perform this action')
        
        return super().update(request, pk, *args, **kwargs)