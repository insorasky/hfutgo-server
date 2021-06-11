from django.views import View
from django.core.paginator import Paginator
from utils.response import get_json_response
from ...models import DakaLog


class GetLog(View):
    def get(self, request, stu, user):
        data = DakaLog.objects.filter(user=user.student_id).all()
        page = Paginator(data, 20)
        return get_json_response(page.page(int(request.GET['page'])).object_list.value())
