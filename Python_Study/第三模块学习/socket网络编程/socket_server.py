#-*- Coding:utf-8 -*-
# Author: D.Gray

#服务器端
import socket
server = socket.socket()
server.bind(('localhost',6969))   #绑定端口
server.listen(5)     #监听

print("我要开始等电话了")
conn,addr = server.accept()  #等电话打进来
#conn就是客户端连过来而在服务器端为其生产的一个链接实例
print(conn,addr)

print("电话来了")
data = conn.recv(1024)
print("recv",data)
conn.send(data.upper())
server.close()