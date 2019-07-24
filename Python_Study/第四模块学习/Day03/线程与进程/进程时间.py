# -*- coding:utf-8 -*-
# Author:D.Gray
import threading,time
def run(n):
    print('talk_',n)
    time.sleep(2)
    print('当前使用线程：',threading.current_thread())
start_time = time.time()
t_list = []
for i in range(50):
    t = threading.Thread(target=run,args=(i,))
    t.start()
    t_list.append(t)
for t in t_list:
    t.join()
print('线程耗时：%s秒'%(time.time()-start_time))

