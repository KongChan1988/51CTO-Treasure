# -*- coding:utf-8 -*-
# Author:D.Gray
'''
线程写法一
'''
import threading,time
def run(n):
    print('talk run',n)
    time.sleep(2)
r1 = threading.Thread(target=run,args=(2,))
r2 = threading.Thread(target=run,args=(3,))
r1.start()
r2.start()