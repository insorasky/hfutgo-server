from utils.response import get_json_response
from django.views import View
from utils.Student import Student


class SetPassword(View):
    def get(self, request):
        stu = Student(request.GET['vpn_ticket'])
        data = stu.request(
            url='https://cas.hfut.edu.cn/cas/password/updatePwd',
            method='GET',
            params={
                'username': request.GET['username'],
                'oldPwd': request.GET['old'],
                'newPwd': request.GET['new']
            }
        ).json()
        return get_json_response(data['msg'], 200 if data['data'] else 3305)
