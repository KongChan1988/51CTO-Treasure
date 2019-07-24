# -*- coding:utf-8 -*-
# Author:D.Gray
import socket
client = socket.socket()
client.connect(('localhost',6969))
while True:
    meg = input('>>>:').strip()
    if len(meg) == 0:continue
    client.send(meg.encode())
    print("发送给服务端消息：",meg)
    res = client.recv(1024)
    print('接收服务端回调消息：',res.decode())

client.close()

