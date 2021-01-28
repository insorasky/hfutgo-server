from django.urls import path
from .views import *
urlpatterns = [
    path('semester', views.semester, name='jwgl_score_semester'),
    path('info', views.info, name='jwgl_score_info'),
]
