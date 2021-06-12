from django.views import View
from utils.response import get_json_response


class ResetPwd(View):
    def get(self, request, stu, user):
        data = stu.request('https://one.hfut.edu.cn/api/center/manage/user/update-mypwd', json={
            'newPassword': request.GET['new'],
            'oldPassword': request.GET['old'],
        }).json()
        if data['code'] == 1:
            return get_json_response({
                'result': True
            })
        else:
            return get_json_response({
                'result': False,
                'message': data['msg'],
            }, 3001)
