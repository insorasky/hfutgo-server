from django.http import JsonResponse
from .models import *
import requests
import json


def qie(request):
    mid = request.GET['mid']
    data = json.loads(requests.post('https://userapi.qiekj.com/machine/detail',
                                    params={
                                        'machineId': mid
                                    },
                                    headers={
                                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:84.0) Gecko/20100101 Firefox/84.0'
                                    }).text)['data']
    if data['status'] == 1:
        status = '空闲'
    elif data['status'] == 2:
        status = '使用中，剩余' + data['remainTime'] + '秒'
    else:
        status = '未知'
    return JsonResponse({
        'status': status
    })


def haier(request):
    mid = request.GET['mid']
    ssid = request.GET['ssid']
    data = json.loads(requests.get('https://www.saywash.com/saywash/WashCallApi/common/laundry/getDeviceInfo.api',
                                   params={
                                       'deviceQRCode': mid,
                                       'ssid': ssid
                                   }).text)['data']
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
    data = json.loads(requests.get('https://u.zhinengxiyifang.cn/api/Devices/getDevicesByCode',
                                   params={'qrCode': 'http://weixin.qq.com/r/Ej8rM5LElM-rrdZQ92oA?uuid=' + mid}).text)['result']
    if data[0]['status'] == '0':
        status = '空闲'
    else:
        status = '使用中'
    return JsonResponse({
        'status': status
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
