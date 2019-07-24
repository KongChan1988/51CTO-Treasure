# -*- coding:utf-8 -*-
# Author:D.Gray
'''

'''
import queue
print('先进先出'.center(50,'-'))
q = queue.Queue()
q.put('d1')
q.put('d2')
print(q.get())
print('打印队列个数：',q.qsize())

print('后进先出'.center(50,'-'))
q = queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)
print('\n最先打印最后进的3：',q.get())
print(q.get())
print(q.get())
try:
    print(q.get_nowait())
except queue.Empty as e:
    print('p.get()超出所设队列个数会报异常')

print('限制队列个数'.center(50,'-'))
q = queue.Queue(maxsize=3)  #设置最大队列个数为3
q.put(1)
q.put(2)
q.put(3)
try:
    q.put_nowait(4)
except queue.Full as e:
    print('队列超过最大队列个数maxsize=3会异常')
print(q.get())
print(q.get())
print(q.get())

print('队列优先级'.center(50,'-'))
q = queue.PriorityQueue()
q.put((1,'zero'))
q.put((2,'boy'))
q.put((3,'alex'))
print('按数字大小顺序：',q.get())
print(q.get())
print(q.get())

q.put(('zero',1))
q.put(('boy',2))
q.put(('alex',3))
print('按首字母顺序：',q.get())
print(q.get())
print(q.get())