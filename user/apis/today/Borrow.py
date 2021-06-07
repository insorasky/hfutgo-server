from utils.response import get_json_response
from django.views import View


class Borrow(View):
    def get(self, request, stu, user):
        borrow_books = stu.request('/https/77726476706e69737468656265737421fff944d22f367d44300d8db9d6562d/api/operation/library/getBorrowNum').json()['data']
        return get_json_response({
            'borrow_books': borrow_books,
        })
