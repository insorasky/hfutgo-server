from utils.response import get_json_response
from django.views import View
import requests


class Qie(View):
    def get(self, request):
        try:
            mid = requests.post(
                url='https://userapi.qiekj.com/goods/scan/v2',
                params={
                    'NQT': request.GET['NQT']
                },
                headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:84.0) Gecko/20100101 Firefox/84.0 '
                }
            ).json()
            if mid['code'] == 4000:
                return get_json_response({'status': '设备可能已被拆除但仍未更新'})
            mid = mid['data']['id']
            if len(mid) >= 15:
                data = requests.post('https://userapi.qiekj.com/machine/detail',
                                     params={
                                         'machineId': mid
                                     },
                                     headers={
                                         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:84.0) Gecko/20100101 '
                                                       'Firefox/84.0 '
                                     }).json()['data']
                if data['status'] == 1:
                    status = '空闲'
                elif data['status'] == 2:
                    status = '使用中，剩余%s秒' % data['remainTime']
                else:
                    status = '未知(%s)' % data['status']
            else:
                data = requests.post('https://userapi.qiekj.com/goods/normal/details',
                                     params={
                                         'goodsId': mid
                                     },
                                     headers={
                                         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:84.0) Gecko/20100101 '
                                                       'Firefox/84.0 '
                                     }).json()['data']
                if data['deviceErrorCode'] is None:
                    status = '空闲'
                elif data['deviceErrorCode'] == 2:
                    status = '使用中'
                else:
                    status = data['deviceErrorMsg']
            return get_json_response({
                'status': status
            })
        except:
            return get_json_response({
                'status': '未知'
            })
