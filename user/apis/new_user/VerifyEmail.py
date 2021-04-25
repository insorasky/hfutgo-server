from utils.response import get_json_response
from django.views import View
from utils.Student import Student


class VerifyEmail(View):
    def get(self, request):
        stu = Student(request.GET['vpn_ticket'])
        data = stu.request('https://cas.hfut.edu.cn/cas/policy/loginInfoRecord',
                                params={
                                    'username': request.GET['username'],
                                    'mail': request.GET['email'],
                                    'verifCode': request.GET['code'],
                                    'type': 'mail',
                                    'authTicket': request.GET['boss_ticket']
                                }).json()
        return get_json_response(data['msg'], 200 if data['code'] else 3307)
