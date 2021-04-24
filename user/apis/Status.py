from utils.Request import Request, get_json_response


class Status(Request):
    def get(self, request):
        status = self.stu.is_login
        if status:
            info = self.stu.userinfo
            return get_json_response({
                'id': info['loginName'],
                'class': info['orgName'],
                'name': info['xm']
            })
        else:
            return get_json_response("登录状态已失效", 3303)
