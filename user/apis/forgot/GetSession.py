import requests
from django.views import View
from utils.response import get_json_response
import base64
from utils.Student import TICKET_NAME


class GetSession(View):
    def get(self, request):
        session = requests.session()
        captcha = session.get('https://webvpn.hfut.edu.cn/http/77726476706e69737468656265737421f3f652d22f367d44300d8db9d6562d/cas/vercode?randomStr=HFUTGo').content
        return get_json_response({
            'captcha': 'data:image/jpeg;base64,%s' % base64.b64encode(captcha).decode(),
            'vpn_ticket': session.cookies[TICKET_NAME]
        })
