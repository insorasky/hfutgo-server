from utils.response import get_json_response
from bs4 import BeautifulSoup
from django.views import View


class BookInfo(View):
    def get(self, request, stu, user):
        data = stu.request('/http-8080/77726476706e69737468656265737421ffe7409f69386e456a468ca88d1b203b/opac/item.php?marc_no=' + request.GET['marc']).text
        soup = BeautifulSoup(data, 'lxml')
        information = []
        content = ''
        for dl in soup.select('.booklist'):
            title = dl.select('dt')[0].text
            info = dl.select('dd')[0].text
            if title == '电子资源:' or title == '' or title == '豆瓣简介：':
                continue
            if title == '提要文摘附注:':
                content = info
            else:
                information.append({
                    'title': title,
                    'value': info
                })
        available = []
        for tr in soup.select('.whitetext'):
            td = tr.select('td')
            if len(td) < 4:
                continue
            available.append({
                'bookno': td[0].text,
                'barcode': td[1].text,
                'place': td[3].text.strip(),
                'status': td[4].text
            })
        return get_json_response({
            'info': information,
            'content': content,
            'available': available
        })
