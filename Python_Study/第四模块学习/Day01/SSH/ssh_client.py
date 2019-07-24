# -*- coding:utf-8 -*-
# Author:D.Gray
import socket
client = socket.socket()
client.connect(("localhost",6969))

while True:
    option = input(">>>:")
    if len(option) == 0:continue
    client.send(option.encode())
    server_back_size = client.recv(1024).decode()
    print("收到服务器传来的指令大小:",int(server_back_size))
    client.send("ok".encode())
    reversed_data = b''
    reversed_size = 0
    while reversed_size < int(server_back_size):
        data = client.recv(1024)
        reversed_size += len(data)
        reversed_data += data
        print('实际收到大小:',reversed_size)
    else:
        print(reversed_data.decode())
