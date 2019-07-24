#-*- Coding:utf-8 -*-
# Author: D.Gray
''''
公有属性：
1、类里所有对象都能访问的属性
2、在类里直接定义的属性
3、类内部的函数方法都是公有属性
r1 = Role('Alex', 'police', 'AK47')  这些只是r1这个对象的成员属性并不是Role类的公有属性
'''
class Role(object):
    nationality = 'JP'          #定义一个公有属性，r1和r2实例都能共享（相同)的一个属性
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name  #名字
        self.role = role    #角色
        self.weapon = weapon #武器
        self.life_value = life_value #血量
        self.money = money  #金钱
        self.__heart_puplic = 'Nomal'      #定义一个私有属性 外部不能调用

    def shot(self):
        print("shooting...")

    def got_shot(self):
        '''
        定义一个中枪函数
        :return:
        '''
        self.__heart = 'DIE'
        print("\n在方法内部设有一个私有属性>>>\n%s\nah...,I got shot...\nMy heart is %s\n" %(self.name,self.__heart))

    def buy_gun(self, gun_name):
        self.weapon = gun_name
        print("%s just bought %s" %(self.name,gun_name))

r1 = Role('Alex', 'police', 'AK47') #生成一个角色(实例化Role类)
r2 = Role('Jack', 'terrorist', 'B22')  #生成一个角色（实例化Role类）

print('r1的国籍(公有属性)>>>',r1.nationality)
print('r2的国籍(公有属性)>>>',r2.nationality)
Role.nationality = 'USA'            #将Role的公有属性nationality 更改为USA
print('将Role的公有属性nationality 更改为USA r1的国籍>>>',r1.nationality)
print('将Role的公有属性nationality 更改为USA r2的国籍>>>',r2.nationality)

r1.nationality = 'CN'   #将r1这个实例成员对象nationality 更改为CN
print('将r1这个实例成员对象nationality 更改为CN r1的国籍>>>',r1.nationality)
print('将r1这个实例成员对象nationality 更改为CN r2的国籍>>>',r2.nationality)

print('r1的国籍(公有属性)>>>',r1.nationality)
print('r2的国籍(公有属性)>>>',r2.nationality)