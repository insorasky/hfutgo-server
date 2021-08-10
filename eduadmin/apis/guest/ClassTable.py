from django.views import View
import json
import re
from utils.response import get_json_response
from utils.Manager import Manager
from ..schedule.analyze import analyze
from bs4 import BeautifulSoup

LESSONS_REG = r'renderCourseTable\(\s*\[([\s\S]*)\]'
LAYOUT_ID_REG = r'timeTableLayoutId: (.*)\n'


class ClassTable(View):
    def get(self, request, guest):
        mgr = Manager()
        resp = mgr.request('/bizType/2/adminclass-course-table/semester/%s/course-table/%s' % (request.GET['sid'], request.GET['cid']))
        soup = BeautifulSoup(resp.content, 'lxml').select_one('#lessons > tbody').findAll('tr')
        lessons = []
        for tr in soup:
            data = [td.text.strip() for td in tr.findAll('td')]
            print([item.strip() for item in data[8].split(';')])
            lessons.append({
                'code': data[3],
                'name': data[2],
                'schedules': [analyze(item.strip()) for item in data[8].split(';')],
                'classes': data[4],
                'credits': None,
                'type': data[5],
                'teachers': [{
                    'name': re.sub(r'\s{2,}|\n+', '', item),
                    'title': None
                } for item in data[7].split('，')]
            })
        return get_json_response({
            'layout': int(re.search(LAYOUT_ID_REG, resp.text)[1]),
            'last_week': None,
            'current_week': None,
            'lessons': lessons
        })
