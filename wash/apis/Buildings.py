from utils.Request import Request, get_json_response
from ..models import Building


class Buildings(Request):
    def get(self, request):
        query = Building.objects.filter(campus=request.GET['campus']).order_by('sort')
        data = []
        for building in query:
            data.append(building.name)
        return get_json_response(data)
