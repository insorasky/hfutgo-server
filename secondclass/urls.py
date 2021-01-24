from django.urls import path
from . import views
urlpatterns = [
    path('score', views.score, name='sc_score'),
    path('rank', views.rank, name='sc_rank'),
    path('list', views.projects, name='sc_list'),
    path('info', views.info, name='sc_info'),
]