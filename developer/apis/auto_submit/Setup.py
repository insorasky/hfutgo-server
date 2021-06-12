from django.views import View
from utils.response import get_json_response
from ...models import DakaUser
from .auth import Daka
from hfutgo.settings import WEIXIN_APPID, WEIXIN_SECRET
import requests


class Setup(View):
    def get(self, request, stu, user):
        user_filter = DakaUser.objects.filter(user=user.student_id)
        wx = requests.get('https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % (WEIXIN_APPID, WEIXIN_SECRET, request.GET['code'])).json()
        if user_filter.exists():
            if user_filter.get().enable:
                return get_json_response('该用户已存在！', 3001)
            else:
                if Daka(stu).login(user.student_id, request.GET['password']):
                    user_filter.update(
                        enable=True,
                        openid=wx['openid'],
                        password=request.GET['password'],
                    )
                    return get_json_response(True)
                else:
                    return get_json_response('密码错误或系统出错', 3001)
        else:
            if Daka(stu).login(user.student_id, request.GET['password']):
                DakaUser(
                    user=user.student_id,
                    openid=wx['openid'],
                    password=request.GET['password'],
                    enable=True
                ).save()
                return get_json_response(True)
            else:
                return get_json_response('密码错误或系统出错', 3002)
