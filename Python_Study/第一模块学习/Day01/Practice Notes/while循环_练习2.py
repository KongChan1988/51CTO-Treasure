#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
五香熏牛肉(pastrami)卖完了:创建sandwich_orders列表，并确保'pastrami'在其中至少出现了三次。在程序开头
附近添加这样的代码：打印一条消息，指出熟食店的五香熏牛肉卖完了；再使用一个while循环将sandwich_orders中
的'pastrami'都删除。确认最终的列表finished_sandwiches中不包含'pastrami'
'''
sandwich_orders = ['pastrami','bacon','chicken','meat',
                   'chicken','bacon','pastrami',
                   'meat','pastrami','bacon','bacon','pastrami']
finished_sandwiches = []

print("Sorry We're out of bacon and beef ")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches.append(sandwich_orders)
print(finished_sandwiches)