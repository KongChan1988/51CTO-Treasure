# -*- coding:utf-8 -*-
# Author:D.Gray
'''
公钥私钥
A连B  A把公钥给B  A留私钥
A:
ssh-keygen 生成秘钥
ssh-copy-id root@192.168.72.128 复制公钥给B
more .ssh/id_rsa@root@wangwei    查看私钥
more .ssh/id_rsa@root@wangwei.pub 查看公钥
B:
ssh -p22 root@192.168.72.128 B端登录验证
vi .ssh/authorized_keys 公钥保存文件

linux下载秘钥文件到win
sz ~/.ssh/id_rsa@root
'''
import  paramiko
p_key = paramiko.RSAKey.from_private_key_file('id_rsa@root@wangwei') #wangwei@192.168.72.128 连 root@192.168.72.128的公钥
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#通过wangwei@192.168.72.128 连 root@192.168.72.128
ssh.connect(hostname='192.168.72.128',port=22,username='root',pkey=p_key)
stdin,stdou,stdeer = ssh.exec_command('who')
result = stdou.read()
print(result.decode())
ssh.close()