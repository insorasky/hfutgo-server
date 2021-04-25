from utils.response import get_json_response
from django.views import View


class Status(View):
    def get(self, request, stu, user):
        status = stu.is_login
        if status:
            info = stu.userinfo
            return get_json_response({
                'id': info.id,
                'class': info.organization,
                'name': info.name
            })
        else:
            return get_json_response("登录状态已失效", 3303)
