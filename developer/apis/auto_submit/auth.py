import re
from enum import Enum
from utils.ECBPkcs7 import ECBPkcs7


class Url(Enum):
    key = 'http://stu.hfut.edu.cn/xsfw/sys/emapfunauth/pages/funauth-login.do'
    login = 'http://stu.hfut.edu.cn/xsfw/sys/emapfunauth/loginValidate.do'
    initialize = 'http://stu.hfut.edu.cn/xsfw/sys/swpubapp/indexmenu/getAppConfig.do?appId=5811258723206966&appName=xsyqxxsjapp'
    date = 'http://stu.hfut.edu.cn/xsfw/sys/xsyqxxsjapp/mrbpa/getDateTime.do'
    time = 'http://stu.hfut.edu.cn/xsfw/sys/xsyqxxsjapp/mrbpa/getTsxx.do'
    jbxx = 'http://stu.hfut.edu.cn/xsfw/sys/xsyqxxsjapp/mrbpa/getJbxx.do'
    zxpaxx = 'http://stu.hfut.edu.cn/xsfw/sys/xsyqxxsjapp/mrbpa/getZxpaxx.do'
    save = 'http://stu.hfut.edu.cn/xsfw/sys/xsyqxxsjapp/mrbpa/saveMrbpa.do'


class Daka:
    __headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
    }

    def __init__(self, stu):
        self.__student = stu

    def __getCryptoKey(self):
        data = self.__student.request(Url.key.value).text
        regexp = r'cryptoKey = "(.*)"'
        key = re.findall(regexp, data)[0]
        return key

    def __encryptPwd(self, password):
        key = self.__getCryptoKey()
        return ECBPkcs7(key).encrypt(password)

    def login(self, id, password):
        data = self.__student.request(
            url=Url.login.value,
            method='POST',
            headers=self.__headers,
            data={
                'userName': id,
                'password': self.__encryptPwd(password),
                'isWeekLogin': 'false'
            }
        ).json()
        if 'validate' in data:
            return data['validate'] == 'success'
        else:
            return False
