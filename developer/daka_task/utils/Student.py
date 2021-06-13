import requests
from requests.utils import add_dict_to_cookiejar, dict_from_cookiejar
import json
from utils.ECBPkcs7 import ECBPkcs7
from utils.VPNUrl import encrypUrl

VPN_DOMAIN = 'webvpn.hfut.edu.cn'
URL_VPN_BASE = 'https://' + VPN_DOMAIN
TICKET_NAME = 'wengine_vpn_ticket' + VPN_DOMAIN.replace('.', '_')
URL_CAS_BASE = URL_VPN_BASE + '/https/77726476706e69737468656265737421f3f652d22f367d44300d8db9d6562d'
URL_PAGE = URL_CAS_BASE + '/cas/login'
URL_VERCODE = URL_CAS_BASE + '/cas/vercode'
URL_LOGIN_FLAVORING = URL_CAS_BASE + '/cas/checkInitVercode'
URL_COOKIE = URL_VPN_BASE + '/wengine-vpn/cookie?method=get&host=cas.hfut.edu.cn&scheme=http&path=/cas/login'
URL_CHECK = URL_CAS_BASE + '/cas/policy/checkUserIdenty'
URL_LOGIN = URL_CAS_BASE + '/cas/login?service=https%3A%2F%2F' + VPN_DOMAIN + '%2Flogin%3Fcas_login%3Dtrue'
URL_VPN_LOGIN = URL_CAS_BASE + '/cas/login?service=https%3A%2F%2F' + VPN_DOMAIN + '%2Flogin%3Fcas_login%3Dtrue'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'


class Student:

    def __init__(self, ticket=None):
        self.session = requests.session()
        self.__boss_ticket = None
        if ticket is not None:
            add_dict_to_cookiejar(self.session.cookies, {TICKET_NAME: ticket})

    @property
    def ticket(self):
        cookies = dict_from_cookiejar(self.session.cookies)
        if TICKET_NAME in cookies:
            return cookies[TICKET_NAME]
        else:
            return None

    def login(self, username, password):
        # 访问登录页
        login_page = self.session.get(URL_LOGIN)
        # 置VERCODE
        vercode_page = self.session.get(URL_VERCODE)
        # 获取LOGIN_FLAVORING
        flavor_page = self.session.get(URL_LOGIN_FLAVORING)
        # 从Cookie中提取LOGIN_FLAVORING
        flavoring = ''
        cookies = self.session.get(URL_COOKIE).text.split(';')
        for cookie in cookies:
            data = cookie.strip().split('=')
            if data[0] == 'LOGIN_FLAVORING':
                flavoring = data[1]
                break
        if flavoring == '':
            return False
        # CAS验证用户
        password = ECBPkcs7(flavoring).encrypt(password)
        data = self.session.get(URL_CHECK, params={
            'username': username,
            'password': password
        }).json()
        if 'authTicket' not in data['data']:  # 密码错误
            return -1
        self.__boss_ticket = data['data']['authTicket']
        # CAS登录
        data = self.session.post(URL_LOGIN, data={
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
        }).text
        return True

    def request(self, url, method='GET', params=None, data=None, headers=None, allow_redirects=True):
        if headers is None:
            headers = {}
        if self.ticket:
            url = URL_VPN_BASE + (url if url[0] == '/' else encrypUrl(url.split('://')[0], url))
        return self.session.request(method=method, url=url, params=params, data=data,
                                    headers=headers, allow_redirects=allow_redirects)

    @property
    def boss_ticket(self):
        return self.__boss_ticket
