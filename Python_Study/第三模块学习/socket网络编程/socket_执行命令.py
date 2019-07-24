#-*- Coding:utf-8 -*-
# Author: D.Gray
import os
import socket
server = socket.socket()
server.bind(("localhost",6969))
server.listen(5)
print("等电话进来")
while True:
    conn,addr = server.accept()
    print(conn,addr)
    print("电话进来了")
    while True:
        data = conn.recv(1024)
        print("recv:",data)
        if not data:
            print("client has lost...")
            break
        res = os.popen(data).read()
        conn.send(res)

server.close()