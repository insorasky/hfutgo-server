from django.urls import path
from ..apis import newuser

urlpatterns = [
    path('get_phone_code', newuser.get_phone_code, name='get_phone_code'),
    path('get_email_code', newuser.get_email_code, name='get_email_code'),
    path('verify_email', newuser.verify_email, name='newuser_verify_email'),
    path('verify_phone', newuser.verify_phone, name='newuser_verify_phone'),
]
