from bs4 import BeautifulSoup
import re


def get_details_from_html(data):
    soup = BeautifulSoup(data, 'lxml').select('#tables > tr')
    detail = []
    if len(soup) != 2:
        for i in range(1, len(soup) - 2):
            tds = soup[i].select('td')
            detail.append({
                'time': tds[0].text.strip(),
                'type': tds[3].text.strip(),
                'place': tds[4].text.strip(),
                'consume': tds[5].text.strip(),
                'balance': tds[6].text.strip(),
                'info': tds[9].text.strip()
            })

    class Details:
        def __init__(self, pages, details):
            self.pages = pages
            self.details = details

    return Details(int(re.search(r'共([0-9]*)页', data)[1]), detail)
