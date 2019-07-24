#-*- Coding:utf-8 -*-
# Author: D.Gray

class Animal:
    def __init__(self,name):
        self.name = name

    def talk(self):
        raise NotImplementedError("调用此方法时主动报个错")

    @staticmethod  # 实现多态
    def animal_talk(obj):
        print(obj.talk())

class Dog(Animal):
    def talk(self):
        return "Woof!Woof!"

class Cat(Animal):
    def talk(self):
        return  "Meow"

d = Dog('大黄')
c = Cat('大黄')
Animal.animal_talk(c)   #多态的实现
Animal.animal_talk(d)
d.animal_talk()