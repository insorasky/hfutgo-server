from django.views import View
from utils.response import get_json_response
from ...models import DakaUser


class Setup(View):
    def get(self, request, stu, user):
        user_filter = DakaUser.objects.filter(user=user.student_id)
        if user_filter.exists():
            if user_filter.get().enable:
                return get_json_response('该用户已存在！', 3001)
            else:
                user_filter.update(
                    enable=True,
                    openid=request.GET['openid'],
                    password=request.GET['password'],
                )
                return get_json_response(True)
        else:
            DakaUser(
                user=user.student_id,
                openid=request.GET['openid'],
                password=request.GET['password'],
                enable=True
            ).save()
            return get_json_response(True)
