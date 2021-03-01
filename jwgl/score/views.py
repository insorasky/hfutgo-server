from django.http import JsonResponse
from student import Student
from bs4 import BeautifulSoup


def semester(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    student.request('http://jxglstu.hfut.edu.cn/eams5-student/neusoft-sso/login')
    data = student.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/grade/sheet/').text
    soup = BeautifulSoup(data, 'lxml').select('#semester > option')
    response = []
    for option in soup:
        if option['value']:
            response.append({
                'name': option.text,
                'sid': option['value']
            })
    return JsonResponse({
        'data': response
    })


def info(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    stu_id = student.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/grade/sheet/', allow_redirects=False).headers['Location'].split('/')[-1]
    data = student.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/grade/sheet/info/%s?semester=%s' % (stu_id, request.GET['sid'])).text
    soup = BeautifulSoup(data.replace('<br />', '\n'), 'lxml').select('tbody > tr')
    response = []
    for tr in soup:
        td = tr.select('td')
        details = []
        for line in td[6].text.splitlines():
            detail = line.strip().split(':')
            details.append({
                'name': detail[0],
                'score': detail[1]
            })
        response.append({
            'name': td[0].text,
            'subject_id': td[1].text,
            'class_id': td[2].text,
            'mark': td[3].text,
            'point': td[4].text,
            'score': td[5].text,
            'details': details
        })
    return JsonResponse({
        'data': response
    })
