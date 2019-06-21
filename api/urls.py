from django.urls import include, path
from allauth.account import views

urlpatterns = [
    path('employees/', include('employees.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]