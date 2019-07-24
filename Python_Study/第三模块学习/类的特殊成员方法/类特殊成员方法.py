#-*- Coding:utf-8 -*-
# Author: D.Gray

class Dog(object):
    ''' 描述类信息，这是用于看片的神奇'''

    def func(self):
        pass
print(Dog.__doc__)   #输出类的描述信息
print(Dog.__module__) #表示当前操作对象的类是什么


