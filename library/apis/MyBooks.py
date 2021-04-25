from utils.response import get_json_response
from django.views import View
from bs4 import BeautifulSoup


class MyBooks(View):
    def get(self, request, stu):
        stu.request('/http-8080/77726476706e69737468656265737421a2a611d2736526022a5ac7f9/reader/hwthau2.php')
        data = stu.request('/http-8080/77726476706e69737468656265737421a2a611d2736526022a5ac7f9/reader/book_lst.php').text
        soup = BeautifulSoup(data, 'lxml').select('.table_line > tr')
        response = []
        first = True
        for tr in soup:
            if first:
                first = False
                continue
            td = tr.select('td')
            print(td[1])
            response.append({
                'name': td[1].text,
                'starttime': td[2].text,
                'endtime': td[3].text,
                'marc': td[1].select('a')[0]['href'].split('marc_no=')[1]
            })
        return get_json_response(response)
