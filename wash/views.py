from django.http import JsonResponse
from .models import *
import requests
from utils.models import *


def qie(request):
    mid = request.GET['mid']
    if mid.len >= 15:
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
            status = '使用中，剩余' + data['remainTime'] + '秒'
        else:
            status = '未知'
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
    return JsonResponse({
        'status': status
    })


def haier(request):
    mid = request.GET['mid']
    ssid = request.GET['ssid']
    data = requests.get('https://www.saywash.com/saywash/WashCallApi/common/laundry/getDeviceInfo.api',
                        params={
                            'deviceQRCode': mid,
                            'ssid': ssid
                        }).json()['data']
    if data['status'] == 1:
        status = '空闲'
    elif data['status'] == 2:
        status = '使用中，剩余' + data['timeRemaining'] + '分钟'
    else:
        status = '未知'
    return JsonResponse({
        'status': status
    })


def ujing(request):
    mid = request.GET['mid']
    token = Util.objects.filter(name='ujing_token').first().value['token']
    data = requests.post('https://phoenix.ujing.online:443/api/v1/devices/scanWasherCode',
                         json={'qrCode': mid},
                         headers={'Authorization': 'Bearer ' + token}).json()
    return JsonResponse({
        'status': '空闲' if data['data']['result']['createOrderEnabled'] else '使用中'
    })


def buildings(request):
    query = Building.objects.filter(campus=request.GET['campus']).order_by('sort')
    data = []
    for building in query:
        data.append(building.name)
    return JsonResponse({'buildings': data})


def machines(request):
    query = Machine.objects.filter(building=request.GET['building']).order_by('sort')
    data = []
    for machine in query:
        data.append({
            'name': machine.name,
            'type': machine.type,
            'machineid': machine.machineid,
            'NQT': machine.NQT
        })
    return JsonResponse({'machines': data})
