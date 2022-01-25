import os, sys
parent_path = os.path.abspath('.')
sys.path.append(parent_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hfutgo.settings")
import django
django.setup()

import requests, re, json
from datetime import time, datetime
from enum import Enum
from developer.daka_task.Student import Student
from utils.ECBPkcs7 import ECBPkcs7
from config import UserInfo
from developer.models import DakaLog

class Url(Enum):
    key = 'http://stu.hfut.edu.cn/xsfw/sys/emapfunauth/pages/funauth-login.do'
    login = 'http://stu.hfut.edu.cn/xsfw/sys/emapfunauth/loginValidate.do'
    previous = 'http://stu.hfut.edu.cn/xsfw/sys/swmxsyqxxsjapp/modules/mrbpa/getStuXx.do'
    submit = 'http://stu.hfut.edu.cn/xsfw/sys/swmxsyqxxsjapp/modules/mrbpa/saveStuXx.do'
    page = 'http://stu.hfut.edu.cn/xsfw/sys/swmxsyqxxsjapp/*default/index.do'
    initialize = 'http://stu.hfut.edu.cn/xsfw/sys/emappagelog/config/swmxsyqxxsjapp.do'
    initialize2 = 'http://stu.hfut.edu.cn/xsfw/sys/swpubapp/MobileCommon/setAppRole.do'
    initialize3 = 'http://stu.hfut.edu.cn/xsfw/sys/swmxsyqxxsjapp/modules/mrbpa/getSetting.do'

def date():
    return datetime.now().date().isoformat()


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

    def __init__(self):
        self.__student = Student()

    def __getCryptoKey(self):
        data = self.__student.request(Url.key.value).text
        regexp = r'cryptoKey = "(.*)"'
        key = re.findall(regexp, data)[0]
        return key

    def __encryptPwd(self, password):
        key = self.__getCryptoKey()
        return ECBPkcs7(key).encrypt(password)

    def __login(self, id, password):
        self.id = id
        return self.__student.login(id, password)

    def __initialize(self):
        data = self.__student.request(Url.page.value)
        data = self.__student.request(Url.initialize.value)
        data = self.__student.request(
            url=Url.initialize2.value,
            method='POST',
            data={'data': '{"APPID":"5811260348942403","APPNAME":"swmxsyqxxsjapp","ROLEID":"771cf22ed4db4a11827f0dd19ca3e38d"}'}
        )
        data = self.__student.request(
            url=Url.initialize3.value,
            method='POST',
            data={'data': '{}'}
        )

    def previous(self):
        data = self.__student.request(
            url=Url.previous.value,
            method='POST',
            headers=self.__headers,
            data={
                'data': json.dumps({
                    'TBSJ': date()
                })
            }
        ).json()
        if data['code'] == '0':
            return data['data']
        else:
            return False

    def __save(self):
        previous = self.previous()
        data = {
            'data': json.dumps({
                **previous,
                'TBSJ': date(),
                'GCKSRQ': '',
                'GCJSRQ': '',
                'DFHTJHBSJ': '',
                'BY1': '1',
                'DZ_TBDZ': '合肥工业大学',
                'WID': date() + '-' + self.id,
                'DZ_SFSB': '1'
            })
        }
        data = self.__student.request(
            url=Url.submit.value,
            method='POST',
            headers=self.__headers,
            data=data
        ).json()
        if data['code'] == '0':
            return True
        else:
            return data['msg']

    def run(self, id, password):
        try:
            logined = self.__login(id, password)
        except requests.exceptions.RequestException:  # 你HFUT又双叒封网辣
            return "连接失败，可能又封网了！"
        except:
            return "未知错误，可能又封网了！"
        try:
            if logined is True:
                print("登录成功")
                self.__initialize()
                saved = self.__save()
                if saved == True:
                    return '打卡成功'
                else:
                    return '打卡失败！' + saved
            else:
                return '帐号或密码错误！'
        except Exception as e:
            print(e)
            return '因不明原因打卡失败'


if __name__ == '__main__':
    for user in UserInfo.users.value:
        if user['enable']:
            try:
                daka = Daka()
                print("当前打卡：" + user['user'])
                status = daka.run(user['user'], user['password'])
                print(status)
                DakaLog(user=user['user'], status=1, log=status).save()
            except Exception as e:
                print(e)
                DakaLog(user=user['user'], status=0, log='因不明原因打卡失败').save()
