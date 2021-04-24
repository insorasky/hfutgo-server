from utils.Request import Request, get_json_response
from ..request import sc_request


class ProjectList(Request):
    def get(self, request):
        urls = {
            'applying': 'https://dekt.hfut.edu.cn/scReports/api/wx/item/getApplyingItemList/',
            'waiting': 'https://dekt.hfut.edu.cn/scReports/api/wx/item/getWaitItemList/',
            'end': 'https://dekt.hfut.edu.cn/scReports/api/wx/item/getEndItemList/'
        }
        data = sc_request('POST', request.GET['id'], urls[request.GET['type']] + '1/100000',
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