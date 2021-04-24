from utils.Request import get_json_response, Request


class GetPhoneCode(Request):
    def get(self, request):
        data = self.stu.request('https://cas.hfut.edu.cn/cas/policy/sendVerifCode?username=%s&connectInfo=%s&type=phone' % (request.GET['username'], request.GET['phone'])).json()
        return get_json_response(data['msg'], 200 if data['data'] else 3305)
