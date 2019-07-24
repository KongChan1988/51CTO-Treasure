#-*- Coding:utf-8 -*-
# Author: D.Gray
import time
'''
高阶函数：
a：把一个函数名当做实参传给另外一个函数（在不修改被装饰函数源代码情况下
为其添加功能）
b：返回值中包含函数名(不修改函数的调用方式)
'''
def bar():              #源代码
    time.sleep(3)
    print('in the bar')
def text1(func):        #装饰器，来装饰bar函数
    start_time = time.time()
    func()          # 运行bar函数
    stop_time = time.time()
    print('the func run time is %s'%(stop_time-start_time))
text1(bar)      # 光一个bar就是一个内存地址  bar()是运行返回结果
#text1(bar)  =  func()


print('\n------高阶函数返回值-------')
def bar1():
    time.sleep(3)
    print('bar1:','in the bar')
def text2(func):
    print('func:%s'%func)
    #return func
print(text2(bar))
bar1 = text2(bar1)
bar1()      # 运行bar的返回结果
