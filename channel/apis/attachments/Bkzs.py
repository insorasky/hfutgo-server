from django.views import View
from django.http import HttpResponse


class Bkzs(View):
    def get(self, request, stu):
        data = stu.request('http://bkzs.hfut.edu.cn' + request.GET['url'])
        response = HttpResponse(data.content)
        response['Content-Type'] = data.headers['Content-Type']
        return response
