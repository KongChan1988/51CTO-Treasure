#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
列表形式一：
a = [1,2,3]
列表生成式:
[i*2 for i in range(10)]  相当于    a = []
                                for i in range(10):
                                    a.append(i*2)
'''
print('------斐波那契数列-----')
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'
f = fib(10)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())



