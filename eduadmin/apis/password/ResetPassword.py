from django.views import View
from utils.response import get_json_response
from utils.CBCPkcs7 import CBCPkcs7
from urllib.parse import urlencode


class ResetPassword(View):
    def get(self, request, stu, user):
        key = stu.request('http://jxglstu.hfut.edu.cn/eams5-student/my/password-secret').text
        pwd = CBCPkcs7(key).encrypt(request.GET['password'])
        data = stu.request(
            url='http://jxglstu.hfut.edu.cn/eams5-student/my/updateAccount',
            method='POST',
            data=urlencode({
                'loginName': user.student_id,
                'password': pwd,
                'REDIRECT_URL': '/my/account'
            }).encode(),
            headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
            allow_redirects=False
        )
        if '/eams5-student/my/account' in data.headers['Location']:
            return get_json_response(True)
        else:
            return get_json_response('密码修改失败', 3002)
