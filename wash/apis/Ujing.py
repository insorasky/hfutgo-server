from utils.response import get_json_response
from django.views import View
import requests
from others.models import Config


class Ujing(View):
    def get(self, request, stu, user):
        mid = request.GET['mid']
        token = Config.objects.filter(name='ujing_token').first().value['token']
        data = requests.post('https://phoenix.ujing.online:443/api/v1/devices/scanWasherCode',
                             json={'qrCode': mid},
                             headers={'Authorization': 'Bearer ' + token}
                             ).json()
        return get_json_response({
            'status': '空闲' if data['data']['result']['createOrderEnabled'] else '使用中'
        })
