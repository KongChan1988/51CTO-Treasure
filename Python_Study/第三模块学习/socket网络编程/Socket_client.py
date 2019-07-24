#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
网络七层：
应用层
表示层
会话层
传输层     http、smtp、dns、ftp、ssh、snmp....通过协议传输数据
网络层     认识IP地址  A和B连上了还不能传数据
数据链路层  只认识mac地址（物理地址16进制）： 40-8D-5C-06-F0-A5
物理层

TCP/IP：三次握手，四次断开。 SVN--->svn+ack
                                <---ack
UDP（用的少了）：A端不管B端是否存在或开机 直接传输数据给B端

每个机器最多可以开65535port(端口)
地址簇：网络层
'''
#客户端
import socket
client = socket.socket() #声明socket类型，同事生产socket链接对象
client.connect(('localhost',6969))

while True:
    msg = input(">>>:").strip()
    if len(msg) == 0:
        continue
    #client.send(b"Hello World!!")
    client.send(msg.encode("utf-8"))
    data = client.recv(1024)    #默认收 1024个字节=1k
    print("recv：",data.decode())

client.close()


