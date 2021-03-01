from django.urls import path, include
from . import views
urlpatterns = [
    path('login', views.login),
    path('is_login', views.is_login),
    path('today', views.today),
    path('newuser/', include('cas.newuser'))
]