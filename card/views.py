from django.http import JsonResponse
from student import Student
from bs4 import BeautifulSoup
import re
import datetime
import base64


def info(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    student.request('/http/77726476706e69737468656265737421a1a013d2746126022a50c7fec8/ahdxdrPortalHome.action')
    data = student.request(
        '/http/77726476706e69737468656265737421a1a013d2746126022a50c7fec8/accountcardUser.action').text
    soup = BeautifulSoup(data, 'lxml').select('.tttt > tr:nth-child(1) > th:nth-child(1) > table:nth-child(1)')[0]
    balance_text = soup.select('tr:nth-child(12) > td:nth-child(2)')[0].text
    balance_data = re.match(r'(.*)元（卡余额）(.*)元\(当前过渡余额\)(.*)元\(上次过渡余额\)', balance_text)
    return JsonResponse({
        'id': soup.select('tr:nth-child(2) > td:nth-child(4) > div:nth-child(1)')[0].text,
        'sum': str(round(float(balance_data[1]) + float(balance_data[2]), 2)),
        'available': balance_data[1],
        'waiting': balance_data[2],
        'isfreezed': soup.select('tr:nth-child(11) > td:nth-child(6) > div:nth-child(1)')[0].text,
        'islost': soup.select('tr:nth-child(12) > td:nth-child(6)')[0].text
    })


def details_today(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    data = student.request('http://172.31.248.20/accounttodatTrjnObject.action',
                           method='POST',
                           params={
                               'account': request.GET['account_id'],
                               'inputObject': 'all'
                           })
    detail = get_details_from_html(data)
    return JsonResponse({
        'current_page': int(request.GET['page']),
        'page_count': detail.pages,
        'details': detail.details
    })


def details_past(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    today = datetime.date.today()
    one_month_ago = today - datetime.timedelta(days=31)
    if request.GET['page'] == '1':
        student.request('/http/77726476706e69737468656265737421a1a013d2746126022a50c7fec8/accounthisTrjn1.action',
                        method='POST',
                        params={
                            'account': request.GET['account_id'],
                            'inputObject': 'all',
                            'submit': '+%C8%B7+%B6%A8+'
                        })
        student.request('/http/77726476706e69737468656265737421a1a013d2746126022a50c7fec8/accounthisTrjn2.action',
                        method='POST',
                        params={
                            'inputStartDate': one_month_ago.strftime('%Y%m%d'),
                            'inputEndDate': today.strftime('%Y%m%d')
                        })
        student.request('/http/77726476706e69737468656265737421a1a013d2746126022a50c7fec8/accounthisTrjn3.action',
                        'POST')
    data = student.request('/http/77726476706e69737468656265737421a1a013d2746126022a50c7fec8/accountconsubBrows.action',
                           method='POST',
                           params={
                               'inputStartDate': one_month_ago.strftime('%Y%m%d'),
                               'inputEndDate': today.strftime('%Y%m%d'),
                               'pageNum': request.GET['page']
                           }).text
    detail = get_details_from_html(data)
    return JsonResponse({
        'current_page': int(request.GET['page']),
        'page_count': detail.pages,
        'details': detail.details
    })


def get_details_from_html(data):
    soup = BeautifulSoup(data, 'lxml').select('#tables > tr')
    detail = []
    if len(soup) != 2:
        for i in range(1, len(soup) - 2):
            tds = soup[i].select('td')
            detail.append({
                'time': tds[0].text.strip(),
                'type': tds[3].text.strip(),
                'place': tds[4].text.strip(),
                'consume': tds[5].text.strip(),
                'balance': tds[6].text.strip(),
                'info': tds[9].text.strip()
            })

    class Details:
        def __init__(self, pages, details):
            self.pages = pages
            self.details = details

    return Details(int(re.search(r'共([0-9]*)页', data)[1]), detail)

def lose(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    data = student.request('/http/77726476706e69737468656265737421a1a013d2746126022a50c7fec8/accountDoLoss.action',
                           method='POST',
                           params={
                               'account': request.GET['account_id'],
                               'passwd': request.GET['password']
                           }).text
    data = BeautifulSoup(data, 'lxml').select('.biaotou')[0].text.strip()
    if '操作成功' in data:
        return JsonResponse({
            'status': True,
            'message': data
        })
    else:
        return JsonResponse({
            'status': False,
            'message': data
        })


def old_index_code(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    data = student.request(
        '/http-8080/77726476706e69737468656265737421e0f4408e237e60566b1cc7a99c406d3657/code.jsp').content
    return JsonResponse({
        'image': 'data:image/jpeg;base64,' + base64.b64encode(data).decode()
    })


def old_login(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    data = student.request('/http-8080/77726476706e69737468656265737421e0f4408e237e60566b1cc7a99c406d3657/login.action?'
                           'username=%s&userpwd=%s&randcode=%s&usertype=2&logintype=2' % (
                               request.GET['account_id'], request.GET['password'], request.GET['code'])).text
    if data == 'accloginok!':
        status = True
        message = '登录成功'
    else:
        status = False
        message = data
    return JsonResponse({
        'status': status,
        'message': message
    })


def old_lose_code(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    data = student.request(
        '/http-8080/77726476706e69737468656265737421e0f4408e237e60566b1cc7a99c406d3657/getCheckpic.action').content
    return JsonResponse({
        'image': 'data:image/jpeg;base64,' + base64.b64encode(data).decode()
    })


def old_unlose(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    data = student.request('/http-8080/77726476706e69737468656265737421e0f4408e237e60566b1cc7a99c406d3657/'
                           'accountunlose.action?account=%s&passwd=%s&captcha=%s' % (
                           request.GET['account_id'], request.GET['password'], request.GET['code'])).json()
    print(data)
    return JsonResponse({
        'status': (data['error'] == '交易成功'),
        'message': data['error']
    })
