from student.StudentRequest import StudentRequest, get_json_response


class Schedules(StudentRequest):
    def get(self, request):
        super(Schedules, self).get(request)
        self.stu.request('http://jxglstu.hfut.edu.cn/eams5-student/neusoft-sso/login')
        data = self.stu.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/course-table/get-data?bizTypeId=2&semesterId=134&dataId=149251').json()
