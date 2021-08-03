from utils.response import get_json_response
from django.views import View


class OneNotice(View):
    def get(self, request, stu, user):
        data = stu.request('https://one.hfut.edu.cn/api/operation/newsDetails/getPageData?type=notification&size=%s&current=%s' % (request.GET['size'], request.GET['page'])).json()
        response = []
        for item in data['data']['records']:
            response.append({
                'url': item['url'],
                'title': item['title']
            })
        return get_json_response(response)
