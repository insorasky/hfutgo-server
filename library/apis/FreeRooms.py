from utils.Request import Request, get_json_response
from bs4 import BeautifulSoup


class FreeRooms(Request):
    def room_free(self, request):
        data = self.stu.request('/http/77726476706e69737468656265737421a2a611d2736526022a5ac7fdca06/roomshow/').text
        soup = BeautifulSoup(data, 'lxml').select('table > tr')
        response = []
        for tr in soup:
            tds = tr.select('td')
            if len(tds) != 3 or '区域' in tds[0].text:
                continue
            response.append({
                'name': '总计' if tds[0].text == 'ALL' else tds[0].text,
                'unavailable': tds[1].text,
                'available': tds[2].text
            })
        return get_json_response(response)
