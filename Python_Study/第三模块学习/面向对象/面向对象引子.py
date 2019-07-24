#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
面向对象(OOP)----object oriented programing(面向对象编程)
面向对象编程:
OOP编程是利用“类”和“对象”来创建各种模型来实现对真实世界的描述，
使用面向对象编程的原因一方面是因为它可以使程序的维护和扩展变得更简单，
并且可以大大提高程序开发效率 ，另外，基于面向对象的程序可以使它人更加容易理解你的代码逻辑，
从而使团队开发变得更从容。

面向对象几个核心特性：
Class 类（模板）:一个类就是对一类用于相同属性对象的抽象、蓝图、原型。
Object  对象：一个对象就是一个类的实例化后实例
Encapsulation 封装：
1、防止数据被随意修改
2、使外部程序不需要关注对象内部的构造，只需要通过对象对外提供的接口进行直接访问即可
Inheritance 继承：一个类可以派生出子类、在这个父类里定义的属性、方法自动被子类继承
    通过父类---->子类的方式以最小代码量实现、不同角色的共同点和不同点同时存在
Polymorphism 多态：多态是面向对象的重要特性，简单来说“一个接口，多种实现”，指一个父模板中派生
出来子模板，且每个子模板继承了父类同样的方法名后，同时又对父类的方法做了不同的实现。这就是同一种事物表现出的多种状态
例：父类：人
    对象：华人、欧洲人
    父类方法：说话
    多态：华人、欧洲人都继承了父类（人）说话的功能，但同时对说话这个功能做了不同的实现
对不同类的对象发出相同的消息将会有不同的行为：
例：老板只需要发出指令消息让所有员工开始工作，老板不需要对具体某个职位发出具体工作消息
这里的“员工”是抽象的事物
'''

class Role(object):
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name  #名字
        self.role = role    #角色
        self.weapon = weapon #武器
        self.life_value = life_value #血量
        self.money = money  #金钱

    def shot(self):
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        self.weapon = gun_name
        print("%s just bought %s" %(self.name,gun_name))


r1 = Role('Alex', 'police', 'AK47')     #生成一个角色(实例化Role类) r1--实例（Role实例化后的实例对象）
                                        # ('Alex', 'police', 'AK47')---r1的成员属性
r2 = Role('Jack', 'terrorist', 'B22')   #生成一个角色

r2.buy_gun('沙漠之鹰')