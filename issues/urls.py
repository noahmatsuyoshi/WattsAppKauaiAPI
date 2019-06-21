from django.urls import path, include
from . import views
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register('issues', views.IssueView)

urlpatterns = [
    path('', views.IssueListCreate.as_view()),
    path('resolved/', views.IssueListResolved.as_view()),
    path('<int:pk>/', views.IssueViewUpdate.as_view()),
] 