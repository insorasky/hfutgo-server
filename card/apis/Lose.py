from utils.Request import Request, get_json_response
from bs4 import BeautifulSoup


class Lose(Request):
    def get(self, request):
        super(Lose, self).get(request)
        data = self.stu.request('http://172.31.248.20/accountDoLoss.action', method='POST', params={
                                   'account': request.GET['account_id'],
                                   'passwd': request.GET['password']
                               }).text
        data = BeautifulSoup(data, 'lxml').select('.biaotou')[0].text.strip()
        if '操作成功' in data:
            return get_json_response(data)
        else:
            return get_json_response(data, 3001)
