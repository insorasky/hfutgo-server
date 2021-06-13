from django.views import View
from utils.response import get_json_response
from ...models import DakaUser
from .auth import Daka


class Setup(View):
    def get(self, request, stu, user):
        user_filter = DakaUser.objects.filter(user=user.student_id)
        if user_filter.exists():
            if user_filter.get().enable:
                return get_json_response('该用户已存在！', 3001)
            else:
                if Daka(stu).login(user.student_id, request.GET['password']):
                    user_filter.update(
                        enable=True,
                        openid='',
                        password=request.GET['password'],
                    )
                    return get_json_response(True)
                else:
                    return get_json_response('密码错误或系统出错', 3001)
        else:
            if Daka(stu).login(user.student_id, request.GET['password']):
                DakaUser(
                    user=user.student_id,
                    openid='',
                    password=request.GET['password'],
                    enable=True
                ).save()
                return get_json_response(True)
            else:
                return get_json_response('密码错误或系统出错', 3002)
