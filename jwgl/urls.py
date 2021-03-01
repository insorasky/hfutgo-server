from django.urls import path, include
from . import views
urlpatterns = [
    path('search', views.search, name='jwgl_search'),
    path('score/', include('jwgl.score'), name='jwgl_score'),
    path('pingjiao/', include('jwgl.pingjiao'), name='jwgl_pingjiao'),
    path('exams', views.exams, name='jwgl_exams')
]
