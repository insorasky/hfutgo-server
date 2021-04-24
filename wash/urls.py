from django.urls import path
from .apis import *
urlpatterns = [
    path('qie', Qie.as_view(), name='qie'),
    path('haier', Haier.as_view(), name='haier'),
    path('ujing', Ujing.as_view(), name='ujing'),
    path('buildings', Buildings.as_view(), name='buildings'),
    path('machines', Machines.as_view(), name='machines')
]
