from student.StudentRequest import StudentRequest, get_json_response
from .get_details_from_html import get_details_from_html


class DetailsToday(StudentRequest):
    def get(self, request):
        super(DetailsToday, self).get(request)
        data = self.stu.request('http://172.31.248.20/accounttodatTrjnObject.action',
                                method='POST',
                                params={
                                    'account': request.GET['account_id'],
                                    'inputObject': 'all'
                                })
        detail = get_details_from_html(data)
        return get_json_response({
            'page_count': detail.pages,
            'details': detail.details
        })
