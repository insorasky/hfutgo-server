from utils.Request import Request, get_json_response
from ..models import Machine


class Machines(Request):
    def get(self, request):
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
