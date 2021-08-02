from django.urls import path, include
from .apis import *

urlpatterns = [
    path('search', Search.as_view(), name='eduadmin_search'),
    path('score/', include('eduadmin.apis.score.urls'), name='eduadmin_score'),
    path('evaluate/', include('eduadmin.apis.evaluate.urls'), name='eduadmin_evaluate'),
    # path('all_schedule/', include('eduadmin.apis.all_schedule.urls'), name='eduadmin_all_schedule'),
    path('roomboard/', include('eduadmin.apis.roomboard.urls'), name='eduadmin_roomboard'),
    path('schedule/', include('eduadmin.apis.schedule.urls'), name='eduadmin_schedule'),
    path('login', Login.as_view(), name='eduadmin_login'),
    path('exams', Exams.as_view(), name='eduadmin_exams'),
    path('score/', include('eduadmin.apis.score.urls'), name='eduadmin_score'),
    path('manager/', include('eduadmin.apis.manager.urls'), name='eduadmin_manager'),
    path('password/', include('eduadmin.apis.password.urls'), name='eduadmin_password'),
]
