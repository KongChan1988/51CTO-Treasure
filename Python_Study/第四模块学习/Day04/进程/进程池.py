# -*- coding:utf-8 -*-
# Author:D.Gray
from multiprocessing import Process,Pool
pool = Pool(5)
def f(num):
    print('Hello World',num)

list = []
for num in range(20):
    p = Process(target=f,args=(num,)).start()
    list.append(p)

for info in list:
    info.join()
