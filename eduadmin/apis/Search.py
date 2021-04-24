from utils.Request import Request, get_json_response
from ..models import Lesson
import json
from django.core.paginator import Paginator


class Search(Request):
    def get(self, request):
        super(Search, self).get(request)
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
        return get_json_response({
            'last_page': query.num_pages,
            'data': list(response)
        })
