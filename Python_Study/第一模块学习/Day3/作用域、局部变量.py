#-*- Coding:utf-8 -*-
# Author: D.Gray

school = 'Oldboy edu'               #全局变量，在整个程序顶层定义的变量
def change_name(name):
    global school                  # 在函数里面改全局变量   千万不要在函数里面改全局变量
    school = 'Mage Linux'
    print('before change:',name,school)
    name = 'Alex li'                #局部变量只在函数里生效，这个函数就是这个变量的作用域
    print('after change:',name)
    print('局部变量：',school)

print('调用函数前global全局变量：',school)
print('全局变量：',school)
name = 'alex'
change_name(name)
print('调用函数后global全局变量：',school)        # 必须调用函数后才会生效，放在调用函数前依然是全局变量参数
print(name)