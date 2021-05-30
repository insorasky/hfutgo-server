from utils.response import get_json_response
from django.views import View
from ..request import sc_request


class Ranking(View):
    def get(self, request, stu, user):
        data = sc_request('POST', user.student_id, 'https://dekt.hfut.edu.cn/scReports/api/wx/range/student/score/',
                          json_data={'type': request.GET['type']})['data']
        response = []
        for dat in data:
            response.append({
                'id': dat['userId'],
                'name': dat['userName'],
                'rank': dat['rank'],
                'sum': dat['sumScore'],
                'data': [
                    {'title': '思政学习', 'score': dat['szxxNum']},
                    {'title': '科技创新', 'score': dat['kjcxNum']},
                    {'title': '体育健身', 'score': dat['tyjsNum']},
                    {'title': '公益服务', 'score': dat['gyfwNum']},
                    {'title': '社会实践', 'score': dat['shsjNum']},
                    {'title': '创业活动', 'score': dat['cyhdNum']},
                    {'title': '文艺活动', 'score': dat['wyhdNum']},
                    {'title': '社团活动', 'score': dat['sthdNum']},
                    {'title': '技能项目', 'score': dat['jnxmNum']}
                ]
            })
        return get_json_response(response)
