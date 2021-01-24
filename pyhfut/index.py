from django.http import HttpResponse


def index(request):
    return HttpResponse('合工大超级导航服务器<br />'
                        '<a href="https://www.sorasky.in">返回inSoraSky博客</a>')
