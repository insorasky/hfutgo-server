from django.urls import path, include
from .apis import *
urlpatterns = [
    path('login', Login.as_view()),
    path('is_login', Status.as_view()),
    path('today', Today.as_view()),
    path('newuser/', include('user.newuser.urls'))
]