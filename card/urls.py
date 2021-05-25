from django.urls import path
from . import apis
urlpatterns = [
    path('info', apis.Info.as_view(), name='card_info'),
    path('details_past', apis.DetailsPast.as_view(), name='card_details_past'),
    path('details_today', apis.DetailsToday.as_view(), name='card_details_today'),
    path('lose', apis.Lose.as_view(), name='card_lose'),
    path('old_index_code', apis.OldLoginCode.as_view(), name='card_old_index_code'),
    path('old_login', apis.OldLogin.as_view(), name='card_old_login'),
    path('old_lose_code', apis.OldLoseCode.as_view(), name='card_old_lose_code'),
    path('old_unlose', apis.OldFound.as_view(), name='card_old_found'),
]
