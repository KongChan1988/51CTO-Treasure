#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
hasattr(obj,new_str)  #判断一个对象里是否有对应的字符串的方法映射
getattr(obj,new_str)   #根据字符串去获取obj对象里的对应方法的内存地址
setattr(obj,y,z)    #通过y设置一个新的属性z或方法
delattr(obj,new_Str)    #删除一个映射方法
'''


def bulk(self):
    print(" %s talk is 'WafWaf...'" %self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eatting..."%self.name,food)


d = Dog("NiuHanYang")
choice = input(">>>:").strip()

#print(hasattr(d,choice))  #判断一个对象里是否有对应的字符串的方法映射
#print(getattr(d,choice))    #根据字符串去获取obj对象里的对应方法的内存地址

if hasattr(d,choice):   #根据用户输入并判断这个类中是否存在指定相应的方法
    func = getattr(d,choice)    #根据用户输入去调用相应方法的内存地址
    #func("大便")  #“大便”赋值给 eat(self,food)中的food

    setattr(d,choice,"alex")    #将类中已有属性name重新赋值
    print('未删除前:%s'%d.name)
    delattr(d,choice)       #删除一个反射方法
    print('删除后：报空指针' % d.name)
else:
    setattr(d,choice,bulk) #使用setattr方法在类中新创建一个类外部的一个函数做为类内部方法
                            #此时将 类外部函数bulk做为类内部的一个新方法创建
    attr = getattr(d,choice)    #新创建的内部方法是一个静态方法
    attr(d)                     #attr(d) = d.choice(d)  d.talk = bulk

    setattr(d,choice,22)
    attr1 = getattr(d,choice)
    print('attr1:',attr1)



