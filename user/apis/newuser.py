from django.http import JsonResponse
from student import Student


def get_phone_code(request):
    student = Student(request.GET['vpn_token'])
    data = student.request('https://cas.hfut.edu.cn/cas/policy/sendVerifCode?username=%s&connectInfo=%s&type=phone' % (request.GET['username'], request.GET['phone'])).json()
    return JsonResponse({
        'status': True if data['data'] else False,
        'message': data['msg']
    })


def get_email_code(request):
    student = Student(request.GET['vpn_token'])
    data = student.request('https://cas.hfut.edu.cn/cas/policy/sendVerifCode?username=%s&connectInfo=%s&type=email' % (request.GET['username'], request.GET['email'])).json()
    return JsonResponse({
        'status': True if data['data'] else False,
        'message': data['msg']
    })


def verify_email(request):
    student = Student(request.GET['vpn_token'])
    data = student.request('https://cas.hfut.edu.cn/cas/policy/loginInfoRecord',
                                      params={
                                          'username': request.GET['username'],
                                          'mail': request.GET['email'],
                                          'verifCode': request.GET['code'],
                                          'type': 'mail',
                                          'authTicket': request.GET['boss_ticket']
                                      }).json()
    return JsonResponse({
        'status': True if data['code'] else False,
        'message': data['msg']
    })


def verify_phone(request):
    student = Student(request.GET['vpn_token'])
    data = student.request('https://cas.hfut.edu.cn/cas/policy/loginInfoRecord',
                                      params={
                                          'username': request.GET['username'],
                                          'phoneNumber': request.GET['phone'],
                                          'verifCode': request.GET['code'],
                                          'type': 'phone',
                                          'authTicket': request.GET['boss_ticket']
                                      }).json()
    return JsonResponse({
        'status': True if data['code'] else False,
        'message': data['msg']
    })
