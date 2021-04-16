from student.StudentRequest import StudentRequest, get_json_response
from bs4 import BeautifulSoup
import re


class Info(StudentRequest):
    def get(self, request):
        super(Info, self).get(request)
        self.stu.request('http://172.31.248.20/ahdxdrPortalHome.action')
        data = self.stu.request(
            '/http/77726476706e69737468656265737421a1a013d2746126022a50c7fec8/accountcardUser.action').text
        soup = BeautifulSoup(data, 'lxml').select('.tttt > tr:nth-child(1) > th:nth-child(1) > table:nth-child(1)')[0]
        balance_text = soup.select('tr:nth-child(12) > td:nth-child(2)')[0].text
        balance_data = re.match(r'(.*)元（卡余额）(.*)元\(当前过渡余额\)(.*)元\(上次过渡余额\)', balance_text)
        return get_json_response({
            'id': soup.select('tr:nth-child(2) > td:nth-child(4) > div:nth-child(1)')[0].text,
            'sum': str(round(float(balance_data[1]) + float(balance_data[2]), 2)),
            'available': balance_data[1],
            'waiting': balance_data[2],
            'freeze': soup.select('tr:nth-child(11) > td:nth-child(6) > div:nth-child(1)')[0].text,
            'lost': soup.select('tr:nth-child(12) > td:nth-child(6)')[0].text
        })
