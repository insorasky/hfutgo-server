from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login),
    path('is_login', views.is_login),
    path('today', views.today)
]