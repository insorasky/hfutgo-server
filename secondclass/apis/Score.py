from utils.response import get_json_response
from django.views import View
from ..request import sc_request


class Score(View):
    def get(self, request, stu, user):
        data = sc_request('GET', user.student_id, 'https://dekt.hfut.edu.cn/scReports/api/wx/report/getUserScore')
        if data['code'] == '200':
            userinfo = sc_request('GET', user.student_id, 'https://dekt.hfut.edu.cn/scReports/api/wx/uc/userInfo')['data']
            return get_json_response({
                'class': userinfo['deptAndClassesName'],
                'data': [
                    {'title': '思政学习', 'score': data['data']['szxx']},
                    {'title': '科技创新', 'score': data['data']['kjcx']},
                    {'title': '体育健身', 'score': data['data']['tyjs']},
                    {'title': '公益服务', 'score': data['data']['gyfw']},
                    {'title': '社会实践', 'score': data['data']['shsj']},
                    {'title': '创业活动', 'score': data['data']['cyhd']},
                    {'title': '文艺活动', 'score': data['data']['wyhd']},
                    {'title': '社团活动', 'score': data['data']['sthd']},
                    {'title': '技能项目', 'score': data['data']['jnxm']},
                ],
                'hour': userinfo['serviceHour']
            })
        else:
            return get_json_response("未知错误", 3203)
