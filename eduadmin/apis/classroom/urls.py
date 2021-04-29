from django.urls import path
from .EmptyRoom import EmptyRoom
from .Buildings import Buildings

urlpatterns = [
    path('empty', EmptyRoom.as_view(), 'empty_room'),
    path('buildings', Buildings.as_view(), 'room_buildings')
]
