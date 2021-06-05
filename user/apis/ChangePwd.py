from django.views import View
from utils.response import get_json_response
import json


class ChangePwd(View):
    def get(self, request, stu, user):
        data = stu.request(
            url='https://one.hfut.edu.cn/api/center/manage/user/update-mypwd',
            method='PUT',
            data=json.dumps({
                'oldPassword': request.GET['old'],
                'newPassword': request.GET['new']
            })
        ).json()
        if data['code'] == 1:
            return get_json_response('修改成功！')
        else:
            return get_json_response(data['msg'], 3005)
