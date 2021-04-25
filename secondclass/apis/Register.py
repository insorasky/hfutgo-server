from utils.response import get_json_response
from django.views import View
from ..request import sc_request


class Register(View):
    def get(self, request, stu):
        userinfo = stu.userinfo
        data = sc_request('POST', userinfo.id, 'https://dekt.hfut.edu.cn/scReports/api/wx/activedetail/enter/' + request.GET['id'])
        if data['data']:
            return get_json_response("报名成功")
        else:
            return get_json_response(data['errMsg'], 3208)
