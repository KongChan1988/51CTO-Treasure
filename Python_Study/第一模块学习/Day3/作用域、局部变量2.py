# -*- coding:utf-8 -*-
# Author:D.Gray

num = 1
names = ['Alex','Jack','Rain']
def change_name():
    num = 2                     # 在函数里修改全局变量num的参数
    names[0] = '金角大王'       # 列表、字典、类都可以在函数里面改
    print(names)
    print('在函数里修改全局变量num后的值：',num)    # 在函数里面可以修改 局部变量 num的值

print('全局变量num值:',num)          # 在函数里不能修改全局变量中的字符串和整数
change_name()
print('局部变量只在函数里生效的num值：',num)
print('在函数里修改全局变量names列表参数后,全局变量names的值：',names)    #