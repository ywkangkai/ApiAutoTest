from common import parseUrlHandler as parse_url
import requests
from common import logHandler as myLogging
import configHandler as Configer


class GetCookieResult:
    # 通过登录接口获取登录接口中的set_cookie值
    def __init__(self):
        global base_url, username, password, super_username, super_password, meeting_user1, meeting_password1, \
            myLogger, meeting_user2, meeting_password2, meeting_user3, meeting_password3,meeting_user4, \
            meeting_password4,meeting_user5, meeting_password5
        base_url = Configer.ConfigSetting().getOneOptions('OBJECT_URL', 'BaseUrl')
        username = Configer.ConfigSetting().getOneOptions('SYSTEM_LOGIN', 'username')
        password = Configer.ConfigSetting().getOneOptions('SYSTEM_LOGIN', 'password')
        super_username = Configer.ConfigSetting().getOneOptions('SYSTEM_LOGIN', 'super_username')
        super_password = Configer.ConfigSetting().getOneOptions('SYSTEM_LOGIN', 'super_password')
        meeting_user1 = Configer.ConfigSetting().getOneOptions('SYSTEM_LOGIN', 'meeting_user1')
        meeting_password1 = Configer.ConfigSetting().getOneOptions('SYSTEM_LOGIN', 'meeting_password1')
        meeting_user2 = Configer.ConfigSetting().getOneOptions('SYSTEM_LOGIN', 'meeting_user2')
        meeting_password2 = Configer.ConfigSetting().getOneOptions('SYSTEM_LOGIN', 'meeting_password2')
        meeting_user3 = Configer.ConfigSetting().getOneOptions('SYSTEM_LOGIN', 'meeting_user3')
        meeting_password3 = Configer.ConfigSetting().getOneOptions('SYSTEM_LOGIN', 'meeting_password3')
        meeting_user4 = Configer.ConfigSetting().getOneOptions('SYSTEM_LOGIN', 'meeting_user4')
        meeting_password4 = Configer.ConfigSetting().getOneOptions('SYSTEM_LOGIN', 'meeting_password4')
        meeting_user5 = Configer.ConfigSetting().getOneOptions('SYSTEM_LOGIN', 'meeting_user5')
        meeting_password5 = Configer.ConfigSetting().getOneOptions('SYSTEM_LOGIN', 'meeting_password5')
        myLogger = myLogging.Logger()

    def get_login_cookie(self):
        result = ''
        try:
            path = "/mock/login/signIn"
            param = {
                "account": username,
                "password": password
            }
            url = parse_url.GetInterfaceUrlPath().parse_url_for_post(path)
            requests.packages.urllib3.disable_warnings()
            get_cookie = requests.post(url, data=param, verify=False).cookies
            dict_result = get_cookie.get_dict()
            for i in range(len(dict_result)):
                for key in dict_result:
                    if key == "JSESSIONID":
                        result = str(key) + '=' + str(dict_result[key])
                        print(result)
            return result
        except Exception as msg:
            myLogger.logger.error(msg)

    def get_super_admin_cookie(self):
        result = ''
        try:
            path = "/mock/login/signIn"
            param = {
                "account": super_username,
                "password": super_password
            }
            url = parse_url.GetInterfaceUrlPath().parse_url_for_post(path)
            requests.packages.urllib3.disable_warnings()
            get_cookie = requests.post(url, data=param, verify=False).cookies
            dict_result = get_cookie.get_dict()
            for i in range(len(dict_result)):
                for key in dict_result:
                    if key == "JSESSIONID":
                        result = str(key) + '=' + str(dict_result[key])
                        print(result)
            return result
        except Exception as msg:
            myLogger.logger.error(msg)

    def get_manager_cookie(managerSession):
        def wapper(*args):
            result = ''
            try:
                path = "/mock/login/signIn"
                param = managerSession(*args)
                url = parse_url.GetInterfaceUrlPath().parse_url_for_post(path)
                requests.packages.urllib3.disable_warnings()
                get_cookie = requests.post(url, data=param, verify=False).cookies
                dict_result = get_cookie.get_dict()
                for i in range(len(dict_result)):
                    for key in dict_result:
                        if key == "JSESSIONID":
                            result = str(key) + '=' + str(dict_result[key])
                            print(dict_result)
                return result
            except Exception as msg:
                myLogger.logger.error(msg)
        return wapper
        
    @get_manager_cookie
    def managerSession(self,number):
        if number == 1:
            param = {
                "account": meeting_user1,
                "password": meeting_password1
            }
        elif number == 2:
            param = {
                "account": meeting_user2,
                "password": meeting_password2
            }
        elif number == 4:
            param = {
                "account": meeting_user4,
                "password": meeting_password4
            }
        elif number == 5:
            param = {
                "account": meeting_user5,
                "password": meeting_password5
            }
        else:
            param = {
                "account": meeting_user3,
                "password": meeting_password3
            }

        return param


if __name__ == '__main__':
    GetCookieResult().get_login_cookie()
