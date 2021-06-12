from django.views import View
from utils.response import get_json_response
from ...models import DakaUser


class Status(View):
    def get(self, request, stu, user):
        return get_json_response({
            'result': DakaUser.objects.filter(user=user.student_id, enable=True).exists()
        })
