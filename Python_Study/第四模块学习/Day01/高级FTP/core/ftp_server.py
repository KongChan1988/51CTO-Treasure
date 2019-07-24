#-*- Coding:utf-8 -*-
# Author: D.Gray
import sys,os,socket,hashlib,socketserver,json
from conf import setting
from core import users
class MyServer(socketserver.BaseRequestHandler):
    print('等待链接...')
    def auth(self,*args):
        cmd = args[0]
        self.user_obj = users.Users(cmd[1])
        auth_user = self.user_obj.get_user()
        print('in the auth_user:',auth_user)
        if auth_user:
            if auth_user["password"] == cmd[2]:
                if auth_user['status'] == 0:
                    self.request.send(b"ok")
                    #self.user_obj.update_status()
                    self.user_home = auth_user["home"]
                else:
                    self.request.send(b'301')
                    print("用户不得同步登录")
            else:
                self.request.send(b"300")
                print('300:密码错误')
        else:
            self.request.send(b"302")
            print("用户不存在")

    def put(self,cmd):
        file_path = os.path.join(setting.USER_HOME,self.user_home,"server_home",cmd[1])
        if os.path.isfile(file_path):
            file_total_size = os.stat(file_path).st_size
            self.request.send(str(file_total_size).encode())
            self.request.recv(1024)
            self.m = hashlib.md5()
            with open(file_path,'rb') as f:
                for line in f:
                    self.m.update(line)
                    self.request.send(line)
                self.encryption()
        else:
            self.request.send(b'305')
            print("文件不存在")

    def get(self,cmd):
        file_path = os.path.join(setting.USER_HOME,self.user_home,'server_home',cmd[1])
        file_total_size = cmd[2]
        file_total_size = int(file_total_size)
        with open(file_path,'wb')as f:
            self.request.send(b'ok')
            print("开始接收客户端文件")
            rever_size = 0
            self.m = hashlib.md5()
            while rever_size < file_total_size:
                if file_total_size - rever_size <1024:
                    size = file_total_size-rever_size
                else:
                    size = 1024
                data = self.request.recv(size)
                rever_size += len(data)
                f.write(data)
                self.m.update(data)
            self.encryption()

    def encryption(self):
        encryption_recv = self.request.recv(1024).decode()
        print('接收客户端加密认证:', encryption_recv)
        if encryption_recv == "encryption":
            server_file_md5 = self.m.hexdigest()
            print('in the server_file_md5:', server_file_md5)
            self.request.send(server_file_md5.encode())
        else:
            print('取消加密文件发送完成')


    def dir(self,cmd):
        file_path = os.path.join(setting.USER_HOME,self.user_home,"server_home")
        res = os.popen('%s %s'%(cmd[0],file_path)).read()
        print(res)
        if len(res) == 0:
            res = 'has not output'
        self.request.send(str(len(res.encode())).encode())
        self.request.recv(1024)
        self.request.send(res.encode())

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{}客户端已链接".format(self.client_address))
                actin_list = self.data.decode().split()
                action = actin_list[0]
                print('in the handle:',action)
                if hasattr(self,str(action)):
                    func = getattr(self,str(action))
                    func(actin_list)
            except ConnectionResetError as e:
                print("%s客户端已断开%s"%(self.client_address,e))
                break

server = socketserver.ThreadingTCPServer((setting.IP_PORT),MyServer)
server.serve_forever()

