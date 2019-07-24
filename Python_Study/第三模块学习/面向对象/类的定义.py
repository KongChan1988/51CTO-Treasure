#-*- Coding:utf-8 -*-
# Author: D.Gray


class Dog(object):      # class定义一个类  Dog类名  (object)必填
    def __init__(self,name):    #构造函数，构造方法=初始化方法   self就是实例本身
        self.Name = name
        self.__age =  30       #定义一个私有属性

    def sayhi(self):  #  类的方法  self就是实例本身
        print('hello, I am a dog My name is %s'%self.Name)
    def eat(self,food):
        print('%s is eatting %s' %(self.Name,food))

d = Dog('LiChang')       #实例化Dog类   实例化后产生的对象叫做实例
d2 = Dog('Chuang2')       # Dog('Chuang2')中Chuang2就好比实参，传参给了def __init__(self,name)中的形参name
d.sayhi()       #执行Dog类下的sayhi函数
d2.sayhi()
d.eat('大便')   #d调用父类Dog中eat函数，'大便作为实参'传参给了eat(self,food)函数中的food形参
d2.eat('尿')

