from utils.response import get_json_response
from django.views import View
import json


class Submit(View):
    def post(self, request, stu, user):
        body = json.loads(request.body)
        stu.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/start-survey/' + str(
            body['lessonSurveyTaskAssoc']))
        data = stu.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/check-can-submit',
                           method='POST',
                           json=body,
                           headers={
                               'Accept': 'application/json, text/javascript, */*; q=0.01',
                               'Content-Type': 'application/json'
                           }).json()
        if data['validateResult']['passed']:
            data = stu.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/submit-survey',
                               method='POST',
                               json=body,
                               headers={
                                   'Accept': 'application/json, text/javascript, */*; q=0.01',
                                   'Content-Type': 'application/json'
                               }).json()
            if 'status' in data:
                return get_json_response(data['message'], 3101)
            return get_json_response(data['content'])
        else:
            return get_json_response('数据检查未通过', 3103)
