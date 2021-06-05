from django.utils.deprecation import MiddlewareMixin
from utils.response import get_json_response
from user.models import User, LoginState
from datetime import datetime
from utils.Student import Student

url = [
    '/user/login',
    '/others/notice',
    '/user/new_user/get_phone_code',
    '/user/new_user/get_email_code',
    '/user/new_user/verify_email',
    '/user/new_user/verify_phone',
    '/user/forgot/get_code',
    '/user/forgot/get_message',
    '/user/forgot/get_session',
    '/user/forgot/verify',
    '/user/forgot/reset',
    '/',
]


class UserManageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(request.path)
        if request.path in url:
            return None
        else:
            if 'token' in request.headers:
                login_state = LoginState.objects.filter(
                    token=request.headers['token']
                ).first()
                if (not login_state) or (login_state.available is False):
                    return get_json_response('登录凭据无效', 1000)
                user = User.objects.get(pk=login_state.user_id)
                time_now = datetime.now()
                stu = Student(
                    ticket=login_state.vpn_ticket,
                    at_token=login_state.at_token
                )
                if (time_now - user.last_login).seconds > 1800:
                    if stu.is_login:
                        self.stu = stu
                        self.user = user
                    else:
                        login_state.available = False
                        return get_json_response('登录凭据失效', 1001)
                else:
                    self.stu = stu
                    self.user = user
                    self.login_state = login_state
            else:
                return get_json_response('token异常！', 1101)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path in url:
            return None
        else:
            view_kwargs['stu'] = self.stu
            view_kwargs['user'] = self.user
            if request.path == '/user/logout':
                view_kwargs['login_state'] = self.login_state
