from utils.Request import Request, get_json_response


class OldFound(Request):
    def get(self, request):
        super(OldFound, self).get(request)
        data = self.stu.request('/http-8080/77726476706e69737468656265737421e0f4408e237e60566b1cc7a99c406d3657/'
                               'accountunlose.action?account=%s&passwd=%s&captcha=%s' % (
                               request.GET['account_id'], request.GET['password'], request.GET['code'])).json()
        return get_json_response({
            'status': (data['error'] == '交易成功'),
            'message': data['error']
        })
