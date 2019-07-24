#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
__init__：构造方法
私有属性：不能被外部调用只能在方法内部调用的属性  格式：__XXX
 1)允许外部看到私有属性，但不能修改
    定义一个方法，在返回一个私有属性
    def 方法名(self):
        return self.__私有属性名  例：r1.__heart_puplic
2)强制访问私有属性
     对象名._类名__私有属性   例：r1._Role__heart
'''
class Role(object):
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name  #名字
        self.role = role    #角色
        self.weapon = weapon #武器
        self.life_value = life_value #血量
        self.money = money  #金钱
        self.__heart_puplic = 'Nomal'      #定义一个私有属性 外部不能调用

    def shot(self):
        print("shooting...")

    '''
            定义一个中枪函数
            :return:
            '''
    def got_shot(self):
        self.__heart = 'DIE'
        print("\n在方法内部设有一个私有属性>>>\n%s\nah...,I got shot...\nMy heart is %s\n" %(self.name,self.__heart))

    def get_heart(self):
        return self.__heart_puplic     #从外部只能访问私有属性，但不能对其修改

    def buy_gun(self, gun_name):
        self.weapon = gun_name
        print("%s just bought %s" %(self.name,gun_name))


r1 = Role('Alex', 'police', 'AK47') #生成一个角色
r2 = Role('Jack', 'terrorist', 'B22')  #生成一个角色

print(r1.life_value)    #打印一个r1对象的生命值
r1.got_shot()           #在方法内部设有一个私有属性
print('从外部只能访问私有属性，但不能对其修改>>>',r1.get_heart())
print('强制访问私有属性方法:对象名._类名__私有属性>>>',r1._Role__heart)
print('强制访问私有属性方法:对象名._类名__私有属性>>>',r1._Role__heart_puplic)
r1._Role__heart_puplic = '强制更改私有属性'
print('强制访问私有属性方法:对象名._类名__私有属性>>>',r1._Role__heart_puplic)