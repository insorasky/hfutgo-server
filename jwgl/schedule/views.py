from django.http import JsonResponse
from student import Student
import json


def schedules(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    student.request('http://jxglstu.hfut.edu.cn/eams5-student/neusoft-sso/login')
    data = json.loads(student.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/course-table/get-data?bizTypeId=2&semesterId=134&dataId=149251').text)
