#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
静态方法：保存在类中，调用者类（无需创建对象），可以有任意个参数：
            只是名义上归类管理，实际上在静态方法里访问不了类或实例中的任何属性
            实际上使用静态方法后，这个类中方法只是一个函数
class F1:
    @staticmethod
    def a1():
        print('alex')
F1.a1()     # 静态方法：类.方法名----无需创建对象
'''
class Dog(object):

    def __init__(self,name):
        self.name = name

    @staticmethod    #静态方法跟类没什么关系，只是一个单纯的函数
    def eat(self):
        print("%s 吃 %s "%("赵宇","屎"))

d =  Dog("ChenRonghua")
d.eat(d)