from utils.response import get_json_response
from .get_details_from_html import get_details_from_html
import datetime
from django.views import View


class DetailsPast(View):
    def get(self, request, stu, user):
        today = datetime.date.today()
        one_month_ago = today - datetime.timedelta(days=31)
        if request.GET['page'] == '1':
            stu.request('http://hfut-test.heppy.wang:7002/accounthisTrjn1.action',
                             method='POST',
                             params={
                                 'account': user.card_id,
                                 'inputObject': 'all',
                                 'submit': '+%C8%B7+%B6%A8+'
                             })
            stu.request('http://hfut-test.heppy.wang:7002/accounthisTrjn2.action',
                             method='POST',
                             params={
                                 'inputStartDate': one_month_ago.strftime('%Y%m%d'),
                                 'inputEndDate': today.strftime('%Y%m%d')
                             })
            stu.request('http://hfut-test.heppy.wang:7002/accounthisTrjn3.action', 'POST')
        data = stu.request(
            'http://hfut-test.heppy.wang:7002/accountconsubBrows.action',
            method='POST',
            params={
                'inputStartDate': one_month_ago.strftime('%Y%m%d'),
                'inputEndDate': today.strftime('%Y%m%d'),
                'pageNum': request.GET['page']
            }).text
        detail = get_details_from_html(data)
        return get_json_response({
            'current_page': int(request.GET['page']),
            'page_count': detail.pages,
            'details': detail.details
        })
