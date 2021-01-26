from django.http import JsonResponse
from .models import *


def timetable(request):
    data = Util.objects.filter(name='timetable_%s' % request.GET['campus']).first()
    return JsonResponse(data.value, safe=False)


def notice(request):
    data = Notice.objects.filter(page=request.GET['page'], show=True).order_by('-time').all()
    response = []
    for dat in data:
        response.append(dat.text)
    return JsonResponse({
        'theme': data[0].theme,
        'notices': response
    })
