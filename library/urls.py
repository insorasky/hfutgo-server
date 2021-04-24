from django.urls import path
from .apis import *
urlpatterns = [
    path('room_free', FreeRooms.as_view(), name='lib_room_free'),
    path('hot', Hot.as_view(), name='lib_hot'),
    path('book_search', Search.as_view(), name='lib_book_search'),
    path('book_info', BookInfo.as_view(), name='lib_book_info'),
    path('my_books', MyBooks.as_view(), name='lib_book_my'),
]
