from utils.response import get_json_response
from django.views import View
from ..request import sc_request


class Check(View):
    def get(self, request, stu, user):
        data = sc_request('GET', request.GET['id'], 'https://dekt.hfut.edu.cn/scReports/api/wx/report/getUserScore')
        if data['code'] == '200':
            userinfo = sc_request('GET', request.GET['id'], 'https://dekt.hfut.edu.cn/scReports/api/wx/uc/userInfo')['data']
            return get_json_response({
                'classname': userinfo['deptAndClassesName'],
                'hour': userinfo['serviceHour']
            })
        else:
            return get_json_response({
                'classname': '未知',
                'hour': '未知'
            })
