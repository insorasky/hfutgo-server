from bs4 import BeautifulSoup
from django.views import View
from utils.response import get_json_response
import re

url_pattern = r'http[s]?:\/\/(?:[a-zA-Z]+)\.hfut\.edu\.cn\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'


class Article(View):
    def get(self, request, stu, user):
        if re.search(url_pattern, request.GET['url']):
            data = stu.request(request.GET['url'])
            if '无法访问此网站' in data.text:
                return get_json_response('无法访问此网站', 3552)
            soup = BeautifulSoup(data.content, 'lxml').body
            [s.extract() for s in soup.select('a, script, ul, li, button, input')]
            return get_json_response({
                'html': ''.join([str(s) for s in soup]),
                'text': re.sub('\n+', '\n', soup.get_text())
            })
        else:
            return get_json_response('URL不合法！', 3551)
