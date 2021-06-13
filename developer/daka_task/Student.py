import requests
from utils.ECBPkcs7 import ECBPkcs7
from urllib.parse import urlencode

URL_CAS_BASE = 'https://cas.hfut.edu.cn'
URL_VERCODE = URL_CAS_BASE + '/cas/vercode'
URL_LOGIN_FLAVORING = URL_CAS_BASE + '/cas/checkInitVercode'
URL_CHECK = URL_CAS_BASE + '/cas/policy/checkUserIdenty'
URL_LOGIN = 'http://stu.hfut.edu.cn/xsfw/sys/emapfunauth/casValidate.do?service=http%3A%2F%2Fstu.hfut.edu.cn%2Fxsfw%2Fsys%2Fxggzptapp%2F*default%2Findex.do'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'


class Student:

    def __init__(self):
        self.session = requests.session()
        self.session.headers = {}
        self.__boss_ticket = None

    def login(self, username, password):
        # 访问登录页
        login_page = self.session.get(URL_LOGIN)
        login_url = login_page.url
        # 置VERCODE
        vercode_page = self.session.get(URL_VERCODE)
        # 获取LOGIN_FLAVORING
        flavor_page = self.session.get(URL_LOGIN_FLAVORING)
        # 从Cookie中提取LOGIN_FLAVORING
        flavoring = self.session.cookies['LOGIN_FLAVORING']
        # CAS验证用户
        password = ECBPkcs7(flavoring).encrypt(password)
        data = self.session.get(URL_CHECK, params={
            'username': username,
            'password': password
        })
        data1 = data.json()
        if 'authTicket' not in data1['data']:  # 密码错误
            return False
        self.__boss_ticket = data1['data']['authTicket']
        # CAS登录
        data2 = self.session.post(login_url, data={
            'username': username,
            'password': password,
            'capcha': '',
            'execution': 'e1s1',
            'geolocation': '',
            'submit': '登录',
            '_eventId': 'submit'
        }, headers={
            'User-Agent': USER_AGENT,
            'Content-Type': 'application/x-www-form-urlencoded'
        })
        return True

    def request(self, url, method='GET', params=None, data=None, headers=None, allow_redirects=True):
        return self.session.request(method=method, url=url, params=params, data=data,
                                    headers=headers, allow_redirects=allow_redirects)
