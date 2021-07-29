from utils.response import get_json_response
from bs4 import BeautifulSoup
from django.views import View


class Lose(View):
    def get(self, request, stu, user):
        data = stu.request('http://hfut-test.heppy.wang:7002/accountDoLoss.action', method='POST', params={
                                   'account': user.card_id,
                                   'passwd': request.GET['password']
                               }).text
        data = BeautifulSoup(data, 'lxml').select('.biaotou')[0].text.strip()
        if '操作成功' in data:
            return get_json_response(data)
        else:
            return get_json_response(data, 3001)
