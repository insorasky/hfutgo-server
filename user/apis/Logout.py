from utils.response import get_json_response
from django.views import View


class Logout(View):
    def get(self, request, stu, user, login_state):
        login_state.available = False
        login_state.save()
        return get_json_response('退出登录成功！')
