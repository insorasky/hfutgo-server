from utils.response import get_json_response
from django.views import View
from utils.Student import Student


class VerifyPhone(View):
    def get(self, request):
        stu = Student(request.GET['vpn_ticket'])
        data = stu.request('https://cas.hfut.edu.cn/cas/policy/loginInfoRecord',
                                params={
                                    'username': request.GET['username'],
                                    'phoneNumber': request.GET['phone'],
                                    'verifCode': request.GET['code'],
                                    'type': 'phone',
                                    'authTicket': request.GET['boss_ticket']
                                }).json()
        return get_json_response(data['msg'], 200 if data['code'] else 3308)
