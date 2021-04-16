from student.StudentRequest import StudentRequest, get_json_response


class Subjects(StudentRequest):
    def get(self, request):
        super(Subjects, self).get(request)
        stu_id = self.stu.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey', allow_redirects=False).headers['Location'].split('/')[-1]
        data = self.stu.request('http://jxglstu.hfut.edu.cn/eams5-student/for-std/lesson-survey/%s/search/%s' % (request.GET['sid'], stu_id)).json()
        response = []
        for subject in data['forStdLessonSurveySearchVms']:
            tasks = []
            for task in subject['lessonSurveyTasks']:
                tasks.append({
                    'id': task['id'],
                    'teacher': task['teacher']['person']['nameZh'],
                    'submitted': task['submitted']
                })
            period = subject['openEndTimeContent'].split('~')
            response.append({
                'class_id': subject['code'],
                'name': subject['course']['nameZh'],
                'period': {
                    'start': period[0],
                    'end': period[1]
                },
                'tasks': tasks
            })
        return get_json_response(response)
