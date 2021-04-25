from utils.response import get_json_response
from django.views import View
from ..models import Notice as NoticeModel


class Notice(View):
    def get(self, request, stu):
        data = NoticeModel.objects.filter(page=request.GET['page'], show=True).order_by('-time').all()
        if len(data):
            response = []
            for dat in data:
                response.append(dat.text)
            return get_json_response({
                'theme': data[0].theme,
                'notices': response
            })
        else:
            return get_json_response({
                'theme': None,
                'notices': []
            })
