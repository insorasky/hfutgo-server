from django.urls import path
from .apis import *

urlpatterns = [
    path('timetable', TimeTable.as_view(), name='others_timetable'),
    path('notice', Notice.as_view(), name='others_notice')
]
