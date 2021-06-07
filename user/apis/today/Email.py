from utils.response import get_json_response
from django.views import View


class Email(View):
    def get(self, request, stu, user):
        emails = stu.request(
            '/https/77726476706e69737468656265737421fff944d22f367d44300d8db9d6562d/api/center/user/getBindMailList').json()[
            'data']
        unread_email = 0
        for email in emails:
            unread_email += stu.request(
                '/https/77726476706e69737468656265737421fff944d22f367d44300d8db9d6562d/api/msg/mailBusiness/getUnreadMsg?mail=' +
                email['mail']).json()['data']
        return get_json_response({
            'unread_email': unread_email
        })
