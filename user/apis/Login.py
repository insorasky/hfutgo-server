from utils.Request import get_json_response
from utils.Student import Student
from django.views import View


class Login(View):
    def get(self, request):
        student = Student()
        status = student.login(request.GET['username'], request.GET['password'])
        if status is True:
            info = student.userinfo
            return get_json_response({
                'vpn_token': student.vpn_token,
                'at_token': student.at_token,
                'class': info['orgName'],
                'name': info['xm']
            })
        elif status == -2:
            return get_json_response({
                'code': status,
                'boss_ticket': student.boss_ticket,
                'vpn_token': student.vpn_token
            }, 3301)
        else:
            return get_json_response(status, 3302)
