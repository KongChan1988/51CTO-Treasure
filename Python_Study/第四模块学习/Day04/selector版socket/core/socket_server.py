# -*- coding:utf-8 -*-
# Author:D.Gray
import selectors
import socket,os,json,errno,hashlib,time
from conf import setting
sel = selectors.DefaultSelector()


class MyServer(object):
    def __init__(self):
        self.server = socket.socket()

    def start(self):
        '''
        启动函数
        :return:
        '''
        print('等待链接...')
        self.server.bind(setting.LOCAL_HOST)
        self.server.listen(100)
        self.server.setblocking(False)
        self.register()

    def register(self):
        '''
        注册函数
        :return:
        '''
        sel.register(self.server,selectors.EVENT_READ,self.accept)
        while True:
            events = sel.select()
            for k,mask in events:
                callback = k.data
                callback(k.fileobj,mask)

    def accept(self,server,mask):
        '''
        服务器监听函数
        :param server:
        :param mask:
        :return:
        '''
        conn,self.addr = server.accept()
        print('\033[32;1m已和客户端[%s]建立了链接\033[0m'%(conn))
        conn.setblocking(False)
        sel.register(conn,selectors.EVENT_READ,self.read)

    def read(self,conn,mask):
        '''
        接收客户端信息函数
        :param conn:
        :param mask:
        :return:
        '''
        data = conn.recv(1024)
        #print('in the read conn:',conn)
        if data:
            action_dic = json.loads(data) #序列化data={'action':xxx}
            print('\033[35;1m收到客户端操作指令:%s\033[0m'%action_dic['action'])
            if hasattr(self,str(action_dic['action'])):
                action = getattr(self,str(action_dic['action']))
                action(action_dic,conn)  #此时传参一定要用conn,千万不能传self.conn 多并发时会出现异常
        else:
            print('\033[31;1m客户端已断开\033[0m')
            conn.unregister(conn)   #关闭客户端链接
            conn.close()

    def put(self,*args):
        '''
        服务端接收客户端文件函数
        :param args:
        :return:
        '''
        conn = args[1] #客户端链接地址
        dic = args[0]   #操作字典
        file_path = os.path.join(setting.SERVER_PATH,dic['filename'])
        print('\033[34;1m已收到客户端传来的文件相关信息:\n%s\033[0m'%dic)
        conn.send(b'100')
        print('\033[35;1m发送回调给客户端:100\033[0m')
        print('开始接收客户端文件')
        self.m = hashlib.md5()
        with open(file_path,'wb') as f:
            with open(dic['file'],'rb')as fr:
                line = fr.read()
            f.write(line)
            self.m.update(line)
        self.encryption(conn)


    def get(self,*args):
        '''
        服务端上传文件至客户端函数
        :param args:
        :return:
        '''
        conn = args[1]
        dic = args[0]
        print('in the get:',dic)
        file_path = os.path.join(setting.SERVER_PATH,dic['filename'])
        if os.path.isfile(file_path):
            file_totle_size = os.stat(file_path).st_size
            conn.send(str(file_totle_size).encode())
            print('开始发送文件给客户端')
            self.m = hashlib.md5()
            with open(file_path,'rb') as f:
                for line in f:
                    self.m.update(line)
                    conn.send(line)
                self.encryption(conn)
        else:
            conn.send(b'204')
            print('未找到该文件')

    def encryption(self,*args):
        '''
        加密函数
        :param args:
        :return:
        '''
        conn = args[0]
        server_md5 = self.m.hexdigest()
        conn.send(str(server_md5).encode())
        print('文件操作完成并发送加密信息【%s】至客户端' % server_md5)

