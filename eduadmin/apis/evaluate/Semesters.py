from utils.Request import Request, get_json_response
from bs4 import BeautifulSoup


class Semesters(Request):
    def get(self, request):
        super(Semesters, self).get(request)
        self.stu.request('http://jxglstu.hfut.edu.cn/eams5-student/neusoft-sso/login')
        data = self.stu.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey').text
        soup = BeautifulSoup(data, 'lxml').select('#semester > option')
        response = []
        for option in soup:
            if option['value']:
                response.append({
                    'name': option.text,
                    'sid': option['value']
                })
        return get_json_response(response)
