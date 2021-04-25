from utils.response import get_json_response
from django.views import View


class OldLogin(View):
    def get(self, request, stu, user):
        data = stu.request(
            '/http-8080/77726476706e69737468656265737421e0f4408e237e60566b1cc7a99c406d3657/login.action?'
            'username=%s&userpwd=%s&randcode=%s&usertype=2&logintype=2' % (
                user.card_id, request.GET['password'], request.GET['code'])).text
        if data == 'accloginok!':
            status = 200
            message = '登录成功'
        else:
            status = 3002
            message = data
        return get_json_response(message, status)
