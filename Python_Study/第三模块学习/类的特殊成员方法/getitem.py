#-*- Coding:utf-8 -*-
# Author: D.Gray
class Foo(object):
    def __init__(self):
        self.data = {}
    def __getitem__(self, key):
        print('__getitem__',key)

    def __setitem__(self, key, value):
        print('__setitem__',key,value)
        self.data [key] = value

    def __delitem__(self, key):
        print("__delitem__",key)

obj = Foo()
obj['name'] = 'alex'
print(obj.data)