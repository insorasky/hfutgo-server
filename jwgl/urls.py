from django.urls import path
from . import views
urlpatterns = [
    path('search', views.search, name='jwgl_search'),
]