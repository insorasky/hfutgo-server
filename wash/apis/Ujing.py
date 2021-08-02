from utils.response import get_json_response
from django.views import View
import requests
from others.models import Config


class Ujing(View):
    def get(self, request):
        try:
            mid = request.GET['mid']
            token = Config.objects.filter(name='ujing_token').first().value['token']
            data = requests.post('https://phoenix.ujing.online:443/api/v1/devices/scanWasherCode',
                                 json={'qrCode': mid},
                                 headers={'Authorization': 'Bearer ' + token}
                                 ).json()
            if 'reason' in data['data']['result']:
                return get_json_response({
                    'status': data['data']['result']['reason']
                })
            return get_json_response({
                'status': '空闲' if data['data']['result']['createOrderEnabled'] else '使用中'
            })
        except:
            return get_json_response({
                'status': '未知'
            })
