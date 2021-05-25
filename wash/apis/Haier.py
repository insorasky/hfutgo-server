from utils.response import get_json_response
from django.views import View
import requests


class Haier(View):
    def get(self, request, stu, user):
        mid = request.GET['mid']
        ssid = request.GET['ssid']
        data = requests.get('https://www.saywash.com/saywash/WashCallApi/common/laundry/getDeviceInfo.api',
                            params={
                                'deviceQRCode': mid,
                                'ssid': ssid
                            }).json()
        if 'data' not in data:
            return get_json_response({'status': data['retInfo']})
        data = data['data']
        if data['status'] == '1':
            status = '空闲'
        elif data['status'] == '2' or data['status'] == '3':
            status = '使用中，剩余' + data['timeRemaining'] + '分钟'
        elif data['status'] == '7':
            status = '设备离线'
        else:
            status = '未知(%s)' % data['status']
        return get_json_response({
            'status': status
        })
