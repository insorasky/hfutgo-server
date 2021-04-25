from utils.response import get_json_response
from django.views import View
from ..request import sc_request


class Score(View):
    def get(self, request, stu, user):
        data = sc_request('GET', user.student_id, 'https://dekt.hfut.edu.cn/scReports/api/wx/report/getUserScore')
        if data['code'] == '200':
            userinfo = \
                sc_request('GET', request.GET['id'], 'https://dekt.hfut.edu.cn/scReports/api/wx/uc/userInfo')[
                    'data']
            return get_json_response({
                'class': userinfo['deptAndClassesName'],
                'data': {
                    '思政学习': data['data']['szxx'],
                    '科技创新': data['data']['kjcx'],
                    '体育健身': data['data']['tyjs'],
                    '公益服务': data['data']['gyfw'],
                    '社会实践': data['data']['shsj'],
                    '创业活动': data['data']['cyhd'],
                    '文艺活动': data['data']['wyhd'],
                    '社团活动': data['data']['sthd'],
                    '技能项目': data['data']['jnxm'],
                    '志愿服务时长': userinfo['serviceHour']
                }
            })
        else:
            return get_json_response("未知错误", 3203)
