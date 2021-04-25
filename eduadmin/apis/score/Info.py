from utils.response import get_json_response
from bs4 import BeautifulSoup
from django.views import View


class Info(View):
    def get(self, request, stu, user):
        data = stu.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/grade/sheet/info/%s?semester=%s' % (user.eduadmin_id, request.GET['sid'])).text
        soup = BeautifulSoup(data.replace('<br />', '\n'), 'lxml').select('tbody > tr')
        response = []
        for tr in soup:
            td = tr.select('td')
            details = []
            for line in td[6].text.splitlines():
                detail = line.strip().split(':')
                details.append({
                    'name': detail[0],
                    'score': detail[1]
                })
            response.append({
                'name': td[0].text,
                'subject_id': td[1].text,
                'class_id': td[2].text,
                'mark': td[3].text,
                'point': td[4].text,
                'score': td[5].text,
                'details': details
            })
        return get_json_response(response)
