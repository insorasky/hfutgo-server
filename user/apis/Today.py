from utils.Request import Request, get_json_response


class Today(Request):
    def get(self, request):
        info = self.stu.userinfo
        balance = self.stu.request('/https/77726476706e69737468656265737421fff944d22f367d44300d8db9d6562d/api/operation/thirdPartyApi/schoolcard/balance?sno=' + info['loginName']).json()['data']
        borrow_books = self.stu.request('/https/77726476706e69737468656265737421fff944d22f367d44300d8db9d6562d/api/operation/library/getBorrowNum').json()['data']
        subscribe_books = self.stu.request('/https/77726476706e69737468656265737421fff944d22f367d44300d8db9d6562d/api/operation/library/getSubscribeNum').json()['data']
        emails = self.stu.request('/https/77726476706e69737468656265737421fff944d22f367d44300d8db9d6562d/api/center/user/getBindMailList').json()['data']
        unread_email = 0
        for email in emails:
            unread_email += self.stu.request('/https/77726476706e69737468656265737421fff944d22f367d44300d8db9d6562d/api/msg/mailBusiness/getUnreadMsg?mail=' + email['mail']).json()['data']
        return get_json_response({
            'balance': balance,
            'borrow_books': borrow_books,
            'subscribe_books': subscribe_books,
            'unread_email': unread_email
        })
