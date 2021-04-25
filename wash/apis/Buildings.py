from utils.response import get_json_response
from django.views import View
from ..models import Building


class Buildings(View):
    def get(self, request, stu):
        query = Building.objects.filter(campus=request.GET['campus']).order_by('sort')
        data = []
        for building in query:
            data.append(building.name)
        return get_json_response(data)
