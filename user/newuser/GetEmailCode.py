from utils.Request import get_json_response, Request


class GetEmailCode(Request):
    def get(self, request):
        data = self.stu.request('https://cas.hfut.edu.cn/cas/policy/sendVerifCode?username=%s&connectInfo=%s&type=email' % (request.GET['username'], request.GET['email'])).json()
        return get_json_response(data['msg'], 200 if data['data'] else 3306)
