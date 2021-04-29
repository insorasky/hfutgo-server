from utils.response import get_json_response
from django.views import View


class Schedules(View):
    def get(self, request, stu, user):
        data = stu.request(
            'http://jxglstu.hfut.edu.cn/eams5-student/for-std/course-table/get-data?bizTypeId=2&semesterId=%s&dataId=%s' % (user.eduadmin_id)).json()
