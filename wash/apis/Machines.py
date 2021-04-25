from utils.response import get_json_response
from django.views import View
from ..models import Machine


class Machines(View):
    def get(self, request, stu, user):
        query = Machine.objects.filter(building=request.GET['building']).order_by('sort')
        data = []
        for machine in query:
            data.append({
                'name': machine.name,
                'type': machine.type,
                'machineid': machine.machineid,
                'NQT': machine.NQT
            })
        return get_json_response(data)
