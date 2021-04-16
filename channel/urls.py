from django.urls import path, include
urlpatterns = [
    path('channels/', include('channel.channels.url'), name='channel_channels'),
    path('viewers/', include('channel.viewers.urls'), name='channel_viewers'),
    path('attachments/', include('channel.attachments.urls'), name='channel_attachments'),
]
