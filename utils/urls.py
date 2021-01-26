from django.urls import path
from . import views

urlpatterns = [
    path('timetable', views.timetable, name='utils_timetable'),
    path('notice', views.notice, name='utils_notice')
]
