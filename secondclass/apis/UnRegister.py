from utils.response import get_json_response
from django.views import View
from ..request import sc_request


class UnRegister(View):
    def get(self, request, stu, user):
        data = sc_request('POST', user.student_id, 'https://dekt.hfut.edu.cn/scReports/api/wx/activedetail/cancellRegistration/' + request.GET['id'])
        if data['data']:
            return get_json_response("取消报名成功")
        else:
            return get_json_response("操作失败", 3209)
