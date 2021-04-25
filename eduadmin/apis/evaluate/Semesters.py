from utils.response import get_json_response
from bs4 import BeautifulSoup
from django.views import View


class Semesters(View):
    def get(self, request, stu, user):
        data = stu.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey').text
        soup = BeautifulSoup(data, 'lxml').select('#semester > option')
        response = []
        for option in soup:
            if option['value']:
                response.append({
                    'name': option.text,
                    'sid': option['value']
                })
        return get_json_response(response)
