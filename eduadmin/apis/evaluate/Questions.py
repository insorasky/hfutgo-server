from utils.response import get_json_response
from django.views import View


class Questions(View):
    def get(self, request, stu, user):
        data = stu.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/start-survey/%s/get-data' % request.GET['id'], headers={'Content-Type': 'application/json;charset=UTF-8'}).json()
        response = []
        for radio in data['survey']['radioQuestions']:
            response.insert(radio['indexNo'], {
                'type': 'radio',
                'data': radio
            })
        for blank in data['survey']['blankQuestions']:
            response.insert(blank['indexNo'], {
                'type': 'blank',
                'data': blank
            })
        for header in data['survey']['headers']:
            response.insert(header['indexNo'], {
                'type': 'header',
                'data': header
            })
        return get_json_response({
            'assoc': data['lessonSurveyLesson']['surveyAssoc'],
            'questions': response
        })
