from django.urls import path
from . import views
urlpatterns = [
    path('qie', views.qie, name='qie'),
    path('haier', views.haier, name='haier'),
    path('ujing', views.ujing, name='ujing'),
    path('buildings', views.buildings, name='buildings'),
    path('machines', views.machines, name='machines')
]