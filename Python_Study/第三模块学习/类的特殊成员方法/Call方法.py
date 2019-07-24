#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
未使用Call方法，实例化对象后，这个实例对象后面就不能在加括号
'''
class Dog(object):
    def __init__(self,name):
        self.name = name

    # def eat(self,food):
    #     print("%s 吃 %s"%(self.name,food))

    def __call__(self, *args, **kwargs):
        print("running call",args,kwargs)

    def __str__(self):  #在类中定义了__str__方法
        return "<obj:%s>"%self.name

print(Dog.__dict__)        #打印类里的所有属性，不暴扣实例属性
d = Dog("ChenRongHua")
d(1,2,3,name = "alex")
print(d.__dict__)       #打印所有实例属性，不包括类属性
print(d)    #在类中定义了__str__方法,那么在打印对象时，默认输出该方法的返回值
