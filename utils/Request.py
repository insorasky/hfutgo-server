from django.views import View
from utils.Student import Student
from django.http import JsonResponse


class Request(View):
    def get(self, request):
        self.stu = Student(
            ticket=request.GET['ticket'] if 'ticket' in request.GET else None,
            at_token=request.GET['at'] if 'at' in request.GET else None
        )


def get_json_response(data, status_code=200):
    response = JsonResponse({
        'status': status_code,
        'data' if status_code == 200 else 'error': data
    })
    response.status_code = 200 if status_code == 200 else 403
    return response
