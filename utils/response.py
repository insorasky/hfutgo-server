from django.http import JsonResponse


def get_json_response(data, status_code=200):
    response = JsonResponse({
        'status': status_code,
        'data' if status_code == 200 else 'error': data
    })
    response.status_code = 200 if status_code == 200 else 403
    return response
