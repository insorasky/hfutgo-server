from utils.Request import Request, get_json_response
from ..models import Config


class TimeTable(Request):
    def get(self, request):
        data = Config.objects.filter(name='timetable_%s' % request.GET['campus']).first()
        return get_json_response(data.value)
