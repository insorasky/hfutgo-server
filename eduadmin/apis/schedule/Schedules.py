from utils.response import get_json_response
from .analyze import analyze
from django.views import View


class Schedules(View):
    def get(self, request, stu, user):
        data = stu.request(
            'http://jxglstu.hfut.edu.cn/eams5-student/for-std/course-table/get-data?bizTypeId=2&semesterId=%s&dataId=%s'
            % (request.GET['sid'], user.eduadmin_id)).json()
        lessons = []
        for lesson in data['lessons']:
            schedule_texts = lesson['scheduleText']['dateTimePlaceText']['text'].split('; \n')
            schedules = []
            for text in schedule_texts:
                schedules.append(analyze(text))
            teachers = []
            for teacher in lesson['teacherAssignmentList']:
                teachers.append({
                    'name': teacher['teacher']['person']['nameZh'],
                    'title': teacher['teacher']['title']['name']
                })
            lessons.append({
                'code': lesson['code'],
                'name': lesson['course']['nameZh'],
                'schedules': schedules,
                'classes': lesson['nameZh'],
                'credits': lesson['course']['credit'],
                'type': lesson['courseType'],
                'teachers': teachers
            })
        return get_json_response({
            'layout': data['timeTableLayoutId'],
            'last_week': data['weekIndices'][-1],
            'current_week': data['currentWeek'],
            'lessons': lessons
        })
