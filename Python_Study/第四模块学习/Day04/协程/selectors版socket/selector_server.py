# -*- coding:utf-8 -*-
# Author:D.Gray
import selectors
import socket
sel = selectors.DefaultSelector()
print('正在等待链接...')

def put(conn,):
    file_totle_size = conn.recv(1024)
    print('收到文件大小：',file_totle_size)

def read(conn,mask):
        data = conn.recv(1024)
        if data:
            print('收到服务端消息：',data)
            conn.send(data)
            print('发送给客户端回调消息：',data)
            put(conn)
            # conn.setblocking(False)
            # sel.register(conn, selectors.EVENT_READ, put)
        else:
            print('服务器已断开')

def accept(server,mask):
    conn,addr = server.accept()
    print('已和客户端[%s]建立连接'%str(addr))
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)

server = socket.socket()
server.bind(('localhost',6969))
server.listen(100)
server.setblocking(False)
sel.register(server,selectors.EVENT_READ,accept)

while True:
    events = sel.select()
    for k,mask in events:
        callback = k.data
        callback(k.fileobj,mask)
