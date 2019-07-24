# -*- coding:utf-8 -*-
# Author:D.Gray
import selectors
import socket,json,os,hashlib,sys,time
from conf import setting


class MyClient(object):
    def __init__(self):
        self.client = socket.socket()
        self.client.connect(setting.LOCAL_HOST)
        self.run = self.run()

    def run(self):
        '''
        启动函数
        :return:
        '''
        while True:
            help = '''\033[33;1m
                        "get":"用于下载文件,例如：get readme.txt 即 get 文件名"
                        "put":"用于上传文件,例如：put readme.txt 即 put 文件名"
            \033[0m'''
            print(help)
            meg = input('root@selectors_client>>>:').strip().split()
            if len(meg) == 0:continue
            if len(meg) >= 2:
                dic = {
                    'action':meg[0],
                    'filename':meg[1],
                    'filesize':0
                }
                if hasattr(self,str(dic['action'])):
                    action = getattr(self,str(dic['action']))
                    action(dic)
                else:
                    print('\033[31;1m请输入有效操作指令\033[0m')
            else:
                print('\033[31;1m请输入有效操作指令\033[0m')

    def put(self,*args):
        '''
        上传文件至服务端函数
        :param args:
        :return:
        '''
        args = args[0] # args = {'action':put,'filename':xxx}
        print('in the put:',args)
        file_path = os.path.join(setting.HOME_PATH,args['filename'])
        if os.path.isfile(file_path):
            args['file'] = file_path   #在字典中增加 文件大小键值对
            self.client.send(json.dumps(args).encode())  # 字典序列化上传
            print('\033[34;1m发送文件相关信息至服务端:\n%s\033[0m' % args)
            recv_server = self.client.recv(1024)        #接收服务端回调：允许客户端上传文件参数
            if recv_server.decode() == '100':
                print('\033[35;1m收到服务回调信息:%s\033[0m'%recv_server.decode())
                print('开始上传文件...')
                self.m = hashlib.md5()
                with open(file_path, 'rb') as f:
                    data = f.read()
                    '''
                    加密认证
                    '''
                    self.m.update(data)
                    self.encryption()
            else:
                print('\033[31;1m收到服务端异常回调信息\033[0m',recv_server.decode())
        else:
            print('\033[31;1m未找到该文件\033[0m')


    def get(self,*args):
        dic = args[0]
        self.client.send(json.dumps(dic).encode())
        server_recv = self.client.recv(1024)        #获取服务端回调参数或文件大小
        if server_recv.decode() != '204':
            print('收到服务端发送过来的文件大小[%s bytes]'%server_recv.decode())
            file_path = os.path.join(setting.HOME_PATH,dic['filename'])
            print('开始接受文件')
            file_totle_size = int(server_recv.decode())
            self.m = hashlib.md5()
            recv_size = 0
            i = 0
            with open(file_path,'wb') as f:
                while recv_size < file_totle_size:
                    if file_totle_size - recv_size < 1024:
                        size = file_totle_size - recv_size
                    else:
                        size = 1024
                    data = self.client.recv(size)
                    self.m.update(data)
                    f.write(data)
                    recv_size += len(data)
                    '''
                    进度条
                    '''
                    str1 = '已下载 %s Bytes' % recv_size
                    str2 = '%s%s' % (round((recv_size / file_totle_size) * 100, 2), '%')
                    str3 = '[%s%s]' % ('*' * i, str2)
                    sys.stdout.write('\033[32;1m\r%s%s\033[0m' % (str1, str3))
                    sys.stdout.flush()
                    i += 2
                    time.sleep(1)
                    '''
                    加密认证
                    '''
                self.encryption()
        else:
            print('服务端未找到该文件')


    def encryption(self):
        '''
        文件加密函数
        :return:
        '''
        enc = input('\n文件已上传是否需要加密（n取消加密）>>>:')
        if enc == 'n':
            self.client.recv(1024)     #因服务端无论客户端是否选择加密都会发送加密消息过来，所以这里也必须接受下防止粘包
            print('已取消加密文件上传成功')
        else:
            file_md5 = self.m.hexdigest()
            server_md5 = self.client.recv(1024)     #接受服务端文件加密信息
            print("\033[32;1m本地文件加密:%s\n服务端文件加密:%s\033[0m" % (file_md5 ,server_md5.decode()))
            if file_md5 == server_md5.decode():
                print("\033[32;1m加密认证成功\033[0m")
            else:
                print("加密认证失败")
