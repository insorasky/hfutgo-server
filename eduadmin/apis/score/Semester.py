from utils.response import get_json_response
from django.views import View
from bs4 import BeautifulSoup


class Semester(View):
    def get(self, request, stu):
        stu.request('http://jxglstu.hfut.edu.cn/eams5-student/neusoft-sso/login')
        data = stu.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/grade/sheet/').text
        soup = BeautifulSoup(data, 'lxml').select('#semester > option')
        response = []
        for option in soup:
            if option['value']:
                response.append({
                    'name': option.text,
                    'sid': option['value']
                })
        return get_json_response(response)
