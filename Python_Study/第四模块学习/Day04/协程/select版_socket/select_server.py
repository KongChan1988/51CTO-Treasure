# -*- coding:utf-8 -*-
# Author:D.Gray
import select
import socket
import queue
server = socket.socket()
server.bind(('localhost',6969))
server.listen(100)
print('等待链接...')

dic = {}
inputs = [server,]  #想要监测的链接列表 不能为空列表否则会报错 解决办法：先把自己server（socket实例）交给内核监测
outputs = []    #往outputs放啥链接就出啥链接内核不监测（这里就是要返回给客户端的数据放到outputs）

while True:
    # readable:活动的可读数据的链接列表  writeable:       exceptional:发生异常的链接(比如说断开的链接)
    readable,writeable,exceptional = select.select(inputs,outputs,inputs)  #通过内核监测进来的链接
    print('\033[31;1m有链接进来了...\033[0m')
    print('readable：%s\nwriteable:%s\nexptional:%s\n'%(readable,writeable,exceptional)) #fd:文件描述符
    for r in readable:
        if r is server:   #server活动了代表来了一个新链接，就要建立一个新链接
            conn,addr = r.accept()
            print('与客户端链接建立了'.center(50,'-'))
            print('server:%s\n客户端链接的实例conn:%s\n客户端地址addr：%s'%(r,conn,addr))
            server.setblocking(0)  # 不阻塞模式
            inputs.append(conn)  # 因为首次新建立的链接还没发数据过来（没有阻塞）所以程序会报错，所以要先让select监测这个conn
            dic[conn] = queue.Queue() #初始化一个队列，后面存要返回给客户端的数据
        else:
            #print('\033[32;1m客户端链接的实例conn:%s\033[0m' % conn)
            data = r.recv(1024)  #这里只能r.recv() 如用conn.recv()会出错收发数据时会出现链接错乱
            if data:
                #print('\033[32;1m客户端链接的实例r:%s\033[0m'%r)
                print('收到客户端数据:%s\n'%data.decode())
                dic[r].put(data)
                if r not in outputs:
                    outputs.append(r)
                # r.send(data)
                # print('发送数据给客户端：',data.decode())
            else:
                print('客户端已断开:',r)
                if r in outputs:
                    outputs.remove(r)
                inputs.remove(r)
                del dic[r]


    for w in writeable:
        send_to_clint = dic[w].get()
        w.send(send_to_clint)
        print('发送数据给客户端：', send_to_clint.decode())
        outputs.remove(w)

    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        e.close()
        del dic[e]

