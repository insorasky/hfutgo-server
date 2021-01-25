from django.contrib import admin
from django.urls import path, include
from . import index
urlpatterns = [
    path('', index.index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('wash/', include('wash.urls'), name='wash'),
    path('sc/', include('secondclass.urls'), name='sc'),
    path('cas/', include('cas.urls'), name='cas')
]
