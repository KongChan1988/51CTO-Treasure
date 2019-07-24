#-*- Coding:utf-8 -*-
# Author: D.Gray

def bulk(self):
    print("%s bulk is :Wafwaf"%self.name)
class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eat %s"%(self.name,food))

d = Dog("Chenronghua")
choise = input(">>>:")
if hasattr(d,choise):
    func = getattr(d,choise)
    func("大便")
    setattr(d,choise,"alex")
    attr = getattr(d,choise)
    print(attr)
else:
    setattr(d,choise,bulk)
    attr = getattr(d,choise)
    attr(d)
