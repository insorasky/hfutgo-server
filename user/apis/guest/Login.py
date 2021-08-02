from django.views import View
from hfutgo.settings import WEIXIN_APPID, WEIXIN_SECRET
from utils.response import get_json_response
from user.models import LoginState, Guest
import requests
import uuid


class Login(View):
    def get(self, request):
        data = requests.get(
            url='https://api.weixin.qq.com/sns/jscode2session',
            params={
                'appid': WEIXIN_APPID,
                'secret': WEIXIN_SECRET,
                'js_code': request.GET['code'],
                'grant_type': 'authorization_code'
            }
        ).json()
        if data['errcode'] == 0:
            token = uuid.uuid4()
            openid = data['openid']
            unionid = data['unionid']
            guest, success = Guest.objects.update_or_create(
                defaults={
                    'unionid': unionid,
                    'nick_name': '',
                    'city': '',
                    'avatar': ''
                },
                openid=openid,
            )
            LoginState.objects.create(
                user_id=guest.pk,
                student_id=None,
                type=2,
                token=token,
                vpn_ticket="",
                at_token="",
                available=True
            )
            return get_json_response({
                'type': 'guest',
                'token': token
            })
        else:
            return get_json_response({
                'msg': data['errmsg']
            }, 3001)
