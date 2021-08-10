import requests
from hashlib import sha1
from others.models import Config
from requests.utils import add_dict_to_cookiejar, dict_from_cookiejar

URL_BASE = "http://jxgltea.hfut.edu.cn:8980/eams5-manager"
URL_SALT = URL_BASE + "/login-salt"
URL_LOGIN = URL_BASE + "/login"
URL_STU_SEARCH = URL_BASE + "/bizType/2/student-course-table/semester/134/search"
URL_SCHEDULE = URL_BASE + "/bizType/2/student-course-table/semester/%s/course-table/%s"


class Manager:

    def __init__(self):
        self.__session = requests.session()
        add_dict_to_cookiejar(self.__session.cookies, Config.get("manager_session"))

    def login(self):
        print("MANAGER: LOGIN")
        data = Config.get("eduadmin_manager")
        username = data['username']
        password = data['password']
        session = requests.session()
        salt = session.get(URL_SALT).text
        password = salt + "-" + password
        password = sha1(password.encode('utf-8')).hexdigest()
        if(session.post(
            url=URL_LOGIN,
            json={
                'captcha': '',
                'username': username,
                'password': password
            }
        ).json()['result']):
            self.__session = session
            Config.set('manager_session', dict_from_cookiejar(session.cookies))
        else:
            raise Exception("PasswordError")

    def request(self, url, method='GET', timeout=7, **kwargs):
        resp = self.__session.request(
            url=URL_BASE + url,
            method=method,
            **kwargs
        )
        if URL_BASE + '/login' in resp.url:
            self.login()
            resp = self.__session.request(
                url=URL_BASE + url,
                method=method,
                timeout=timeout,
                **kwargs
            )
        return resp

    @property
    def session(self):
        return self.__session
