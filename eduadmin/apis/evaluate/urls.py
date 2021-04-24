from django.urls import path
from .Submit import Submit
from .Subjects import Subjects
from .Questions import Questions
from .Semesters import Semesters
urlpatterns = [
    path('semesters', Semesters.as_view(), name='score_evaluate_semesters'),
    path('subjects', Subjects.as_view(), name='score_evaluate_subjects'),
    path('questions', Questions.as_view(), name='score_evaluate_questions'),
    path('submit', Submit.as_view(), name='score_evaluate_submit')
]
