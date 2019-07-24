# -*- coding:utf-8 -*-
# Author:D.Gray
import paramiko
p_key = paramiko.RSAKey.from_private_key_file('id_rsa@root@wangwei')
transport = paramiko.Transport(('192.168.72.128',22))
transport.connect(username='root',pkey=p_key)
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put('server.txt','/root/python_work/ssh_sftp/oldgirls.txt')
#sftp.get('/root/python_work/ssh_sftp/oldgirls.txt','server.txt')
transport.close()