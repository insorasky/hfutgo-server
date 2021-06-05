from django.views import View
from utils.response import get_json_response
import requests


class GetMessage(View):
    def get(self, request):
        data = requests.get('https://webvpn.hfut.edu.cn/http/77726476706e69737468656265737421f3f652d22f367d44300d8db9d6562d/cas/password/getContactInfo?username=%s' % request.GET['id']).json()
        if data['code'] == 1:
            if data['data']['email'] is None or data['data']['phone'] is None:
                return get_json_response('预留信息无效，请尝试使用初始密码（身份证后6位）登录！', 3003)
            return get_json_response(data['data'])
        else:
            return get_json_response(data['msg'])
