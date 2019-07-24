# -*- coding:utf-8 -*-
# Author:D.Gray

def acount(func):
    def bar(*args,**kwargs):
        print('before:',*args,**kwargs)
        func(*args,**kwargs)
        print('after:%s'%func(*args,**kwargs))
    return bar

@acount
def f1(arg):
    return arg + 1
@acount
def f2(arg1, arg2):
    return arg1 + arg2

f1(2)
f2(1,3)

