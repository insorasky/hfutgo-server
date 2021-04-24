from utils.Request import get_json_response, Request


class VerifyEmail(Request):
    def get(self, request):
        data = self.stu.request('https://cas.hfut.edu.cn/cas/policy/loginInfoRecord',
                                params={
                                    'username': request.GET['username'],
                                    'mail': request.GET['email'],
                                    'verifCode': request.GET['code'],
                                    'type': 'mail',
                                    'authTicket': request.GET['boss_ticket']
                                }).json()
        return get_json_response(data['msg'], 200 if data['code'] else 3307)
