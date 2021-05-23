from utils.response import get_json_response
from django.views import View
from ..request import sc_request


class ProjectList(View):
    def get(self, request, stu, user):
        urls = {
            'applying': 'https://dekt.hfut.edu.cn/scReports/api/wx/item/getApplyingItemList/',
            'waiting': 'https://dekt.hfut.edu.cn/scReports/api/wx/item/getWaitItemList/',
            'end': 'https://dekt.hfut.edu.cn/scReports/api/wx/item/getEndItemList/'
        }
        data = sc_request('POST', user.student_id, urls[request.GET['type']] + request.GET['page'] + '/25',
                          json_data={
                              'deptIds': [],
                              'modules': [],
                              'campus': [],
                              'name': '',
                              'orderby': '0'
                          })
        response = []
        for dat in data['list']:
            response.append({
                'id': dat['id'],
                'name': dat['name'],
                'sponsor': dat['sponsor'],
                'organizer': dat['organizer'],
                'end': dat['endTime'],
                'applied': (dat['teamApplyNum'] if dat['applyWay'] else dat['personApplyNum']),
                'size': (dat['teamPeopleNum'] if dat['applyWay'] else dat['peopleNum']),
                'logo': dat['activePhoto']
            })
        return get_json_response({
            'count': data['count'],
            'data': response
        })
