from django.urls import path
from . import views
urlpatterns = [
    path('room_free', views.room_free, name='lib_room_free'),
    path('hot', views.hot, name='lib_hot'),
    path('book_search', views.book_search, name='lib_book_search'),
    path('book_info', views.book_info, name='lib_book_info'),
    path('my_books', views.my_books, name='lib_book_my'),
]
