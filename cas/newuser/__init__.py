from django.urls import path
from . import views

urlpatterns = [
    path('get_phone_code', views.get_phone_code, name='get_phone_code'),
    path('get_email_code', views.get_email_code, name='get_email_code'),
    path('verify_email', views.verify_email, name='newuser_verify_email'),
    path('verify_phone', views.verify_phone, name='newuser_verify_phone'),
]
