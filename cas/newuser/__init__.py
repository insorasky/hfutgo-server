from django.urls import path
from . import views
urlpatterns = [
    path('get_phone_code', views.get_phone_code, name='get_phone_code'),
    path('get_email_code', views.get_email_code, name='get_email_code'),
    path('verify', views.verify, name='newuser_verify'),
]
