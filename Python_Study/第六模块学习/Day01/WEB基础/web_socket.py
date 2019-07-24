#-*-coding:utf-8 -*-
# Author: D.Gray
import socket

def handle(client):
    buf = client.recv(1024)
    client.send(b"HTTP/1.1 200 ok\r\n\r\n")
    f = open('index','rb')
    data = f.read()
    f.close()
    client.send(data)

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',8000))
    sock.listen(5)

    while True:
        connaction,address = sock.accept()
        handle(connaction)
        connaction.close()

if __name__ == '__main__':
    main()