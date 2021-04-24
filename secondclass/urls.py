from django.urls import path
from .apis import *
urlpatterns = [
    path('score', Score.as_view(), name='sc_score'),
    path('ranking', Ranking.as_view(), name='sc_rank'),
    path('list', ProjectList.as_view(), name='sc_list'),
    path('info', ProjectInfo.as_view(), name='sc_info'),
    path('my_projects', MyProjects.as_view(), name='sc_my'),
    path('register', Register.as_view(), name='sc_reg'),
    path('unregister', UnRegister.as_view(), name='sc_unreg')
]
