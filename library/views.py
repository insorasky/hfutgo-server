from student import Student
from bs4 import BeautifulSoup
from django.http import JsonResponse
import json


def room_free(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    data = student.request('/http/77726476706e69737468656265737421a2a611d2736526022a5ac7fdca06/roomshow/').text
    soup = BeautifulSoup(data, 'lxml').select('table > tr')
    response = []
    for tr in soup:
        tds = tr.select('td')
        if len(tds) != 3 or '区域' in tds[0].text:
            continue
        response.append({
            'name': '总计' if tds[0].text == 'ALL' else tds[0].text,
            'unavailable': tds[1].text,
            'available': tds[2].text
        })
    return JsonResponse({
        'data': response
    })


def hot(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    data = student.request(
        '/http-8080/77726476706e69737468656265737421a2a611d2736526022a5ac7f9/opac/ajax_top_lend_shelf.php').text
    soup = BeautifulSoup(data, 'lxml').select('ul')
    borrow_list = []
    for li in soup[0].select('li'):
        borrow_list.append({
            'title': li.text,
            'marc': li.select('a')[0]['href'].split('=')[1]
        })
    book_list = []
    for li in soup[1].select('li'):
        book_list.append({
            'title': li.text,
            'marc': li.select('a')[0]['href'].split('=')[1]
        })
    return JsonResponse({
        'borrow_list': borrow_list,
        'book_list': book_list
    })


def book_search(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    filters = json.loads(request.body)['filters']
    data = student.request(
        '/http-8080/77726476706e69737468656265737421a2a611d2736526022a5ac7f9/opac/ajax_search_adv.php',
        method='POST',
        headers={
            'Content-Type': 'application/json'
        },
        data={
            "searchWords": [
                {
                    "fieldList": [
                        {
                            "fieldCode": "any",
                            "fieldValue": request.GET['word']
                        }
                    ]
                }
            ],
            "filters": filters,
            "limiter": [],
            "sortField": "relevance",
            "sortType": "desc",
            "pageSize": 20,
            "pageCount": int(request.GET['page']),
            "locale": "zh_CN",
            "first": True
        }).text
    return JsonResponse(json.loads(data))


def book_info(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    data = student.request('/http-8080/77726476706e69737468656265737421ffe7409f69386e456a468ca88d1b203b/opac/item.php?marc_no=' + request.GET['marc']).text
    soup = BeautifulSoup(data, 'lxml')
    information = []
    content = ''
    for dl in soup.select('.booklist'):
        title = dl.select('dt')[0].text
        info = dl.select('dd')[0].text
        if title == '电子资源:' or title == '' or title == '豆瓣简介：':
            continue
        if title == '提要文摘附注:':
            content = info
        else:
            information.append({
                'title': title,
                'value': info
            })
    available = []
    for tr in soup.select('.whitetext'):
        td = tr.select('td')
        if len(td) < 4:
            continue
        available.append({
            'bookno': td[0].text,
            'barcode': td[1].text,
            'place': td[3].text.strip(),
            'status': td[4].text
        })
    return JsonResponse({
        'info': information,
        'content': content,
        'available': available
    })


def my_books(request):
    student = Student(request.GET['vpn_token'], request.GET['at_token'])
    student.request('/http-8080/77726476706e69737468656265737421a2a611d2736526022a5ac7f9/reader/hwthau2.php')
    data = student.request('/http-8080/77726476706e69737468656265737421a2a611d2736526022a5ac7f9/reader/book_lst.php').text
    soup = BeautifulSoup(data, 'lxml').select('.table_line > tr')
    response = []
    first = True
    for tr in soup:
        if first:
            first = False
            continue
        td = tr.select('td')
        print(td[1])
        response.append({
            'name': td[1].text,
            'starttime': td[2].text,
            'endtime': td[3].text,
            'marc': td[1].select('a')[0]['href'].split('marc_no=')[1]
        })
    return JsonResponse({
        'data': response
    })
