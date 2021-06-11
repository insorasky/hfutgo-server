from .GetLog import GetLog
from .Setup import Setup
from .Stop import Stop
from django.urls import path

urlpatterns = [
    path('setup', Setup.as_view(), name='daka_setup'),
    path('stop', Stop.as_view(), name='daka_stop'),
    path('log', GetLog.as_view(), name='daka_log'),
]
