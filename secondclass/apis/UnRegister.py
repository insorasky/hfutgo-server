from utils.Request import Request, get_json_response
from ..request import sc_request


class UnRegister(Request):
    def get(self, request):
        userinfo = self.stu.userinfo
        data = sc_request('POST', userinfo['loginName'], 'https://dekt.hfut.edu.cn/scReports/api/wx/activedetail/cancellRegistration/' + request.GET['id'])
        if data['data']:
            return get_json_response("取消报名成功")
        else:
            return get_json_response("操作失败", 3209)
