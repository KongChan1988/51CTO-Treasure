#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
属性方法：把一个方法变成一个静态属性
'''
class Dog(object):

    def __init__(self,name):
        self.name = name

    @property  #attribute
    def eat(self):  #使用属性方法后 不能直接给eat方法传参
                        #只能 通过 方法名.setter  方法来赋值
        print("%s 吃 %s" % (self.name, 'dd'))

    @eat.setter
    def eat(self,food):
        print("set to food %s"%food)

    @eat.deleter
    def eat(self):
        print("全删了")

d = Dog("ChenRongHua")
d.eat = "包子"
del d.eat
