#-*- Coding:utf-8 -*-
# Author: D.Gray
import time
print('-----不修改源代码情况下统计时间-----')
def timer(func):    #timer(text1) func=text1
    def deco():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('the func run time is %s'%(stop_time-start_time))
    return deco


print('\n-----源代码-----')
@timer          # @timer(装饰器名字) = [text1 = timer(text1)]
def text1():
    time.sleep(3)
    print('in the text1')
@timer
def text2():
    time.sleep(3)
    print('in the text2')

print('\n-----装饰器-----')
print('deco的内存地址：',timer(text1))
text1 = timer(text1)   # @timer(装饰器名字) = [text1 = timer(text1)]
text1()
text2()
