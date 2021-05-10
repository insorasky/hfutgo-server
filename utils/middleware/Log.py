from django.utils.deprecation import MiddlewareMixin
import json
from django.shortcuts import reverse
from others.models import Log

url = [
    '/user/login',
    '/others/notice',
    '/',
]


class LogMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path in url:
            return None
        else:
            Log.objects.create(
                user=view_kwargs['user'].student_id,
                path=request.path,
                params=json.dumps(request.GET),
            )
