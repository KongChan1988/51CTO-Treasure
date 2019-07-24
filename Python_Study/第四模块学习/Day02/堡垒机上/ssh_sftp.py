# -*- coding:utf-8 -*-
# Author:D.Gray
import paramiko
transport = paramiko.Transport(('192.168.72.128',22))
transport.connect(username='root',password='admin1988')

sftp = paramiko.SFTPClient.from_transport(transport)
try:
    #将rd.txt  上传至服务器 /home/wangwei/python_work/ssh_sftp
    sftp.put('rd.txt','/root/python_work/堡垒机上/ssh_sftp/client.txt')
except OSError as e:
    print(e)

# #将服务端/home/wangwei/python_work/ssh_sftp/oldgirls.txt 下载到本地 文件名为:fromlinux.txt
# sftp.get('/root/python_work/堡垒机上/ssh_sftp/oldgirls.txt','fromlinux.txt')
transport.close()