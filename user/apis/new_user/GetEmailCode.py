from utils.response import get_json_response
from django.views import View
from utils.Student import Student


class GetEmailCode(View):
    def get(self, request):
        stu = Student(request.GET['vpn_ticket'])
        data = stu.request('https://cas.hfut.edu.cn/cas/policy/sendVerifCode?username=%s&connectInfo=%s&type=email' % (request.GET['username'], request.GET['email'])).json()
        return get_json_response(data['msg'], 200 if data['data'] else 3306)
