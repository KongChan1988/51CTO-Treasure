# -*- coding:utf-8 -*-
# Author:D.Gray

# -*- coding:utf-8 -*-
# Author:D.Gray
'''
面向对象编程 (OOP) 语言的一个主要功能就是“继承”。
继承是指这样一种能力：它可以使用现有类的所有功能，并在无需重新编写原来的类的情况下对这些功能进行扩展。
通过继承创建的新类称为“子类”或“派生类”。
被继承的类称为“基类”、“父类”或“超类”。
继承的过程，就是从一般到特殊的过程。
要实现继承，可以通过“继承”（Inheritance）和“组合”（Composition）来实现。
在某些 OOP 语言中，一个子类可以继承多个基类。
但是一般情况下，一个子类只能有一个基类，要实现多重继承，可以通过多级继承来实现。
继承概念的实现方式主要有2类：实现继承、接口继承。
Ø         实现继承是指使用基类的属性和方法而无需额外编码的能力；
Ø         接口继承是指仅使用属性和方法的名称、但是子类必须提供实现的能力(子类重构爹类方法)；
在考虑使用继承时，有一点需要注意，那就是两个类之间的关系应该是“属于”关系。
例如，Employee 是一个人，Manager 也是一个人，因此这两个类都可以继承 Person 类。
但是 Leg 类却不能继承 Person 类，因为腿并不是一个人。
抽象类仅定义将由子类创建的一般属性和方法。
OO开发范式大致为：划分对象→抽象类→将类组织成为层次化结构(继承和合成) →用类与实例进行设计和实现几个阶段。
'''

class Person(object):   #父类
    def __init__(self,name,age):
        self.name = name        # self = b    self.name = b.name
        self.age = age
        self.sex = 'Noraml'
    def talk(self):
        print('person is talking...!')

class BlackPerson(Person):   #继承父类
    def __init__(self,name,age,powwer): #先继承在重构
        Person.__init__(self,name,age)  #继承了父类的构造方法  这里的self是BlackPerson实例化的self
                                        #name,age是父类传过来的
        self.powwer = powwer
        print(self.name,self.age,self.sex)

    def talk(self):
        print('继承父类的子类可以重写父类方法：black person is talking...')
    def walk(self):
        print('继承父类的子类可以自定义方法：black person is walking....')   #继承父类的子类可以自定义方法

class WhitePerson(Person):
    pass

b = BlackPerson('Wei er smith',30,'strong')
b.talk()
b.walk()