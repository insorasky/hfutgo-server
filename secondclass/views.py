from django.http import JsonResponse as Json
import requests
import json


def sc(method, userid, url, params=None, json_data=None):
    headers = {'key_session': userid}
    if params is None:
        params = []
    if json_data is not None:
        headers.update({'Content-Type': 'application/json'})
        json_data = json.dumps(json_data)
    data = requests.request(method, url, params=params, headers=headers, data=json_data).text
    return json.loads(data)


def score(request):
    data = sc('GET', request.GET['id'], 'https://dekt.hfut.edu.cn/scReports/api/wx/report/getUserScore')
    if data['code'] == '1005':
        return Json({'code': -2})
    elif data['code'] == '200':
        if data['data']['userName'] == request.GET['name']:
            userinfo = sc('GET', request.GET['id'], 'https://dekt.hfut.edu.cn/scReports/api/wx/uc/userInfo')['data']
            return Json({
                'code': 1,
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
            return Json({
                'code': -1
            })
    else:
        return Json({
            'code': -3
        })


def rank(request):
    data = sc('POST', request.GET['id'], 'https://dekt.hfut.edu.cn/scReports/api/wx/range/student/score/',
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
    return Json({
        'code': 1,
        'data': response
    })


def projects(request):
    urls = {
            'applying': 'https://dekt.hfut.edu.cn/scReports/api/wx/item/getApplyingItemList/',
            'waiting': 'https://dekt.hfut.edu.cn/scReports/api/wx/item/getWaitItemList/',
            'end': 'https://dekt.hfut.edu.cn/scReports/api/wx/item/getEndItemList/'
    }
    data = sc('POST', request.GET['id'], urls[request.GET['type']] + '1/100000',
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
    return Json({
        'count': data['count'],
        'data': response
    })


def info(request):
    data = sc('POST', request.GET['id'], 'https://dekt.hfut.edu.cn/scReports/api/wx/activedetail/' + request.GET['pid'])
    print(data)
    if data['code'] != '200':
        return Json({
            'code': data['code']
        })
    else:
        return Json({
            'code': '200',
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
