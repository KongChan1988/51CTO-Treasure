# -*- coding:utf-8 -*-
# Author:D.Gray

'''
高阶函数：变量可以指向函数，函数的参数能接受变量，那么一个函数就可以接受另一个函数作为参数，
            这种函数就称之为高阶函数
'''
def add(a,b,f):
    return f(a)+f(b)

res = add(3,-6,abs)     # abs方法： 就是取绝对值
print(res)

print('abs语法：',abs(-6))