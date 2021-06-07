from utils.response import get_json_response
from django.views import View


class Subscribe(View):
    def get(self, request, stu, user):
        subscribe_books = stu.request('/https/77726476706e69737468656265737421fff944d22f367d44300d8db9d6562d/api/operation/library/getSubscribeNum').json()['data']
        return get_json_response({
            'subscribe_books': subscribe_books,
        })
