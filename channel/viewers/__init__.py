from django.urls import path
from . import bkzs
urlpatterns = [
    path('bkzs', bkzs.content, name='bkzs_content'),
    path('bkzs_attachment', bkzs.attachment, name='bkzs_attachment'),
]
