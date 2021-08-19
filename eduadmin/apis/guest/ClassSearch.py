from django.views import View
from utils.response import get_json_response
from utils.Manager import Manager


class ClassSearch(View):
    def get(self, request, guest):
        mgr = Manager()
        data = mgr.request(
            url='/bizType/2/adminclass-course-table/semester/154/search',
            params={
                'nameZhLike': request.GET['name'],
                'grades': request.GET['grade'],
                'department': request.GET['deptid'],
                'queryPage__': '%s,100' % request.GET['page']
            },
            headers={
                'Accept': 'application/json'
            }
        ).json()
        return get_json_response({
            'classes': [{
                'name': item['nameZh'],
                'code': item['code'],
                'id': item['id'],
                'grade': item['grade'],
                'department': item['mngtDepart']['abbrZh']
            } for item in data['data']],
            'sum': data['_page_']['totalRows'],
            'pages': data['_page_']['totalPages']
        })
