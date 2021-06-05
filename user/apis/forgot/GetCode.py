from django.views import View
from utils.response import get_json_response
import requests
from utils.Student import TICKET_NAME, USER_AGENT


class GetCode(View):
    def get(self, request):
        data = requests.get(
            url='https://webvpn.hfut.edu.cn/http/77726476706e69737468656265737421f3f652d22f367d44300d8db9d6562d/cas/message/sendCode?username=%s&contactType=%s&strCode=%s&randomStr=HFUTGo'
                % (request.GET['id'], request.GET['type'], request.GET['captcha']),
            cookies={TICKET_NAME: request.GET['vpn_ticket']}
        ).json()
        if data['code'] == 1:
            return get_json_response({
                'success': True,
                'random': data['data']['codeRandom']
            })
        else:
            return get_json_response(data['msg'], 3001)
