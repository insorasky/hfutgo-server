from django.urls import path
from .Schedules import Schedules
urlpatterns = [
    path('schedules', Schedules.as_view(), name='eduadmin_schedules')
]
