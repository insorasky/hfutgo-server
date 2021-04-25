from urllib.parse import unquote
import time
from utils.response import get_json_response
from django.views import View


class Bkzs(View):
    def get(self, request, stu, user):
        token = stu.request('http://bkzs.hfut.edu.cn/f/ajax_get_csrfToken',
                            method='POST',
                            params={'n': '1'},
                            headers={
                                'X-Requested-With': 'XMLHttpRequest',
                                'X-Requested-Time': str(int(time.time() * 1000))
                            }).json()['data']
        data = stu.request('http://bkzs.hfut.edu.cn/f/newsCenter/ajax_article_view',
                           method='POST',
                           params={
                               'contentId': request.GET['id']
                           },
                           headers={
                               'Csrf-Token': token,
                               'X-Requested-Time': str(int(time.time() * 1000)),
                               'X-Requested-With': 'XMLHttpRequest'
                           }).json()
        attachments = []
        print(data['data']['article']['attachment'][0])
        for attachment in data['data']['article']['attachment']:
            attachments.append({
                'name': unquote(attachment).split('/')[-1].split('.')[0],
                'url': attachment
            })
        return get_json_response({
            'content': data['data']['article']['articleData']['content'],
            'attachment': attachments
        })
