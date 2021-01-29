from django.urls import path, include
from . import views
urlpatterns = [
    path('channels/', include('channel.channels'), name='channel_channels'),
    path('viewers/', include('channel.viewers'), name='channel_viewers'),
]
