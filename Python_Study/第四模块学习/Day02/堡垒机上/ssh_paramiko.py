# -*- coding:utf-8 -*-
# Author:D.Gray
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #链接并自动加入未在know_hosts文件里的机器
#设置链接机器的IP地址，端口号，用户名，密码...
ssh.connect(hostname='192.168.72.128',port=22,username='root',password='admin1988')
stdin,stdou,stdeer = ssh.exec_command('who') #输入linux执行命令
res ,err = stdou.read(),stdeer.read()  #stdeer返回错误结果
result = res if res else err  #读取命令返回结果（Byre格式）  标准输出：正确结果
print(result.decode())
ssh.close()