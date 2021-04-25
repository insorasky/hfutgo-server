from django.views import View
from utils.response import get_json_response


class Login(View):
    def get(self, request, stu, user):
        stu.request('http://jxglstu.hfut.edu.cn/eams5-student/neusoft-sso/login')
        if user.eduadmin_id is None:
            stu_id = stu.request(
                'http://jxglstu.hfut.edu.cn/eams5-student/for-std/grade/sheet/',
                allow_redirects=False
            ).headers['Location'].split('/')[-1]
            user.eduadmin_id = stu_id
            user.save()
        return get_json_response({
            'id': user.eduadmin_id
        })
