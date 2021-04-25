from utils.response import get_json_response
from django.views import View
import base64


class OldLoginCode(View):
    def get(self, request, stu, user):
        data = stu.request(
            '/http-8080/77726476706e69737468656265737421e0f4408e237e60566b1cc7a99c406d3657/code.jsp').content
        return get_json_response({
            'image': 'data:image/jpeg;base64,' + base64.b64encode(data).decode()
        })
