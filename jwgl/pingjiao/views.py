from django.http import JsonResponse
from student import Student
from bs4 import BeautifulSoup
import json


def semester(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    student.request('http://jxglstu.hfut.edu.cn/eams5-student/neusoft-sso/login')
    data = student.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey').text
    soup = BeautifulSoup(data, 'lxml').select('#semester > option')
    response = []
    for option in soup:
        if option['value']:
            response.append({
                'name': option.text,
                'sid': option['value']
            })
    return JsonResponse({
        'data': response
    })


def subjects(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    stu_id = \
    student.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey', allow_redirects=False).headers[
        'Location'].split('/')[-1]
    data = student.request(
        'http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/%s/search/%s' % (
        request.GET['sid'], stu_id)).json()
    response = []
    for subject in data['forStdLessonSurveySearchVms']:
        tasks = []
        for task in subject['lessonSurveyTasks']:
            tasks.append({
                'id': task['id'],
                'teacher': task['teacher']['person']['nameZh'],
                'submitted': task['submitted']
            })
        period = subject['openEndTimeContent'].split('~')
        response.append({
            'class_id': subject['code'],
            'name': subject['course']['nameZh'],
            'period': {
                'start': period[0],
                'end': period[1]
            },
            'tasks': tasks
        })
    return JsonResponse({
        'data': response
    })


def questions(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    data = student.request(
        'http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/start-survey/%s/get-data' % request.GET['id'],
        headers={'Content-Type': 'application/json;charset=UTF-8'}).json()['survey']
    response = []
    for radio in data['radioQuestions']:
        response.insert(radio['indexNo'], {
            'type': 'radio',
            'data': radio
        })
    for blank in data['blankQuestions']:
        response.insert(blank['indexNo'], {
            'type': 'blank',
            'data': blank
        })
    for header in data['headers']:
        response.insert(header['indexNo'], {
            'type': 'header',
            'data': header
        })
    return JsonResponse({
        'data': response
    })


def submit(request):
    body = json.loads(request.body)
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    student.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/start-survey/' + str(
        body['lessonSurveyTaskAssoc']))
    data = student.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/check-can-submit',
                           method='POST',
                           data=body,
                           headers={
                               'Accept': 'application/json, text/javascript, */*; q=0.01',
                               'Content-Type': 'application/json'
                           }).json()
    if data['validateResult']['passed']:
        data = student.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/submit-survey',
                               method='POST',
                               data=body,
                               headers={
                                   'Accept': 'application/json, text/javascript, */*; q=0.01',
                                   'Content-Type': 'application/json'
                               }).json()
        if 'status' in data:
            return JsonResponse({
                'status': False,
                'message': data['message']
            })
        return JsonResponse({
            'status': data['success'],
            'message': data['content']
        })
    else:
        return JsonResponse({
            'status': False,
            'message': '数据检查未通过'
        })
