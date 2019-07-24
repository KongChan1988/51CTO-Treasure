# -*- coding:utf-8 -*-
# Author:D.Gray

import socket
client = socket.socket()
client.connect(("localhost",6969))

client.send("下载TV影视".encode("utf-8"))
data = client.recv(1024)
print("recv: ",data.decode())
client.close()