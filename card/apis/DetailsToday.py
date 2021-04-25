from utils.response import get_json_response
from django.views import View
from .get_details_from_html import get_details_from_html


class DetailsToday(View):
    def get(self, request, stu, user):
        data = stu.request('http://172.31.248.20/accounttodatTrjnObject.action',
                           method='POST',
                           params={
                               'account': user.card_id,
                               'inputObject': 'all'
                           })
        detail = get_details_from_html(data)
        return get_json_response({
            'page_count': detail.pages,
            'details': detail.details
        })
