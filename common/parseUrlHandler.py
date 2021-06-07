import configHandler as Configer
from common import logHandler as myLogging


class GetInterfaceUrlPath:
    def __init__(self):
        global base_url, myLogger,file_url
        myLogger = myLogging.Logger()
        base_url = Configer.ConfigSetting().getOneOptions('OBJECT_URL', 'BaseUrl')
        file_url = Configer.ConfigSetting().getOneOptions('OBJECT_URL', 'FileUrl')
    # 拼接GET地址方法
    # data为一个dict，主要提供接口入参data = {"参数"：值(变量）}
    # path具体在某个接口用例中传入
    # 当遇到无参数的接口data可以传入空字典，如data = {}
    def parse_url_for_get(self, path, data):
        try:
            item = data.items()
            urls = '?'
            for i in item:
                (key, value) = i
                temp = key + "=" + str(value)
                urls = urls + temp + "&"
            urls = urls.rstrip('&')
            full_urls = base_url + path + urls
            return full_urls
        except Exception as msg:
            myLogger.logger.error(msg)

     #文件驿站get请求
    def file_url_for_get(self, path, data):
        try:
            item = data.items()
            urls = '?'
            for i in item:
                (key, value) = i
                temp = key + "=" + str(value)
                urls = urls + temp + "&"
            urls = urls.rstrip('&')
            full_urls = file_url + path + urls
            return full_urls
        except Exception as msg:
            myLogger.logger.error(msg)

    # 拼接POST，PUT,DELETE地址方法
    def parse_url_for_post(self, path):
        try:
            full_url = base_url + str(path)
            return full_url
        except Exception as msg:
            myLogger.logger.error(msg)


    #文件驿站post请求
    def file_url_for_post(self, path):
        try:
            full_url = file_url + str(path)
            return full_url
        except Exception as msg:
            myLogger.logger.error(msg)

    def parse_url_for_form_post(self, path, data):
        try:
            item = data.items()
            urls = '?'
            for i in item:
                (key, value) = i
                temp = key + "=" + str(value)
                urls = urls + temp + "&"
            urls = urls.rstrip('&')
            full_urls = base_url + path + urls
            return full_urls
        except Exception as msg:
            myLogger.logger.error(msg)


if __name__ == "__main__":
    pass
    # path = '/meeting/ext/vote/list'
    # data = {"pageNum": 1, 'pageSize': 20000, "meetingId": '6f351b42dcd54d8e92742ebd551396bc'}
    # url = GetInterfaceUrlPath().parse_url_for_get(path, data)
    # print(url)
