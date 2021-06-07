from django.urls import path
from .Balance import Balance
from .Borrow import Borrow
from .Subscribe import Subscribe
from .Email import Email

urlpatterns = [
    path('balance', Balance.as_view(), name='today_balance'),
    path('borrow', Borrow.as_view(), name='today_borrow'),
    path('subscribe', Subscribe.as_view(), name='today_subscribe'),
    path('email', Email.as_view(), name='today_email'),
]