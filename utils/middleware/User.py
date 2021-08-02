from django.utils.deprecation import MiddlewareMixin
from utils.response import get_json_response
from user.models import User, LoginState
from datetime import datetime
from utils.Student import Student
from hfutgo.settings import DEBUG

url = [
    '/user/login',
    '/user/guest/login',
    '/others/notice',
    '/user/new_user/get_phone_code',
    '/user/new_user/get_email_code',
    '/user/new_user/verify_email',
    '/user/new_user/verify_phone',
    '/user/new_user/set_password',
    '/user/forgot/get_code',
    '/user/forgot/get_message',
    '/user/forgot/get_session',
    '/user/forgot/verify',
    '/user/forgot/reset',
    '/user/logout',
    '/wash/buildings',
    '/wash/machines',
    '/wash/qie',
    '/wash/haier',
    '/wash/ujing',
    '/',
]


class UserManageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path in url:
            return None
        else:
            token = None
            if DEBUG and 'token' in request.GET:
                token = request.GET['token']
            if token is None and 'token' in request.headers:
                token = request.headers['token']
            if token is None:
                return get_json_response('token异常！', 1101)
            login_state = LoginState.objects.filter(
                token=token
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


    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path in url:
            return None
        else:
            view_kwargs['stu'] = self.stu
            view_kwargs['user'] = self.user
            if request.path == '/user/logout':
                view_kwargs['login_state'] = self.login_state
