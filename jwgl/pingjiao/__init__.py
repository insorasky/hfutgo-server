from django.urls import path
from .views import *
urlpatterns = [
    path('semester', views.semester, name='score_pingjiao_semester'),
    path('subjects', views.subjects, name='score_pingjiao_subjects'),
    path('questions', views.questions, name='score_pingjiao_questions'),
    path('submit', views.submit, name='score_pingjiao_submit')
]
