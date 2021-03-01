from django.urls import path
from . import views
urlpatterns = [
    path('schedules', views.schedules, name='jwgl_schedules')
]
