from django.contrib import admin
from django.urls import path, include
from . import index
urlpatterns = [
    path('', index.index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('wash/', include('wash.urls'), name='wash'),
    path('sc/', include('secondclass.urls'), name='sc'),
    path('user/', include('user.urls'), name='user'),
    path('card/', include('card.urls'), name='card'),
    path('others/', include('others.urls'), name='others'),
    path('library/', include('library.urls'), name='library'),
    path('eduadmin/', include('eduadmin.urls'), name='eduadmin'),
    path('channel/', include('channel.urls'), name='channel')
]
