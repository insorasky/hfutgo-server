from utils.response import get_json_response
from django.views import View


class Questions(View):
    def get(self, request, stu, user):
        data = stu.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/start-survey/%s/get-data' % request.GET['id'], headers={'Content-Type': 'application/json;charset=UTF-8'}).json()['survey']
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
        return get_json_response(response)
