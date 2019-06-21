from django.urls import path, include
from . import views
    
urlpatterns = [
    path('', views.EmployeeList.as_view()),
    path('<int:pk>/', views.EmployeeEdit.as_view()),

]