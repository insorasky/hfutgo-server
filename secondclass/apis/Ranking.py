from utils.response import get_json_response
from django.views import View
from ..request import sc_request


class Ranking(View):
    def get(self, request):
        data = sc_request('POST', request.GET['id'], 'https://dekt.hfut.edu.cn/scReports/api/wx/range/student/score/',
                          json_data={'type': request.GET['type']})['data']
        response = []
        for dat in data:
            response.append({
                'id': dat['userId'],
                'name': dat['userName'],
                'rank': dat['rank'],
                'sum': dat['sumScore'],
                '思政学习': dat['szxxNum'],
                '科技创新': dat['kjcxNum'],
                '体育健身': dat['tyjsNum'],
                '公益服务': dat['gyfwNum'],
                '社会实践': dat['shsjNum'],
                '创业活动': dat['cyhdNum'],
                '文艺活动': dat['wyhdNum'],
                '社团活动': dat['sthdNum'],
                '技能项目': dat['jnxmNum']
            })
        return get_json_response(response)
