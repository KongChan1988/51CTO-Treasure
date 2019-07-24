# -*- coding:utf-8 -*-
# Author:D.Gray
'''
目标：单线程实现并发Http请求
socket
IO多路复用
Http协议
流程：
    http://www.cnblogs.com/wupeiqi.articles/6229292.htnl
    1.socket连接,IP和端口进行连接  www.cnbolgs.com
    2.请求信息
        请求头
            k = v \r\n
            k = v \r\n
            k = v \r\n
            \r\n\r\n
            请求体
        socket.sendall()
'''
import socket
client = socket.socket()
# client.setblocking(False)   #将其变为非阻塞模式
#连接 阻塞
client.connect(("www.baidu.com",80))
#发送
client.sendall(b"GET / HTTP/1.0\r\nHost:www.baidu.com\r\n\r\n")
#接收 阻塞
data = client.recv(1024)
head,body = data.split(b"\r\n\r\n")   #分割响应头和响应体
for item in head.split(b"\r\n"):
    print("请求头：",item)
print("请求体：",body)
client.close()