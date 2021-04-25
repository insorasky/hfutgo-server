from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import reverse
from utils.response import get_json_response
from user.models import User
from datetime import datetime
from utils.Student import Student

url = [
    reverse('user_login'),
    reverse('others_notice'),
    reverse('index'),
]


class UserManageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path in url:
            return None
        else:
            if 'token' in request.GET:
                user = User.objects.filter(
                    user_token=request.GET['token']
                ).first()
                if not user:
                    return get_json_response('登录凭据无效', 1000)
                time_now = datetime.now()
                stu = Student(
                    ticket=user.vpn_ticket,
                    at_token=user.at_token
                )
                if (time_now - user.last_login).seconds > 1800:
                    if stu.is_login:
                        self.stu = stu
                        self.user = user
                    else:
                        return get_json_response('登录凭据失效', 1001)
                else:
                    self.stu = stu
                    self.user = user
            else:
                return get_json_response('token异常！', 1101)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path in url:
            return None
        else:
            view_kwargs['stu'] = self.stu
            view_kwargs['user'] = self.user
