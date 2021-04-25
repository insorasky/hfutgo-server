from utils.response import get_json_response
from django.views import View
from ..request import sc_request


class ProjectInfo(View):
    def get(self, request, stu):
        data = sc_request('POST', request.GET['id'], 'https://dekt.hfut.edu.cn/scReports/api/wx/activedetail/' + request.GET['pid'])
        if data['code'] != '200':
            return get_json_response("未知错误：%s" % data['code'], 3204)
        else:
            return get_json_response({
                'name': data['data']['name'],
                'module': data['data']['module'],
                'form': data['data']['form'],
                'level': data['data']['activityLevel'],
                'category': data['data']['category'],
                'tag': data['data']['label'],
                'campus': data['data']['campus'],
                'createtime': data['data']['ct'],
                'applystart': data['data']['st'],
                'applyend': data['data']['et'],
                'projectstart': data['data']['lectureStartTime'],
                'projectend': data['data']['lectureEndTime'],
                'location': data['data']['theVenue'],
                'sponsor': data['data']['sponsor'],
                'organizer': data['data']['organizer'],
                'teacher': data['data']['teacher'],
                'phone': data['data']['phone'],
                'goal': '德' + data['data']['virtue'] + '% 智' + data['data']['wisdom'] + '% 体' + data['data']['body'] + '% 美' + data['data']['beauty'] + '% 劳' + data['data']['work'] + '%',
                'applyway': ('团队报名' if data['data']['applyWay'] else '个人报名'),
                'applynum': (data['data']['bmTeamNum'] if data['data']['applyWay'] else data['data']['bmNum']),
                'fullnum': (data['data']['teamNum'] if data['data']['applyWay'] else data['data']['peopleNum']),
                'teamsize': (data['data']['teamSize'] if data['data']['applyWay'] else None),
                'content': data['data']['content']
            })
