from utils.Request import Request, get_json_response
import requests
from others.models import Config


class Ujing(Request):
    def get(self, request):
        mid = request.GET['mid']
        token = Config.objects.filter(name='ujing_token').first().value['token']
        data = requests.post('https://phoenix.ujing.online:443/api/v1/devices/scanWasherCode',
                             json={'qrCode': mid},
                             headers={'Authorization': 'Bearer ' + token}
                             ).json()
        return get_json_response({
            'status': '空闲' if data['data']['result']['createOrderEnabled'] else '使用中'
        })
