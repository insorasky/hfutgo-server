from student.StudentRequest import StudentRequest, get_json_response
from bs4 import BeautifulSoup


class Semester(StudentRequest):
    def get(self, request):
        super(Semester, self).get(request)
        self.stu.request('http://jxglstu.hfut.edu.cn/eams5-student/neusoft-sso/login')
        data = self.stu.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/grade/sheet/').text
        soup = BeautifulSoup(data, 'lxml').select('#semester > option')
        response = []
        for option in soup:
            if option['value']:
                response.append({
                    'name': option.text,
                    'sid': option['value']
                })
        return get_json_response(response)
