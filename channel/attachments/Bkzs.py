from student.StudentRequest import StudentRequest
from django.http import HttpResponse


class Bkzs(StudentRequest):
    def get(self, request):
        super(Bkzs, self).get(request)
        data = self.stu.request('http://bkzs.hfut.edu.cn' + request.GET['url'])
        response = HttpResponse(data.content)
        response['Content-Type'] = data.headers['Content-Type']
        return response
