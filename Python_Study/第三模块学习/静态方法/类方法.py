#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
类方法：
    -   只能访问类变量，不能访问实例变量
'''
class Dog(object):
    n = 'huazai'       #类方法只能访问类变量（公有属性）
    def __init__(self,name):
        self.name = name

    @classmethod
    def eat(self):
        print("%s 吃 %s"%(self.n,'dd'))

d = Dog("ChenRongHua")
d.eat()