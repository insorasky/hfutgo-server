from utils.response import get_json_response
from django.views import View
from ..models import Config


class TimeTable(View):
    def get(self, request, stu, user):
        data = Config.objects.filter(name='timetable_%s' % request.GET['campus']).first().value
        return get_json_response(data)
