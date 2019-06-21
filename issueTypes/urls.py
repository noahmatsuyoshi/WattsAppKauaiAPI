from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('', views.IssueTypesView.as_view()),
    path('<int:pk>/', views.IssueTypesView.as_view()),
]