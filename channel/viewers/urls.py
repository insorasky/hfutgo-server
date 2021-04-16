from django.urls import path
from .Bkzs import Bkzs
urlpatterns = [
    path('bkzs', Bkzs.as_view(), name='bkzs_content'),
]
