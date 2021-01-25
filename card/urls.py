from django.urls import path
from . import views
urlpatterns = [
    path('info', views.info, name='card_info'),
    path('details', views.details, name='card_details'),
    path('lose', views.lose, name='card_lose'),
    path('old_index_code', views.old_index_code, name='card_old_index_code'),
    path('old_login', views.old_login, name='card_old_login'),
    path('old_lose_code', views.old_lose_code, name='card_old_lose_code'),
    path('old_unlose', views.old_unlose, name='card_unlose'),
]
