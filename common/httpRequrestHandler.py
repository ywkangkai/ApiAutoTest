from common import parseUrlHandler as parse_url
from common import logHandler as myLogging
import requests
import configHandler as Config
from common.parseUrlHandler import GetInterfaceUrlPath


class GetApiResult:
    def __init__(self):
        global base_url, username, password, myLogger
        base_url = Config.ConfigSetting().getOneOptions('OBJECT_URL', 'BaseUrl')
        username = Config.ConfigSetting().getOneOptions('SYSTEM_LOGIN', 'username')
        password = Config.ConfigSetting().getOneOptions('SYSTEM_LOGIN', 'password')
        myLogger = myLogging.Logger()

    # 获取get请求反馈json字符串
    @staticmethod
    def get_api_result_get(path, session, data, type_value):
        try:
            url = parse_url.GetInterfaceUrlPath().parse_url_for_get(path, data)
            # 通过登录接口获取cookie,登录接口的cookie在请求的set_cookie中
            headers = {'Cookie': session, 'Content-Type': type_value}
            requests.packages.urllib3.disable_warnings()
            result = requests.get(url, headers=headers, verify=False)
            result.encoding = "utf-8"
            return result
        except Exception as msg:
            myLogger.logger.error(msg)

    # 文件驿站get请求
    @staticmethod
    def file_get(path, data, type_value):
        try:
            url = GetInterfaceUrlPath().file_url_for_get(path, data)
            # 通过登录接口获取cookie,登录接口的cookie在请求的set_cookie中
            headers = {'Content-Type': type_value}
            requests.packages.urllib3.disable_warnings()
            result = requests.get(url, headers=headers, verify=False)
            result.encoding = "utf-8"
            return result
        except Exception as msg:
            myLogger.logger.error(msg)

    # 获取post请求反馈json字符串
    # data为post接口的入参
    @staticmethod
    def get_api_result_post(path, session, data, type_value):
        try:
            url = parse_url.GetInterfaceUrlPath().parse_url_for_post(path)
            # 通过登录接口获取cookie,登录接口的cookie在请求的set_cookie中
            headers = {'cookie': session, 'Content-Type': type_value}
            requests.packages.urllib3.disable_warnings()
            result = requests.post(url, json=data, headers=headers, verify=False)
            result.encoding = "utf-8"
            return result
        except Exception as msg:
            myLogger.logger.error(msg)

    # 文件驿站POST请求
    @staticmethod
    def file_post(path, data, type_value):
        try:
            url = parse_url.GetInterfaceUrlPath().file_url_for_post(path)
            # 通过登录接口获取cookie,登录接口的cookie在请求的set_cookie中
            headers = {'Content-Type': type_value}
            requests.packages.urllib3.disable_warnings()
            result = requests.post(url, json=data, headers=headers, verify=False)
            result.encoding = "utf-8"
            return result
        except Exception as msg:
            myLogger.logger.error(msg)

    # data为post接口的入参（以表单形式提交拼接在URL后）
    @staticmethod
    def get_api_result_form_post(path, session, data, type_value):
        try:
            url = parse_url.GetInterfaceUrlPath().parse_url_for_form_post(path, data)
            # 通过登录接口获取cookie,登录接口的cookie在请求的set_cookie中
            headers = {'cookie': session, 'Content-Type': type_value}
            requests.packages.urllib3.disable_warnings()
            result = requests.post(url, json=data, headers=headers, verify=False)  # .content.decode('utf-8')
            return result
        except Exception as msg:
            myLogger.logger.error(msg)

    # 获取post请求反馈json字符串
    # data为post接口的入参
    # files为需要上传的文件
    @staticmethod
    def get_api_result_post_file(path, session, data, type_value):
        try:
            url = parse_url.GetInterfaceUrlPath().parse_url_for_post(path)
            # files = {'file': open('D:/test.apk', 'rb')} 示例
            # 通过登录接口获取cookie,登录接口的cookie在请求的set_cookie中
            headers = {'cookie': session, 'Content-Type': type_value}
            requests.packages.urllib3.disable_warnings()
            result = requests.post(url, data=data, headers=headers, verify=False)
            return result
        except Exception as msg:
            myLogger.logger.error(msg)

    # 文件驿站post_file请求
    @staticmethod
    def file_post_file(path, data, type_value):
        try:
            url = parse_url.GetInterfaceUrlPath().file_url_for_post(path)
            # files = {'file': open('D:/test.apk', 'rb')} 示例
            # 通过登录接口获取cookie,登录接口的cookie在请求的set_cookie中
            headers = {'Content-Type': type_value}
            requests.packages.urllib3.disable_warnings()
            result = requests.post(url, data=data, headers=headers, verify=False)
            return result
        except Exception as msg:
            myLogger.logger.error(msg)

    # 获取put请求反馈json字符串
    # data为put接口的入参
    @staticmethod
    def get_api_result_put(path, session, data, type_value):
        try:
            url = parse_url.GetInterfaceUrlPath().parse_url_for_post(path)
            # 通过登录接口获取cookie,登录接口的cookie在请求的set_cookie中
            headers = {'cookie': session, 'Content-Type': type_value}
            requests.packages.urllib3.disable_warnings()
            result = requests.put(url, json=data, headers=headers, verify=False)  # .content.decode('utf-8')
            result.encoding = "utf-8"
            return result
        except Exception as msg:
            myLogger.logger.error(msg)

    # 文件驿站put请求
    @staticmethod
    def file_put(path,data, type_value):
        try:
            url = parse_url.GetInterfaceUrlPath().file_url_for_post(path)
            # 通过登录接口获取cookie,登录接口的cookie在请求的set_cookie中
            headers = {'Content-Type': type_value}
            requests.packages.urllib3.disable_warnings()
            result = requests.put(url, json=data, headers=headers, verify=False)  # .content.decode('utf-8')
            result.encoding = "utf-8"
            return result
        except Exception as msg:
            myLogger.logger.error(msg)

    # 获取delete请求反馈json字符串
    @staticmethod
    def get_api_result_delete(path, session, data, type_value):
        try:
            url = parse_url.GetInterfaceUrlPath().parse_url_for_post(path)
            # 通过登录接口获取cookie,登录接口的cookie在请求的set_cookie中
            headers = {'cookie': session, 'Content-Type': type_value}
            requests.packages.urllib3.disable_warnings()
            result = requests.delete(url, json=data, headers=headers, verify=False)
            result.encoding = "utf-8"
            if "success" in result.text:
                # print("delete success")
                return result.text
            else:
                # print('delete fail:' + result.text)
                return result.text
        except Exception as msg:
            myLogger.logger.error(msg)

    # 文件驿站delete请求
    @staticmethod
    def file_delete(path, session, data, type_value):
        try:
            url = parse_url.GetInterfaceUrlPath().file_url_for_post(path)
            # 通过登录接口获取cookie,登录接口的cookie在请求的set_cookie中
            headers = {'cookie': session, 'Content-Type': type_value}
            requests.packages.urllib3.disable_warnings()
            result = requests.delete(url, json=data, headers=headers, verify=False)
            result.encoding = "utf-8"
            if "success" in result.text:
                # print("delete success")
                return result.text
            else:
                print('delete fail:' + result.text)
                return result.text
        except Exception as msg:
            myLogger.logger.error(msg)


if __name__ == '__main__':
    pass