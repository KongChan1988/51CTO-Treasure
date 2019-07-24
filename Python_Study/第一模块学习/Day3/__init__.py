# -*- coding:utf-8 -*-
# Author:D.Gray
import time

schoola = 'Oldboy edu'           #全局变量
name = 'kyo'
schoolb = '51CTO edu'
def change_name(name):
    global schoola
    school = 'Mage Linux'
    print('before name:',name)
    name = 'Alex li'                #局部变量只在函数里生效，这个函数就是这个变量的作用域
    print('after name:',name)

print('调用函数前global全局变量school:',schoola)
change_name(name)
print('全局变量:',name)
print('调用函数后global全局变量school:',schoola)     # 必须调用函数后才会生效，放在调用函数前依然是全局变量参数


def change_name2(name):
    print('before name:',name)
    name = 'Alex li'
    print('after name:',name)
print('没global全局变量school:',schoolb)