import os


class Proxy(object):

    def __init__(self):

        self.proxy_ip = os.getenv("proxy_ip", "")
        self.proxy_port = os.getenv("proxy_port", "")

    def get_proxy(self):
        ip = "{}:{}".format(self.proxy_ip, self.proxy_port)
        return ip
