from django.http import JsonResponse, HttpResponse
from student import Student
from urllib.parse import unquote
import time


def content(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    token = student.request('http://bkzs.hfut.edu.cn/f/ajax_get_csrfToken',
                                       method='POST',
                                       params={'n': '1'},
                                       headers={
                                           'X-Requested-With': 'XMLHttpRequest',
                                           'X-Requested-Time': str(int(time.time() * 1000))
                                       }).json()['data']
    data = student.request('http://bkzs.hfut.edu.cn/f/newsCenter/ajax_article_view',
                                      method='POST',
                                      params={
                                          'contentId': request.GET['id']
                                      },
                                      headers={
                                          'Csrf-Token': token,
                                          'X-Requested-Time': str(int(time.time() * 1000)),
                                          'X-Requested-With': 'XMLHttpRequest'
                                      }).json()
    attachments = []
    print(data['data']['article']['attachment'][0])
    for attachment in data['data']['article']['attachment']:
        attachments.append({
            'name': unquote(attachment).split('/')[-1].split('.')[0],
            'url': attachment
        })
    return JsonResponse({
        'content': data['data']['article']['articleData']['content'],
        'attachment': attachments
    })


def attachment(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    data = student.request('http://bkzs.hfut.edu.cn' + request.GET['url'])
    response = HttpResponse(data.content)
    response['Content-Type'] = data.headers['Content-Type']
    return response
