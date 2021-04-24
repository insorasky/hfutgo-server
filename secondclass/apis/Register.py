from utils.Request import Request, get_json_response
from ..request import sc_request


class Register(Request):
    def get(self, request):
        userinfo = self.stu.userinfo
        data = sc_request('POST', userinfo['loginName'], 'https://dekt.hfut.edu.cn/scReports/api/wx/activedetail/enter/' + request.GET['id'])
        if data['data']:
            return get_json_response("报名成功")
        else:
            return get_json_response(data['errMsg'], 3208)
