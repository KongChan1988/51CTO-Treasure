# -*- coding:utf-8 -*-
# Author:D.Gray
import threading,time
class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n = n

    def run(self):
        print('talk_',self.n)
        time.sleep(2)

r1 = MyThread(1)
r2 = MyThread(2)
r1.start()
r2.start()

