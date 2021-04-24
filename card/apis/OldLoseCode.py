from utils.Request import Request, get_json_response
import base64


class OldLoseCode(Request):
    def get(self, request):
        super(OldLoseCode, self).get(request)
        data = self.stu.request(
            '/http-8080/77726476706e69737468656265737421e0f4408e237e60566b1cc7a99c406d3657/getCheckpic.action').content
        return get_json_response({
            'image': 'data:image/jpeg;base64,' + base64.b64encode(data).decode()
        })
