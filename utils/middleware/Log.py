from django.utils.deprecation import MiddlewareMixin
import json
from django.shortcuts import reverse
from user.models import User
from others.models import Log

url = [
    reverse('user_login'),
    reverse('others_notice'),
    reverse('index'),
]


class LogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path in url:
            return None
        else:
            user = User.objects.filter(
                user_token=request.GET['token']
            ).first()
            Log.objects.create(
                user=user.student_id,
                path=request.path,
                params=json.dumps(request.GET),
            )
