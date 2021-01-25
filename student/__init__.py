import requests
from requests.utils import add_dict_to_cookiejar, dict_from_cookiejar
import json
from .ECBPkcs7 import ECBPkcs7
from .VPNUrl import encrypUrl

URL_VPN_BASE = 'https://webvpn.hfut.edu.cn'
URL_CAS_BASE = URL_VPN_BASE + '/https/77726476706e69737468656265737421f3f652d22f367d44300d8db9d6562d'
URL_ONE_BASE = URL_VPN_BASE + '/https/77726476706e69737468656265737421fff944d22f367d44300d8db9d6562d'
URL_PAGE = URL_CAS_BASE + '/cas/login'
URL_VERCODE = URL_CAS_BASE + '/cas/vercode'
URL_LOGIN_FLAVORING = URL_CAS_BASE + '/cas/checkInitVercode'
URL_COOKIE = 'https://webvpn.hfut.edu.cn/wengine-vpn/cookie?method=get&host=cas.hfut.edu.cn&scheme=http&path=/cas/login'
URL_CHECK = URL_CAS_BASE + '/cas/policy/checkUserIdenty'
URL_LOGIN = URL_CAS_BASE + '/cas/login?service=https%3A%2F%2Fwebvpn.hfut.edu.cn%2Flogin%3Fcas_login%3Dtrue'
URL_VPN_LOGIN = URL_CAS_BASE + '/cas/login?service=https%3A%2F%2Fwebvpn.hfut.edu.cn%2Flogin%3Fcas_login%3Dtrue'
URL_GET_OC = URL_CAS_BASE + '/cas/oauth2.0/authorize?response_type=code&client_id=BsHfutEduPortal&redirect_uri=https://one.hfut.edu.cn/Login'
URL_VERIFY_OC = URL_ONE_BASE + '/Login'
URL_GET_AT = URL_ONE_BASE + '/api/auth/oauth/getToken'
URL_VERIFY_AT = URL_ONE_BASE + '/cas/bosssoft/checkToken'
URL_USERINFO = URL_ONE_BASE + '/api/center/user/selectUserInfoForHall'
TICKET_NAME = 'wengine_vpn_ticketwebvpn_hfut_edu_cn'


class Student:
    session = requests.session()
    __at = None

    def __init__(self, ticket=None, at_token=None):
        if ticket is not None:
            add_dict_to_cookiejar(self.session.cookies, {TICKET_NAME: ticket})
        if at_token is not None:
            self.__at = at_token

    @property
    def ticket(self):
        cookies = dict_from_cookiejar(self.session.cookies)
        if TICKET_NAME in cookies:
            return cookies[TICKET_NAME]
        else:
            return None

    def login(self, username, password):
        # 访问登录页
        self.session.get(URL_LOGIN)
        # 置VERCODE
        self.session.get(URL_VERCODE)
        # 获取LOGIN_FLAVORING
        self.session.get(URL_LOGIN_FLAVORING)
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
        data = json.loads(self.session.get(URL_CHECK, params={
            'username': username,
            'password': password
        }).text)
        if 'authTicket' not in data['data']:
            return -1
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
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded'
        }).text
        # 获取OC令牌
        data = self.session.get(URL_GET_OC).text
        if 'Central Authentication Service' not in data:
            return -2
        data = self.session.get(URL_GET_OC, allow_redirects=False)
        if data.status_code != 302:
            return -3
        oc = data.headers['Location'].split('=')[1]
        # 验证OC令牌
        self.session.get(URL_VERIFY_OC)
        # 获取AT令牌
        data = json.loads(self.session.get(URL_GET_AT, params={
            'type': 'portal',
            'redirect': 'https%3A%2F%2Fone.hfut.edu.cn%2FLogin%3Fcode%3D' + oc,
            'code': oc
        }).text)
        if data['data'] is None:
            return -4
        self.__at = data['data']['access_token']
        return True

    def request(self, url, method='GET', params=None, data=None, headers={}, allow_redirects=True):
        url = url if url[0] == '/' else encrypUrl(url.split('://')[0], url)
        if '77726476706e69737468656265737421fff944d22f367d44300d8db9d6562d' in url:
            headers.update({'Authorization': 'Bearer ' + self.__at})
        return self.session.request(method=method, url=URL_VPN_BASE + url, params=params, data=data,
                                    headers=headers, allow_redirects=allow_redirects)

    @property
    def userinfo(self):
        try:
            return json.loads(self.session.get(URL_USERINFO, headers={
                'Authorization': 'Bearer ' + self.__at
            }).text)['data'] if self.__at else None
        except json.decoder.JSONDecodeError:
            return None

    @property
    def is_login(self):
        try:
            data = json.loads(self.session.get(URL_VERIFY_AT, params={
                'token': self.__at
            }).text)
            return data['data']
        except requests.exceptions.RequestException:
            return False

    @property
    def at_token(self):
        return self.__at

    @property
    def vpn_token(self):
        try:
            return dict_from_cookiejar(self.session.cookies)[TICKET_NAME]
        except KeyError:
            return None
