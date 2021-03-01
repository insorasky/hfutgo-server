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
    stu_id = student.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey', allow_redirects=False).headers['Location'].split('/')[-1]
    data = json.loads(student.request(
        'http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/%s/search/%s' % (request.GET['sid'], stu_id)).text)
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
    data = json.loads(student.request(
        'http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/start-survey/%s/get-data' % request.GET['id'],
        headers={'Content-Type': 'application/json;charset=UTF-8'}).text)['survey']
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


"""
body = {
	"surveyAssoc": 4,
	"lessonSurveyTaskAssoc": 2708458,
	"radioQuestionAnswers": [{
		"questionId": "af569edb-b41a-4938-9506-e287cc9e999b",
		"optionName": "达到目标"
	}, {
		"questionId": "4c151e87-c9bd-4383-8d3d-3892a5247c5d",
		"optionName": "匹配"
	}, {
		"questionId": "987aa80d-1ebd-4d03-bc83-2dde3d96b40c",
		"optionName": "契合"
	}, {
		"questionId": "bfd7a6e5-3061-4937-9017-d20f7802acc8",
		"optionName": "认真"
	}, {
		"questionId": "eab05c1a-e27e-45f3-9bd2-c07bc0c782d4",
		"optionName": "能充分利用教材设计教学方案，并做好教学预设。"
	}, {
		"questionId": "7f7ee282-9080-4a76-92a2-8b43e25c5983",
		"optionName": "能合理地利用现代教育技术手段。"
	}, {
		"questionId": "a2f4ef5b-fd4e-43e8-88b7-996d56b65351",
		"optionName": "能合理地运用多种教学方法。"
	}, {
		"questionId": "81ae2f44-7079-4c51-8a14-aaa0b6842c95",
		"optionName": "能根据教学设计组织教学活动，并对学生进行有效引导 。"
	}, {
		"questionId": "3217ed5f-81a4-4888-b256-44bb5dfcacca",
		"optionName": "学生积极参与教学活动，较好地掌握所学知识和技能，并对其发展产生积极影响。"
	}, {
		"questionId": "ef0f7676-b7fe-4466-a557-d8436c3c9767",
		"optionName": "能根据学生对课堂内容的掌握情况，适当拓展与延伸专业知识，激发学生学习兴趣，并拓展学生的学习视野。"
	}],
	"blankQuestionAnswers": [{
		"questionId": "9641a52e-1c5e-4306-9466-21069e15f939",
		"content": ""
	}]
}
"""


def submit(request):
    body = json.loads(request.body)
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    student.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/start-survey/' + str(
        body['lessonSurveyTaskAssoc']))
    data = json.loads(student.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/check-can-submit',
                                      method='POST',
                                      data=body,
                                      headers={
                                          'Accept': 'application/json, text/javascript, */*; q=0.01',
                                          'Content-Type': 'application/json'
                                      }).text)
    if data['validateResult']['passed']:
        data = json.loads(
            student.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/submit-survey',
                            method='POST',
                            data=body,
                            headers={
                                'Accept': 'application/json, text/javascript, */*; q=0.01',
                                'Content-Type': 'application/json'
                            }).text)
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
