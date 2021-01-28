from django.http import JsonResponse
from student import Student
import json


def login(request):
    student = Student()
    status = student.login(request.GET['username'], request.GET['password'])
    if status is True:
        info = student.userinfo
        return JsonResponse({
            'code': 200,
            'vpn_token': student.vpn_token,
            'at_token': student.at_token,
            'class': info['orgName'],
            'name': info['xm']
        })
    elif status == -2:
        return JsonResponse({
            'code': status,
            'boss_ticket': student.boss_ticket
        })
    else:
        return JsonResponse({
            'code': status
        })


def is_login(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    status = student.is_login
    if status:
        info = student.userinfo
        return JsonResponse({
            'status': True,
            'stuid': info['loginName'],
            'class': info['orgName'],
            'name': info['xm']
        })
    else:
        return JsonResponse({
            'status': False
        })


def today(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    info = student.userinfo
    balance = json.loads(student.request('/https/77726476706e69737468656265737421fff944d22f367d44300d8db9d6562d/api/operation/thirdPartyApi/schoolcard/balance?sno=' + info['loginName']).text)['data']
    borrow_books = json.loads(student.request('/https/77726476706e69737468656265737421fff944d22f367d44300d8db9d6562d/api/operation/library/getBorrowNum').text)['data']
    subscribe_books = json.loads(student.request('/https/77726476706e69737468656265737421fff944d22f367d44300d8db9d6562d/api/operation/library/getSubscribeNum').text)['data']
    emails = json.loads(student.request('/https/77726476706e69737468656265737421fff944d22f367d44300d8db9d6562d/api/center/user/getBindMailList').text)['data']
    unread_email = 0
    for email in emails:
        unread_email += json.loads(student.request('/https/77726476706e69737468656265737421fff944d22f367d44300d8db9d6562d/api/msg/mailBusiness/getUnreadMsg?mail=' + email['mail']).text)['data']
    return JsonResponse({
        'balance': balance,
        'borrow_books': borrow_books,
        'subscribe_books': subscribe_books,
        'unread_email': unread_email
    })
