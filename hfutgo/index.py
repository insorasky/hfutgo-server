from django.http import HttpResponse


def index(request):
    return HttpResponse('HFUTGo服务器<br />'
                        '<a href="https://www.sorasky.in">返回inSoraSky博客</a>')
