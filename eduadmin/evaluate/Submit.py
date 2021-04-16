from student.StudentRequest import StudentRequest, get_json_response
import json


class Submit(StudentRequest):
    def get(self, request):
        super(Submit, self).get(request)
        body = json.loads(request.body)
        self.stu.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/start-survey/' + str(
            body['lessonSurveyTaskAssoc']))
        data = self.stu.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/check-can-submit',
                                method='POST',
                                data=body,
                                headers={
                                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                                    'Content-Type': 'application/json'
                                }).json()
        if data['validateResult']['passed']:
            data = self.stu.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/submit-survey',
                                    method='POST',
                                    data=body,
                                    headers={
                                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                                        'Content-Type': 'application/json'
                                    }).json()
            if 'status' in data:
                return get_json_response(data['message'], 3101)
            return get_json_response(data['content'], 3102)
        else:
            return get_json_response('数据检查未通过', 3103)
