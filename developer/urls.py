from django.urls import path, include

urlpatterns = [
    path('auto_submit/', include('developer.apis.auto_submit.urls'), name='dev_auto_submit'),
]
