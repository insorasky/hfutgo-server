from django.views import View
from utils.response import get_json_response
from bs4 import BeautifulSoup


class Login(View):
    def get(self, request, stu, user):
        stu.request('http://jxglstu.hfut.edu.cn/eams5-student/neusoft-sso/login')
        if user.eduadmin_id is None:
            resp = stu.request(
                'http://jxglstu.hfut.edu.cn/eams5-student/for-std/grade/sheet/',
                allow_redirects=False
            )
            if 'Location' in resp.headers:
                stu_id = resp.headers['Location'].split('/')[-1]
            else:
                soup = BeautifulSoup(resp.text, parser='lxml')
                buttons = soup.select('.footer.btn.btn-info')
                stu_id = str(max(map(lambda b: int(b['value']), buttons)))
            user.eduadmin_id = stu_id
            user.save()
        return get_json_response({
            'id': user.eduadmin_id
        })
