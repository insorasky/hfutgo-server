from django.urls import path
from .Schedules import Schedules
from .Semester import Semester
urlpatterns = [
    path('schedules', Schedules.as_view(), name='eduadmin_schedules'),
    path('semesters', Semester.as_view(), name='esuadmin_schedules_semester'),
]
