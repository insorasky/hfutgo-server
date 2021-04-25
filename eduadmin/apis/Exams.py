from utils.response import get_json_response
from django.views import View
from bs4 import BeautifulSoup


class Exams(View):
    def get(self, request, stu):
        stu.request('http://jxglstu.hfut.edu.cn/eams5-student/neusoft-sso/login')
        data = stu.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/exam-arrange').text
        soup = BeautifulSoup(data, 'lxml').select('tbody > tr')
        response = []
        for tr in soup:
            td = tr.select('td')
            response.append({
                'name': td[0].text.strip(),
                'time': td[1].text,
                'room': td[2].text,
                'building': td[3].text,
                'campus': td[4].text
            })
        return get_json_response(response)
