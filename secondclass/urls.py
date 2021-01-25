from django.urls import path
from . import views
urlpatterns = [
    path('score', views.score, name='sc_score'),
    path('rank', views.rank, name='sc_rank'),
    path('list', views.projects, name='sc_list'),
    path('info', views.info, name='sc_info'),
    path('my_projects', views.my_projects, name='sc_my'),
    path('register', views.register, name='sc_reg'),
    path('unregister', views.unregister, name='sc_unreg')
]