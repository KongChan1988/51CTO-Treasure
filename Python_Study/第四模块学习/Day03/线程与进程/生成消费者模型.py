# -*- coding:utf-8 -*-
# Author:D.Gray
import threading,time
import queue
q = queue.Queue()
def producers(name):
    count = 1
    while True:
        q.put('骨头%s'%count)
        print('\033[32;1m[%s]生成的骨头%s\033[0m'%(name,count))
        count += 1
        time.sleep(1)

def consumers(name):
    while True:
        print('\033[33;1m[%s]获得了%s并吃掉了...\033[0m'%(name,q.get()))
        time.sleep(1)

p = threading.Thread(target=producers,args=('alex',))
c = threading.Thread(target=consumers,args=('赵宇',))
p.start()
c.start()