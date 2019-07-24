# -*- coding:utf-8 -*-
# Author:D.Gray
import os,sys,socket
from conf import setting
from core import ftp_server
from core import users
class FTP_client(object):
    def __init__(self):
        self.client = setting.socket.socket()
        self.client.connect(setting.IP_PORT)
        self.user_obj = users.Users()
        self.help_info = {
            "get":"用于上传文件，例如：get readme.txt 即 get 文件名",
            "put":"用于下载文件，例如：put readme.txt 即 put 文件名",
            'dir':"用于显示当前目录下文件或文件详细信息 格式 ls "
        }
        if self.auth():
            self.start()

    def auth(self):
        '''
        用户登录验证函数
        :return:
        '''
        while True:
            username = input("请输入用户名>>>:").strip()
            pwd = input("请输入用户密码>>>:").strip()
            auth_info = 'auth %s %s'%(username,pwd)  #格式化输出 auth 用户名 密码
            self.client.send(auth_info.encode())    #将格式化后的内容发送给服务端
            back_res = self.client.recv(1024).decode()
            if back_res == "ok":
                print('认证成功')
                user = self.user_obj.get_user(username)
                self.current_user = username
                self.current_pwd = pwd
                self.current_path = user['home']
                self.current_dir = back_res[1]
                return  True
            elif back_res == "Not password":
                print("\033[31;1m密码不正确\033[0m")
            else:
                print("\033[31;1m用户不存在\033[0m")

    def start(self):
        '''
        输入指令上传下载文件函数
        :return:
        '''
        while True:
            user_input = input('%s>>>:'%self.current_user).strip()
            if len(user_input) == 0:continue
            user_input = user_input.split()
            if user_input[0] == 'q':break
            if hasattr(self,user_input[0]):
                func = getattr(self,user_input[0])
                func(user_input)
            else:
                print("\033[31;1m请输入有效指令\033[0m")
                continue

    def put(self,cmd):
        '''
        从服务器端下载文件函数
        :param cmd:
        :return:
        '''
        print('in the put:',cmd)
        send_server_info = '%s %s'%(cmd[0],cmd[1])  #格式化输出['方法','文件名']
        self.client.send(send_server_info.encode()) #将格式化输出内容发送给服务器端
        server_back = self.client.recv(1024).decode()   #接收服务器回调结果
        print("接收服务器回调信息：",server_back)
        if server_back == "302":
            print('\033[31;1m文件不存在\033[0m')
        else:
            file_totle_size = int(server_back)  #从服务器端接收文件大小
            print("您要下载的文件大小为：%sByte"%file_totle_size)
            self.client.send('可以开始下载了...'.encode())
            rever_file_size = 0 #接收到的文件大小
            file_name_path = setting.USER_HOME + self.current_path + '\\user_home\\' + cmd[1]
            #print(file_name_path)
            with open(file_name_path,"wb") as f:
                while rever_file_size < file_totle_size:
                    if file_totle_size - rever_file_size < 1024:  #当剩余文件大小<1024 全部接收文件
                        size = file_totle_size - rever_file_size
                    else:
                        size = 1024
                    data = self.client.recv(size)   #当剩余文件<1024全部接收文件，当剩余文件>1024每次只接收1024
                    rever_file_size += len(data)    #每次接收数据时自动累计rever_file_size值
                    print("已接收%sByte"%rever_file_size)
                    f.write(data)
                else:
                    print('接受完毕')

    def get(self,cmd):
        '''
        本地上次文件给服务器端
        :param cmd: 接收用户通过start函数输入的操作指令
        :return:
        '''
        print(cmd)
        file_path = setting.USER_HOME + self.current_path +'\\user_home\\' + cmd[1]
        if os.path.isfile(file_path):
            file_totle_size = os.stat(file_path).st_size
            print('您要上传文件大小为【%sByte】'%file_totle_size)
            file_info = '%s %s %s'%(cmd[0],cmd[1],file_totle_size) #格式化输出['操作指令','文件名','文件大小']
            self.client.send(file_info.encode())    #将格式化输出内容发送给服务器端
            server_back = self.client.recv(1024).decode()   #接收回调信息
            if server_back == "300":
                print('可以上传文件了...')
                send_file_size = 0
                with open(file_path,'rb') as f:
                    while send_file_size != file_totle_size:
                        if file_totle_size-send_file_size <= 1024:
                            data = f.read(file_totle_size-send_file_size)
                            send_file_size += file_totle_size - send_file_size
                        else:
                            data = f.read(1024)
                            send_file_size += len(data)
                        print("已上传【%sByte】"%send_file_size)
                        self.client.send(data)
                    print("上传成功")
        else:
            print('\033[31;1m文件不存在\033[0m')

    def dir(self,cmd):
        '''
        查看服务端目录文件信息
        :param cmd:
        :return:
        '''
        print(cmd)
        send_server_info = '%s'%cmd[0]  #格式化输出用户指令
        self.client.send(send_server_info.encode())
        server_back = self.client.recv(1024).decode()   #接收服务端回调
        print("获取服务端回调信息:%s"%server_back)
        self.client.send("ok".encode())   #发送给服务端'ok'
        recv_size = 0
        recv_data = b''
        while recv_size < int(server_back):
            data = self.client.recv(1024)
            recv_data += data
            recv_size = len(data)
            print(recv_size)
        else:
            print(recv_data.decode())


    def help(self,cmd):
        '''
        查看帮助文档函数
        :param cmd:
        :return:
        '''
        print(cmd)
        d = self.help_info
        print(d)