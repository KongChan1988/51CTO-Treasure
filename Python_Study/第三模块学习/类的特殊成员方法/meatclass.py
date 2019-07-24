#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
类的创建
'''
class MyType(type):
    def __init__(self,*args,**kwargs):

        print("Mytype __init__",*args,**kwargs)

    def __call__(self, *args, **kwargs):
        print("Mytype __call__", *args, **kwargs)
        obj = self.__new__(self)
        print("obj ",obj,*args, **kwargs)
        print(self)
        self.__init__(obj,*args, **kwargs)
        return obj

    def __new__(cls, *args, **kwargs):
        print("Mytype __new__",*args,**kwargs)
        return type.__new__(cls, *args, **kwargs)

print('here...')
class Foo(object ,metaclass=MyType):

    def __init__(self,name):
        self.name = name

        print("Foo __init__")

#new是用来创建实例的，若一个类中有new方法，那这个类要先除法new方法
#然后在通过new来调用一个构造函数
    def __new__(cls, *args, **kwargs):  #cls = Foo这个类
        print("Foo __new__",cls, *args, **kwargs)
        print('Foo.__new__:',object.__new__(cls))
        return object.__new__(cls)  #去继承父类的__new__方法

f = Foo("Alex")
print("f",f)
print("fname",f.name)



