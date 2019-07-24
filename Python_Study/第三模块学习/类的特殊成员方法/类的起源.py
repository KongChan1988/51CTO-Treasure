#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
普通方式
class Foo(object):
    def __init__(self,name):
        self.name = name

f = Foo('alex')
print(type(f))
print(type(Foo))
'''
'''
装逼方式
'''
def func(self):
    print('hello %s'%self.name)

def __init__(self,name,age):
    self.name = name

Foo = type('Foo',(),{'talk':func,
                     '__init__':__init__})
f = Foo("ChenRongHua",22)
f.talk()
print(type(Foo))