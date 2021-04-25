from utils.response import get_json_response
from utils.Student import Student
from django.views import View
from ..models import User
from others.models import Log
import json
import uuid


class Login(View):
    def get(self, request):
        student = Student()
        status = student.login(request.GET['username'], request.GET['password'])
        if status is True:
            token = uuid.uuid4()
            info = student.userinfo
            user, success = User.objects.update_or_create(
                defaults={
                    'name': info.name,
                    'organization': info.organization,
                    'vpn_ticket': student.vpn_token,
                    'at_token': student.at_token,
                    'user_token': token,
                    'type': info.type,
                },
                student_id=info.id
            )
            Log.objects.create(
                user=info.id,
                path=request.path,
                params=json.dumps(request.GET),
                data={}
            )
            return get_json_response({
                'vpn_token': student.vpn_token,
                'at_token': student.at_token,
                'token': token,
                'class': info.organization,
                'name': info.name
            })
        elif status == -2:
            return get_json_response({
                'code': status,
                'boss_ticket': student.boss_ticket,
                'vpn_token': student.vpn_token
            }, 3301)
        else:
            return get_json_response(status, 3302)
