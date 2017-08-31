#-*- Coding:utf-8 -*-
# Author: D.Gray
import  time
def timmer(func):
    print('timmer:',func)
    def deco(*args,**kwargs):          #若deco不定义参数时，此程序运行会把报错
        print('deco:',*args,**kwargs)
        start_time = time.time()
        func(*args,**kwargs)                          #执行*args和**kwargs
        print('func:',func)
        stop_time = time.time()
        print('the func run timer is %s:'%(stop_time-start_time))
    return deco
@timmer         # test1 = timmer(text1) = deco   text1() = deco()
def text1(name,age):
    print('in the text1:',name,age)
@timmer
def text2():
    time.sleep(3)
    print('in the text2')

text1('alex',22)
text2()