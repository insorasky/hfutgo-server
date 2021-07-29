from django.urls import path
from .Info import Info
from .Semester import Semester
urlpatterns = [
    path('semester', Semester.as_view(), name='eduadmin_score_semester'),
    path('info', Info.as_view(), name='eduadmin_score_info'),
]
