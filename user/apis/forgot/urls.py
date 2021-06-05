from django.urls import path
from .GetCode import GetCode
from .Reset import Reset
from .Verify import Verify
from .GetMessage import GetMessage
from .GetSession import GetSession

urlpatterns = [
    path('get_code', GetCode.as_view(), name='forgot_get_code'),
    path('reset', Reset.as_view(), name='forgot_reset'),
    path('verify', Verify.as_view(), name='forgot_verify'),
    path('get_message', GetMessage.as_view(), name='forgot_get_message'),
    path('get_session', GetSession.as_view(), name='forgot_get_session'),
]