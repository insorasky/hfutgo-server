from django.contrib import admin
from django.urls import path, include
from . import index
urlpatterns = [
    path('', index.index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('wash/', include('wash.urls'), name='wash'),
    path('sc/', include('secondclass.urls'), name='sc'),
    path('cas/', include('cas.urls'), name='cas'),
    path('card/', include('card.urls'), name='card'),
    path('utils/', include('utils.urls'), name='utils'),
    path('library/', include('library.urls'), name='library')
]
