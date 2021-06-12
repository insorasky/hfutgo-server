from django.urls import path
from .ResetPassword import ResetPassword
from .GetPassword import GetPassword


urlpatterns = [
    path('reset', ResetPassword.as_view(), name='eduadmin_resetpwd'),
    path('get', GetPassword.as_view(), name='eduadmin_getpwd'),
]
