import socket

class GetIp():


    def get_host_ip(self):
        """
        查询本机ip地址
        :return:
        """
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip


if __name__ == '__main__':
    a = GetIp()
    print(a.get_host_ip()+':'+'9555')

