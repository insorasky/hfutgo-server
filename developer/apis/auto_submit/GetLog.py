from django.views import View
from django.core.paginator import Paginator
from utils.response import get_json_response
from ...models import DakaLog


class GetLog(View):
    def get(self, request, stu, user):
        data = DakaLog.objects.filter(user=user.student_id).all().order_by('-time')
        page = Paginator(data, 20)
        response = []
        for item in page.page(int(request.GET['page'])).object_list:
            response.append({
                'time': item.time.strftime("%Y-%m-%d %H:%M:%S"),
                'log': item.log
            })
        return get_json_response(response)
