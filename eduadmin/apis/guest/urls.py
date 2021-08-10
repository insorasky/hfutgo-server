from django.urls import path
from .ClassTable import ClassTable
from .ClassSearch import ClassSearch

urlpatterns = [
    path('class_table', ClassTable.as_view(), name='guest_table'),
    path('class_search', ClassSearch.as_view(), name='guest_class_search'),
]
