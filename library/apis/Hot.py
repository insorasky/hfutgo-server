from utils.Request import Request, get_json_response
from bs4 import BeautifulSoup


class Hot(Request):
    def get(self, request):
        data = self.stu.request(
            '/http-8080/77726476706e69737468656265737421a2a611d2736526022a5ac7f9/opac/ajax_top_lend_shelf.php').text
        soup = BeautifulSoup(data, 'lxml').select('ul')
        borrow_list = []
        for li in soup[0].select('li'):
            borrow_list.append({
                'title': li.text,
                'marc': li.select('a')[0]['href'].split('=')[1]
            })
        book_list = []
        for li in soup[1].select('li'):
            book_list.append({
                'title': li.text,
                'marc': li.select('a')[0]['href'].split('=')[1]
            })
        return get_json_response({
            'borrow_list': borrow_list,
            'book_list': book_list
        })
