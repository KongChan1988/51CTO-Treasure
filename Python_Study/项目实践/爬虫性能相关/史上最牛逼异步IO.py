import select
import socket
import time

class AsyncTimeoutException(TimeoutError):
    """
    请求超时异常类
    """

    def __init__(self, msg):
        self.msg = msg
        super(AsyncTimeoutException, self).__init__(msg)


class HttpContext(object):
    """封装请求和相应的基本数据"""

    def __init__(self, sock, host, port, method, url, data, callback, timeout=5):
        """
        sock: 请求的客户端socket对象
        host: 请求的主机名
        port: 请求的端口
        port: 请求的端口
        method: 请求方式
        url: 请求的URL
        data: 请求时请求体中的数据
        callback: 请求完成后的回调函数
        timeout: 请求的超时时间
        """
        self.sock = sock
        self.callback = callback
        self.host = host
        self.port = port
        self.method = method
        self.url = url
        self.data = data

        self.timeout = timeout

        self.__start_time = time.time()
        self.__buffer = []

    def is_timeout(self):
        """当前请求是否已经超时"""
        current_time = time.time()
        if (self.__start_time + self.timeout) < current_time:
            return True

    def fileno(self):
        """请求sockect对象的文件描述符，用于select监听"""
        return self.sock.fileno()

    def write(self, data):
        """在buffer中写入响应内容"""
        self.__buffer.append(data)

    def finish(self, exc=None):
        """在buffer中写入响应内容完成，执行请求的回调函数"""
        if not exc:
            response = b''.join(self.__buffer)
            self.callback(self, response, exc)
        else:
            self.callback(self, None, exc)

    def send_request_data(self):
        content = """%s %s HTTP/1.0\r\nHost: %s\r\n\r\n%s""" % (
            self.method.upper(), self.url, self.host, self.data,)

        return content.encode(encoding='utf8')


class AsyncRequest(object):
    def __init__(self):
        self.fds = []
        self.connections = []

    def add_request(self, host, port, method, url, data, callback, timeout):
        """创建一个要请求"""
        client = socket.socket()
        client.setblocking(False)
        try:
            client.connect((host, port))
        except BlockingIOError as e:
            pass
            # print('已经向远程发送连接的请求')
        req = HttpContext(client, host, port, method, url, data, callback, timeout)
        self.connections.append(req)
        self.fds.append(req)

    def check_conn_timeout(self):
        """检查所有的请求，是否有已经连接超时，如果有则终止"""
        timeout_list = []
        for context in self.connections:
            if context.is_timeout():
                timeout_list.append(context)
        for context in timeout_list:
            context.finish(AsyncTimeoutException('请求超时'))
            self.fds.remove(context)
            self.connections.remove(context)

    def running(self):
        """事件循环，用于检测请求的socket是否已经就绪，从而执行相关操作"""
        while True:
            r, w, e = select.select(self.fds, self.connections, self.fds, 0.05)

            if not self.fds:
                return

            for context in r:
                sock = context.sock
                while True:
                    try:
                        data = sock.recv(8096)
                        if not data:
                            self.fds.remove(context)
                            context.finish()
                            break
                        else:
                            context.write(data)
                    except BlockingIOError as e:
                        break
                    except TimeoutError as e:
                        self.fds.remove(context)
                        self.connections.remove(context)
                        context.finish(e)
                        break

            for context in w:
                # 已经连接成功远程服务器，开始向远程发送请求数据
                if context in self.fds:
                    data = context.send_request_data()
                    context.sock.sendall(data)
                    self.connections.remove(context)

            self.check_conn_timeout()


if __name__ == '__main__':
    def callback_func(context, response, ex):
        """
        :param context: HttpContext对象，内部封装了请求相关信息
        :param response: 请求响应内容
        :param ex: 是否出现异常（如果有异常则值为异常对象；否则值为None）
        :return:
        """
        print(context, response, ex)

    obj = AsyncRequest()
    url_list = [
        {'host': 'www.google.com', 'port': 80, 'method': 'GET', 'url': '/', 'data': '', 'timeout': 5,
         'callback': callback_func},
        {'host': 'www.baidu.com', 'port': 80, 'method': 'GET', 'url': '/', 'data': '', 'timeout': 5,
         'callback': callback_func},
        {'host': 'www.bing.com', 'port': 80, 'method': 'GET', 'url': '/', 'data': '', 'timeout': 5,
         'callback': callback_func},
    ]
    for item in url_list:
        print(item)
        obj.add_request(**item)

    obj.running()
