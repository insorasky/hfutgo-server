from django.urls import path
from .Bkzs import Bkzs
from .OneNotice import OneNotice
urlpatterns = [
    path('bkzs', Bkzs.as_view(), name='bkzs_list'),
    path('one_notice', OneNotice.as_view(), name='one_notice_list')
]
