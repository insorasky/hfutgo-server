from django.views import View
from utils.response import get_json_response
import requests
from utils.Student import TICKET_NAME


class Reset(View):
    def get(self, request):
        data = requests.get(
            url='https://webvpn.hfut.edu.cn/http/77726476706e69737468656265737421f3f652d22f367d44300d8db9d6562d/cas/password/changePwd',
            cookies={TICKET_NAME: request.GET['vpn_ticket']},
            params={
                'ticket': request.GET['ticket'],
                'password': request.GET['password']
            }
        ).json()
        if data['code'] == 1:
            return get_json_response('修改成功！')
        else:
            return get_json_response(data['msg'], 3004)
