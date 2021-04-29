from django.views import View
from utils.response import get_json_response


class Buildings(View):
    def get(self, request, stu, user):
        data = stu.request('POST', 'http://172.31.241.31:9999/ecc/api/booking/listFilter').json()
        return get_json_response(data)
