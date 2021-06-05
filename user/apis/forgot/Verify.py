from django.views import View
from utils.response import get_json_response
from utils.Student import TICKET_NAME
import requests


class Verify(View):
    def get(self, request):
        data = requests.get(
            url='https://webvpn.hfut.edu.cn/http/77726476706e69737468656265737421f3f652d22f367d44300d8db9d6562d/cas/password/getTicket?username=%s&strCode=%s&codeRandom=%s'
                % (request.GET['id'], request.GET['code'], request.GET['random']),
            cookies={TICKET_NAME: request.GET['vpn_ticket']}
        ).json()
        if data['code'] == 1:
            return get_json_response({
                'success': True,
                'boss_ticket': data['data']
            })
        else:
            return get_json_response('验证码错误！', 3002)
