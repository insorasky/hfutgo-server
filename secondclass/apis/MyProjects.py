from utils.response import get_json_response
from django.views import View
from ..request import sc_request


class MyProjects(View):
    def get(self, request, stu):
        urls = {
            'waiting': 'https://dekt.hfut.edu.cn/scReports/api/wx/item/getMyApplyItems/1/10000',
            'end': 'https://dekt.hfut.edu.cn/scReports/api/wx/item/getMyApplyItemsEnd/1/10000'
        }
        id = request.GET['id']
        data = sc_request('GET', id, 'https://dekt.hfut.edu.cn/scReports/api/wx/report/getUserScore')
        if data['code'] == '1005':
            return get_json_response("用户不存在", 3205)
        elif data['code'] == '200':
            if data['data']['userName'] == request.GET['name']:
                userinfo = sc_request('POST', id, urls[request.GET['type']])
                items = []
                if userinfo['count'] != 0:
                    for item in userinfo['list']:
                        items.append({
                            'id': item['id'],
                            'name': item['name'],
                            'organizer': item['organizer']
                        })
                return get_json_response(items)
            else:
                return get_json_response("学工号和姓名不对应", 3206)
        else:
            return get_json_response("未知错误", 3207)
