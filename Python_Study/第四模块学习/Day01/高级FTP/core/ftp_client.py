#-*- Coding:utf-8 -*-
# Author: D.Gray
import sys,os,socket,hashlib,time,json
from conf import setting
from core import users
class Ftp_client(object):
    def __init__(self):
        self.client = setting.socket.socket()
        self.client.connect(setting.IP_PORT)
        #self.pwd_path = ''  #定义一个用户当前路径
        self.help_info = {
            "get":"用于下载文件,例如：get readme.txt 即 get 文件名",
            "put":"用于上传文件,例如：put readme.txt 即 put 文件名",
            "dir":"用于提示当前目录下文件详细信息 格式 dir"
        }
        if self.auth():
            self.start()

    def auth(self):
        while True:
            username = input("请输入账户名>>>:").strip()
            password = input('请输入用户密码>>>:').strip()
            if len(username) == 0:
                print('\033[31;1m用户名不得为空\033[0m')
            else:
                auth = 'auth %s %s'%(username,password)
                self.client.send(auth.encode())
                self.user_obj = users.Users(username)
                back_res = self.client.recv(1024).decode()
                if back_res == 'ok':
                    print("认证成功")
                    user = self.user_obj.get_user()
                    self.current_user = username
                    self.password = password
                    self.home_path = user['home']
                    self.pwd_path = os.path.join(setting.USER_HOME,self.home_path, 'user_home')  # 定义个默认路径
                    return True
                elif back_res == "300":
                    print("密码错误")
                elif back_res == '301':
                    print("用户不得同步登录")
                else:
                    print("用户不存在")

    def start(self):
        while True:
            user_inport = input("%s>>>:"%(self.current_user)).strip()
            if len(user_inport) == 0 :continue
            user_inport = user_inport.split()
            if user_inport [0] == 'q':
                break
            if hasattr(self,user_inport[0]):
                func = getattr(self,user_inport[0])
                func(user_inport)
            else:
                print("请输入有效指令\n",self.help_info)
                continue

    def put(self,cmd):
        print(cmd)
        if len(cmd) <2 :
            print("请输入有效指令\n",self.help_info)
        else:
            send_server_info = '%s %s'%(cmd[0],cmd[1])
            self.client.send(send_server_info.encode())
            #file_path =os.path.join(setting.USER_HOME,self.home_path,'user_home',cmd[1])
            file_path = os.path.join(self.pwd_path, cmd[1])

            server_back = self.client.recv(1024).decode()
            print('收到服务器回调指令：',server_back)
            if server_back == "305":
                print('文件不存在')
            else:
                file_total_size = int(server_back)
                print('收到服务器回调文件指令大小:',server_back)
                self.client.send(b'ok')
                revered_size = 0
                self.m = hashlib.md5()
                i = 0

                with open(file_path,'wb') as f:
                    while revered_size < file_total_size:
                        if file_total_size - revered_size <1024:
                            size = file_total_size - revered_size
                        else:
                            size = 1024
                        data = self.client.recv(size)
                        revered_size += len(data)
                        str1 = '已接收文件大小：%sByte'%(revered_size)
                        str2 = '%s%s'%(round((revered_size/file_total_size)*100,2),'%')
                        str3 = '[%s%s]'%('*'*i,str2)
                        sys.stdout.write("\033[32;1m\r%s%s\033[0m"%(str1,str3))
                        sys.stdout.flush()
                        while i < 30:
                            i += 1
                            break
                        time.sleep(0.3)
                        self.m.update(data)
                        f.write(data)
                    self.encryption()

    def get(self,cmd):
        print(cmd)
        if len(cmd) < 2:
            print("请输入有效指令\n",self.help_info)
        else:
            #file_path =os.path.join(setting.USER_HOME,self.home_path,'user_home',cmd[1])
            file_path = os.path.join(self.pwd_path, cmd[1])
            if os.path.isfile(file_path):
                file_total_size = os.stat(file_path).st_size
                send_server_info = '%s %s %s' % (cmd[0], cmd[1],file_total_size)
                self.client.send(send_server_info.encode())
                print('发送上传文件大小：',file_total_size)
                self.client.recv(1024)
                print("接收服务端指令开始上传文件")
                send_size = 0
                self.m = hashlib.md5()
                i = 0
                with open(file_path,'rb')as f:
                    while send_size < file_total_size:
                        if file_total_size - send_size <1024:
                            size = file_total_size - send_size
                            data = f.read(size)
                            send_size += size
                        else:
                            size = 1024
                            data = f.read(size)
                            send_size += len(data)
                        str1 = '已上传 %sByte：' % send_size
                        str2 = "%s%s" % (round((send_size / file_total_size) * 100, 2), '%')
                        str3 = '[%s%s]' % ('*'*i, str2)
                        sys.stdout.write('\033[32;1m\r%s%s\033[0m' % (str1,str3))
                        sys.stdout.flush()
                        while i < 30:  #大文件*号打印个数限制
                            i += 1
                            break
                        time.sleep(0.3)
                        self.m.update(data)
                        self.client.send(data)
                    self.encryption()
            else:
                print('文件不存在')

    def encryption(self):
        md5 = input("\n文件已接收是否需加密认证按q取消加密>>>:")
        if md5 != 'q':
            file_md5 = self.m.hexdigest()
            self.client.send(b"encryption")
            print("发送加密认证")
            server_recv_md5 = self.client.recv(1024).decode()
            print('下载文件加密:%s\n服务端文件加密:%s' % (file_md5, server_recv_md5))
            if file_md5 == server_recv_md5:
                print('加密认证成功')
            else:
                print('加密认证失败')
        else:
            self.client.send(b'q')
            print("\n取消加密认证文件接收完毕")

    def dir(self,cmd):
        print(cmd)
        send_server_info = '%s'%cmd[0]
        self.client.send(send_server_info.encode())
        server_back = self.client.recv(1024).decode()
        print('收到服务端回调指令大小:',server_back)
        self.client.send("ok".encode())
        revered_size = 0
        revered_data = b''
        while revered_size < int(server_back):
            data = self.client.recv(1024)
            revered_data += data
            revered_size = len(data)
            print('实际收到指令大小:',revered_size)
        else:
            print(revered_data.decode())

    def mkdir(self,cmd):
        if len(cmd) <2:
            print("请输入有效指令:\n",self.help_info)
        else:
            file_path = os.path.join(self.pwd_path,cmd[1])
            if not os.path.isdir(file_path):
                os.mkdir(file_path)
                print("目录创建成功")
            else:
                print("该路径下已有该目录")

    def cd(self,cmd):
        if len(cmd) <2:
            print("请输入有效指令:\n",self.help_info)
        else:
            if cmd[1] == '..':
                list = []
                path = self.pwd_path
                for index in path.split('\\'):
                    list.append(index)
                list[0] = '%s%s' % (list[0], '/')
                if list[-1] == 'user_home':
                    print("已在根目录下")
                else:
                    self.pwd_path = ''
                    del list[-1]
                    for index in list:
                        self.pwd_path = os.path.join(self.pwd_path,index)
                    print('当前路径:', self.pwd_path)
            elif cmd[1] == '/':
                self.pwd_path = os.path.join(setting.USER_HOME,self.home_path,"user_home")
                print('当前路径:', self.pwd_path)
            else:
                pwd_path = os.path.join(self.pwd_path,cmd[1])
                if os.path.exists(pwd_path):
                    self.pwd_path = pwd_path
                    print('当前路径:',self.pwd_path)
                    print(os.listdir(self.pwd_path))
                else:
                    print("不是有效路径")

    def pwd(self,cmd):
        if len(cmd) >1:
            print("请输入有效指令:\n",self.help_info)
        else:
            if os.path.isdir(self.pwd_path):
                print('当前路径:',self.pwd_path)
                print(os.listdir(self.pwd_path))
            else:
                print("默认家目录路径：",self.pwd_path)

    def help(self,cmd):
        print(cmd)
        h = self.help_info
        if len(cmd) == 1:
            for k,v in h.items():
                print(k,v)
        else:
            print('%s %s'%(cmd[1],h[cmd[1]]))
