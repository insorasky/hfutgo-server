from django.urls import path
from . import bkzs
urlpatterns = [
    path('bkzs', bkzs.news_list, name='bkzs_list')
]
