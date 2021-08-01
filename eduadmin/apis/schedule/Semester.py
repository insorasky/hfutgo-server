from utils.response import get_json_response
from django.views import View
from bs4 import BeautifulSoup
import re
import json


class Semester(View):
    def get(self, request, stu, user):
        data = stu.request(
            url='http://jxglstu.hfut.edu.cn/eams5-student/for-std/course-table/info/%s' % user.eduadmin_id,
            headers={
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache'
            }
        ).text
        s = BeautifulSoup(data, 'lxml')
        soup = s.select('#allSemesters > option')
        response = []
        default = 0
        for option in soup:
            if option['value']:
                response.append({
                    'label': option.text,
                    'value': option['value'],
                    'default': 'selected' in option.attrs
                })
                if 'selected' in option.attrs:
                    default = option['value']
        details = json.loads(re.search(r'JSON.parse\(([\s\S]*?)\);', str(s.html))[1].replace('\'', '').replace('\\"', '"'))
        return get_json_response({
            'default': default,
            'semesters': response,
            'details': {item['id']: item for item in details}
        })
