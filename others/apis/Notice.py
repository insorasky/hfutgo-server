from utils.Request import Request, get_json_response
from ..models import Notice as NoticeModel


class Notice(Request):
    def get(self, request):
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
