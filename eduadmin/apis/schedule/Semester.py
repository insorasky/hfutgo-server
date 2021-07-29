from utils.response import get_json_response
from django.views import View
from bs4 import BeautifulSoup


class Semester(View):
    def get(self, request, stu, user):
        data = stu.request(
            url='http://jxglstu.hfut.edu.cn/eams5-student/for-std/course-table/info/%s' % user.eduadmin_id,
            headers={
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache'
            }
        ).text
        soup = BeautifulSoup(data, 'lxml').select('#allSemesters > option')
        response = []
        default = 0
        for option in soup:
            if option['value']:
                response.append({
                    'name': option.text,
                    'sid': option['value'],
                    'default': 'selected' in option.attrs
                })
                if 'selected' in option.attrs:
                    default = option['value']
        return get_json_response({
            'default': default,
            'semesters': response
        })
