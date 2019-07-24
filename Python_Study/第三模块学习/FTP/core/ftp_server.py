# -*- coding:utf-8 -*-
# Author:D.Gray
import os,sys,socket
from conf import setting
from core import ftp_client
from core import users

class FTP_server(object):
    def __init__(self):
        self.server = setting.socket.socket()
        self.server.bind(setting.IP_PORT)
        self.server.listen(5)
        self.user_obj = users.Users()  #导入users文件并实例化Users类
        self.start()

    def start(self):
        print("等待链接中...")
        while True:
            self.conn,self.addr = self.server.accept()
            print("一个新的链接:%s %s"%(self.conn,self.addr))
            while True:
                self.data = self.conn.recv(1024)  #接受客户端格式化输出内容
                #print('data:',self.conn)
                if not self.data:
                    print("客户端断开")
                    break
                cmd_res = self.data.decode().split() #以列表形式获取用户输入的[[方法名],[文件名]]
                cmd_action = cmd_res[0]     #获取方法名
                #print('in the start获取方法名:',cmd_action)
                if hasattr(self,cmd_action):    #判断用户输入的方法名是否存在
                    func = getattr(self,cmd_action) #执行对应的方法函数
                    func(cmd_res)   #用户输入的[[方法名],[文件名]]传给方法函数
                else:
                    print("\033[31;1m请输入有效命令\033[0m")

    def auth(self,cmd):
        #print('auth:',cmd) #接受客户端格式化输出的 auth 用户名 密码
        user = self.user_obj.get_user(cmd[1])   #调用Users类中get_user方法，并把cmd[1](用户名)传参给get_user方法
        print('in the ftp_server_auth:',user)
        if user:
            if user['password'] == cmd[2]:
                self.current_user = user
                self.current_path = user["home"]
                self.user_home = setting.USER_HOME
                self.conn.send(b"ok")
            else:
                self.conn.send(b"Not password")
        else:
            self.conn.send(b'Not username')

    def put(self,cmd):
        '''
        上传文件函数
        :param cmd: 接收用户输入的[[方法名],[文件名]]
        :return:
        '''
        #print('in the put:',cmd)
        file_name_path = self.user_home + self.current_path +'\server_home\\'+ cmd[1]
        print('文件路径',file_name_path)
        if os.path.isfile(file_name_path):
            file_totle_size = os.stat(file_name_path).st_size #查看文件大小
            self.conn.send(str(file_totle_size).encode())   #将文件大小发送给客户端
            self.conn.recv(1024)    #接收客户端消息
            with open(file_name_path,'rb') as f:
                for line in f:      #循环遍历文件内容
                    self.conn.send(line)    #并将文件内容发送给客户端
            print("send done>>>")
        else:
            print('\033[31;1m文件不存在\033[0m')
            self.conn.send('302'.encode())

    def get(self,cmd):
        '''
        接收客户端上传文件函数
        :param cmd:
        :return:
        '''
        print(cmd)
        file_path = self.user_home + self.current_path + '\server_home\\' + cmd[1]  #文件路径
        file_totle_size = cmd[2]    #接收客户端上传文件大小
        file_totle_size = int(file_totle_size)
        with open(file_path,'wb') as f:
            self.conn.send('300'.encode())  #返回客户端参数300
            revered_file_size = 0   #初始接收文件大小
            while revered_file_size < file_totle_size:  #开始接收客户端上传文件
                if file_totle_size - revered_file_size <= 1024:
                    size = file_totle_size-revered_file_size
                else:
                    size = 1024
                data = self.conn.recv(size)
                revered_file_size += len(data)
                f.write(data)
            else:
                print("文件接收完毕")

    def dir(self,cmd):
        '''
        查看服务端目录文件信息函数
        :param cmd:
        :return:
        '''
        print(cmd)
        file_path = self.user_home + self.current_path + '\server_home\\'
        res = os.popen('%s %s'%(cmd[0],file_path)).read()
        print('服务端文件目录信息：',res)
        if len(res) == 0 :
            res = 'cmd has not output'
        self.conn.send(str(len(res)).encode()) #服务端发送目录文件大小给客户端
        self.conn.recv(1024)    #接收客户端回调信息 "ok"
        self.conn.send(res.encode()) #服务端发送目录文件信息给客户端





