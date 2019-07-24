# -*- coding:utf-8 -*-
# Author:D.Gray
import socket
import selectors
import os,sys,time,json

class MyClient(object):
    def __init__(self):
        self.client = socket.socket()

    def start(self):
        self.client.connect(('localhost',6969))
        while True:
            meg = input('>>>:').strip().split()
            if len(meg) == 0:continue
            if len(meg) >= 2:
                dic = {
                    'action':meg[0],
                    'filename':meg[1]
                }
                if hasattr(self,meg[0]):
                    func = getattr(self,meg[0])
                    func(dic)
                else:
                    print('请输入有效操作指令')

    def put(self,*args):
        dic = args[0]
        print('in the put:',dic)
        path = 'E:\python_work\\51CTO_Python\第四模块学习\Day04\协程'
        file_path = os.path.join(path,str(dic['filename']))
        if os.path.isfile(file_path):
            file_totle_size = os.stat(file_path).st_size
            dic['file'] = file_path
            self.client.send(json.dumps(dic).encode())


        else:
            print('未找到该文件')

start = MyClient()
start.start()