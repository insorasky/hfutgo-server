from django.urls import path
from .GetEmailCode import GetEmailCode
from .GetPhoneCode import GetPhoneCode
from .VerifyEmail import VerifyEmail
from .VerifyPhone import VerifyPhone
from .SetPassword import SetPassword

urlpatterns = [
    path('get_phone_code', GetPhoneCode.as_view(), name='get_phone_code'),
    path('get_email_code', GetEmailCode.as_view(), name='get_email_code'),
    path('verify_email', VerifyEmail.as_view(), name='verify_email'),
    path('verify_phone', VerifyPhone.as_view(), name='verify_phone'),
    path('set_password', SetPassword.as_view(), name='set_password'),
]
