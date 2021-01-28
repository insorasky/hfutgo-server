from django.http import JsonResponse
from .models import Lesson
from django.core.paginator import Paginator
from bs4 import BeautifulSoup
from student import Student
import json


def search(request):
    data = json.loads(request.body)
    filters = data['filters']
    building = ''
    if 'name' in filters:
        filters['name__contains'] = filters['name']
        filters.pop('name')
    if 'classname' in filters:
        filters['classname__contains'] = filters['classname']
        filters.pop('classname')
    if 'teacher' in filters:
        filters['teacher__contains'] = filters['teacher']
        filters.pop('teacher')
    if 'building' in filters:
        building = filters['building']
        filters.pop('building')
    query = Paginator(Lesson.objects.filter(**filters), 25)
    data = query.page(data['page']).object_list.values()
    response = []
    if building:
        for l in data:
            for c in l['info']:
                if building in c['room']:
                    response.append(l)
                    break
    else:
        response = data
    return JsonResponse({
        'last_page': query.num_pages,
        'data': list(response)
    })


def exams(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    student.request('http://jxglstu.hfut.edu.cn/eams5-student/neusoft-sso/login')
    data = student.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/exam-arrange').text
    soup = BeautifulSoup(data, 'lxml').select('tbody > tr')
    response = []
    for tr in soup:
        td = tr.select('td')
        response.append({
            'name': td[0].text.strip(),
            'time': td[1].text,
            'room': td[2].text,
            'building': td[3].text,
            'campus': td[4].text
        })
    return JsonResponse({
        'data': response
    })
