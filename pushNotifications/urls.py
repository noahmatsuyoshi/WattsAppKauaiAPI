from rest_framework import generics
from . import views
from push_notifications.api.rest_framework import APNSDeviceViewSet, GCMDeviceViewSet
from django.urls import path

urlpatterns = [
    path('send/', views.SendPushNotification.as_view()),
    path('', APNSDeviceViewSet.as_view({
        'post': 'create'
    }))
] 