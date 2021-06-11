from django.views import View
from utils.response import get_json_response


class EmptyRoom(View):
    def get(self, request, stu, user):
        data = stu.request(
            method='POST',
            url='http://172.31.241.31:9999/ecc/api/booking/bookinginfo',
            data='page=%s&limit=20&status=%s&buildingId=%s&campusId=%s&date=%s&lessonNo=%s&personNum=%s&teachingRoomId=%s' % (
                request.GET['page'], request.GET['status'], request.GET['buildingId'], request.GET['campusId'],
                request.GET['date'], request.GET['lessonNo'], request.GET['personNum'], request.GET['roomId']
            ),
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        ).json()
        if data['code'] == '0':
            return get_json_response(data)
        else:
            return get_json_response('查询出错', 3501)
