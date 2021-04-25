from django.urls import path, include
urlpatterns = [
    path('channels/', include('channel.apis.channels.url'), name='channel_channels'),
    path('viewers/', include('channel.apis.viewers.urls'), name='channel_viewers'),
    path('attachments/', include('channel.apis.attachments.urls'), name='channel_attachments'),
]
