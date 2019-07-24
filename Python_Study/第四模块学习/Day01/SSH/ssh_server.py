# -*- coding:utf-8 -*-
# Author:D.Gray
import socket,os
server = socket.socket()
server.bind(("localhost",6969))
server.listen(5)
print("等待接电话...")
while True:
    conn,addr = server.accept()
    print("一个新的链接:",addr)
    while True:
        res = conn.recv(1024).decode()
        print(res)
        res_info = os.popen(res).read()
        print(res_info)
        if len(res_info) ==0:res_info = 'cmd has no output'
        conn.send(str(len(res_info.encode())).encode())
        conn.recv(1024)
        conn.send(res_info.encode())