# -*- coding:utf-8 -*-
# Author:D.Gray
import socket
import selectors
import time,hashlib,os,sys,json
sel = selectors.DefaultSelector()

class MyServer(object):
    def __init__(self):
        pass

    def start(self):
        self.server = socket.socket()
        print('等待链接...')
        self.server.bind(('localhost',6969))
        self.server.listen(100)
        self.server.setblocking(False)
        sel.register(self.server,selectors.EVENT_READ,self.accept)
        while True:
            events = sel.select()
            for key,mask in events:
                callback = key.data
                callback(key.fileobj,mask)


    def accept(self,server,mask):
        conn,addr = server.accept()
        print('已和客户端【%s】建立连接'%(conn))
        conn.setblocking(False)
        sel.register(conn,selectors.EVENT_READ,self.read)

    def read(self,conn,mask):
        data = conn.recv(1024).decode()
        dic = json.loads(data)
        print(dic)
        if hasattr(self,dic['action']):
           func = getattr(self,dic['action'])
           func(dic,conn)

    def put(self,*args):
        dic = args[0]
        path = 'E:\python_work\\51CTO_Python\第四模块学习\Day04\协程'
        i = 0
        while True:
            i += 1
            file_path = os.path.join(path, 'new%s_%s' % (i, dic['filename']))
            with open(file_path,'wb') as f:
                with open(str(dic['file']),'rb') as fr:
                    line = fr.read()
                f.write(line)

start = MyServer()
start.start()




