from utils.response import get_json_response
from django.views import View
from requests.exceptions import Timeout


class Balance(View):
    def get(self, request, stu, user):
        try:
            balance = stu.request('/https/77726476706e69737468656265737421fff944d22f367d44300d8db9d6562d/api/operation/thirdPartyApi/schoolcard/balance?sno=' + user.student_id).json()['data']
            return get_json_response({
                'balance': balance,
            })
        except Timeout:
            return get_json_response({
                'balance': '维护中'
            })
