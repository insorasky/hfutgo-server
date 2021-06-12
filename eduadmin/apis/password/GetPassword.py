from django.views import View
from bs4 import BeautifulSoup
from utils.response import get_json_response


class GetPassword(View):
    def get(self, request, stu, user):
        data = stu.request('http://jxglstu.hfut.edu.cn/eams5-student/my/account').text
        soup = BeautifulSoup(data, 'lxml')
        password = soup.find(id='plainPassword')['value']
        return get_json_response({
            'password': password
        })
