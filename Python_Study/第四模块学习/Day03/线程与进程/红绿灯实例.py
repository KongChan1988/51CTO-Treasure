# -*- coding:utf-8 -*-
# Author:D.Gray
import threading,time
event = threading.Event()

def light():
    count = 0
    event.set()
    while True:
        if count >= 5 and count < 10:
            event.clear()
            print('\033[31;1m红灯停\033[0m')
        elif count > 10:
            event.set()
            #event.wait()
            count = 0
        else:
            print('\033[32;1m绿灯亮\033[0m')
        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():
            print('【%s】绿灯了开始跑了'%name)
            time.sleep(1)
        else:
            print('[%s]红灯了停车'%name)
            event.wait()

light = threading.Thread(target=light)
light.start()
car = threading.Thread(target=car,args=('Tesla',))
car.start()
