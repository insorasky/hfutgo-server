from django.urls import path, include
from . import apis
urlpatterns = [
    path('login', apis.login),
    path('is_login', apis.is_login),
    path('today', apis.today),
    path('newuser/', include('user.newuser'))
]