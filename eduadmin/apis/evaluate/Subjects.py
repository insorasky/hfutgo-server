from utils.response import get_json_response
from django.views import View


class Subjects(View):
    def get(self, request, stu, user):
        data = stu.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/%s/search/%s' % (request.GET['sid'], user.eduadmin_id)).json()
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
        return get_json_response(response)
