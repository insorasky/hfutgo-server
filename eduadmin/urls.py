from django.urls import path, include
from .apis import *

urlpatterns = [
    path('search', Search.as_view(), name='eduadmin_search'),
    path('score/', include('eduadmin.apis.score.urls'), name='eduadmin_score'),
    path('evaluate/', include('eduadmin.apis.evaluate.urls'), name='eduadmin_evaluate'),
    path('login/', Login.as_view(), name='eduadmin_login'),
    path('exams', Exams.as_view(), name='eduadmin_exams'),
]
