# -*- coding:utf-8 -*-
# Author:D.Gray
import threading,time
def run(n):
    print('talk_',n)
    time.sleep(2)
    print('talk done:',threading.current_thread())

start_time = time.time()
t_list = []
for i in range(50):
    t = threading.Thread(target=run,args=(i,))
    t.setDaemon(True)
    t.start()
    t_list.append(t)
# for t in t_list:
#     t.join()

print('所有线程执行完毕:'.center(50,'-'))
print('所有线程所用时间：',time.time()-start_time)
print('当前运行线程个数：',threading.active_count())
