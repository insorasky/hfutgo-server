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
                'appid': 'wxa0cf6d472206fa8c',
                'secret': 'b08be86e5f5934f4d8e6356806f779a1',
                'js_code': request.GET['code'],
                'grant_type': 'authorization_code'
            }
        ).json()
        '''
        data = {
            'errcode': 0,
            'openid': 'testopenid' + request.GET['code'],
            'unionid': 'testunionid' + request.GET['code'],
            'errmsg': None
        }
        '''
        print(data)
        if ('errcode' not in data) or (data['errcode'] == 0):
            token = uuid.uuid4()
            openid = data['openid']
            session_key = data['session_key']
            guest, success = Guest.objects.update_or_create(
                defaults={
                    'nick_name': '',
                    'city': '',
                    'avatar': ''
                },
                openid=openid,
            )
            LoginState.objects.create(
                user_id=guest.pk,
                student_id=None,
                session_key=session_key,
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
