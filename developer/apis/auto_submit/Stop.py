from django.views import View
from utils.response import get_json_response
from ...models import DakaUser


class Stop(View):
    def get(self, request, stu, user):
        user_filter = DakaUser.objects.filter(user=user.student_id, enable=True)
        if user_filter.exists():
            user_filter.update(enable=False)
            return get_json_response(True)
        else:
            return get_json_response('找不到用户！', 3002)
