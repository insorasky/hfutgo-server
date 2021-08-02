from utils.response import get_json_response
from utils.Student import Student
from django.views import View
from ..models import User, LoginState
from others.models import Log
import json
import uuid


class Login(View):
    def get(self, request):
        student = Student()
        status = student.login(request.GET['id'], request.GET['password'])
        if status is True:
            token = uuid.uuid4()
            info = student.userinfo
            user, success = User.objects.update_or_create(
                defaults={
                    'name': info.name,
                    'organization': info.organization,
                    'type': info.type,
                },
                student_id=info.id
            )
            LoginState.objects.create(
                user_id=user.pk,
                student_id=user.student_id,
                type=1,
                token=token,
                vpn_ticket=student.vpn_token,
                at_token=student.at_token,
                available=True
            )
            Log.objects.create(
                user=info.id,
                path=request.path,
                params=json.dumps(request.GET),
                data={}
            )
            student.request('http://jxglstu.hfut.edu.cn/eams5-student/neusoft-sso/login')
            return get_json_response({
                'ticket': student.vpn_token,
                'at_token': student.at_token,
                'token': token,
                'class_name': info.organization,
                'name': info.name,
                'type': 'normal'
            })
        elif status == -2:
            return get_json_response({
                'code': status,
                'boss_ticket': student.boss_ticket,
                'ticket': student.vpn_token
            }, 3301)
        elif status == -1:
            return get_json_response("密码错误！", 3303)
        else:
            return get_json_response(status, 3302)
