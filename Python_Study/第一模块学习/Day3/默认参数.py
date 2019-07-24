# -*- coding:utf-8 -*-
# Author:D.Gray
'''
默认参数特点：调用函数的时候，默认参数可有可无非必传，不传就默认值，传了就赋新值
用途：
1、默认安装值
2、默认连接数据库端口号
'''
print('\n----text1---')
def text1(x,y=2):   #定义形参的时候 默认给y=2
    print(x)
    print(y)

text1(1)             #赋值实参的时候就只给x赋值个实参就行
text1(1,3)           #当然也可以给y重新赋新值  3

print('\n----text2---')
def text2(x,y,z=3):     #  定义形参z时默认参数3，所以定义实参x,y就可以了
    print(x)
    print(y)
text2(1,2)

print('\n----text3---')
def text3(*args):       #在实参不固定或不确定的时候，可以先定义一个形参组  以*开头
    print(args)
text3(1,2,3,4,5,6)      #可以接受多个实参，以元组形式
text3(*[1,2,3,4,5])     #   args = tuple([1,2,3,4,5])

print('\n----text4---')
def text4(x,*args):
    print(x)
    print(args)
text4(1,2,3,4,5,6,7)    #其中实参1传给了形参x，其余都以元祖形式传给了*args

print('\n----text5---')
def text5(**kwargs):            #定义一个字典类型的形参，  **kwargs把n个关键字参数转换成字典形式
    print(kwargs)
    print('字典中name所对应的值:%s'%kwargs['name'])
    print('字典中age所对应的值:%s'%kwargs['age'])
text5(name = 'alex',age = 8,sex = '女')      # name当做字典中的键，'alex'就等于键所对应的值
text5(**{'name':'alex','age':8})

print('\n----text6---')
def text6(name,**kwargs):
    print(name)
    print(kwargs)
text6('alex')                           #如果没有定义实参，kwargs就默认为空字典
text6('alex',age = 18,sex = '男')        #定义实参给kwargs时一定要是关键字参数

print('\n----text7---')
def text7(name,age=18,**kwargs):        #参数组一定要往后放
    print(name)                         # 'alex'传递给形参 name
    print(age)                          #  age为默认参数 18
    print(kwargs)
text7('alex',sex = '男',hobby = 'tesla')   # 除'alex'其余都传递给形参 kwargs
text7('alex',sex = '男',hobby = 'tesla',age = 28)  # 若此时在定义个关键字实参age,将会重新赋值28给age

print('\n----text8---')
def text8(name,age=18, *args,**kwargs):
    print(name)
    print(age)
    print(args)                         #   *args 只接受n个位置参数,并转换成元组的形式。
                                        #   该案例中没有多余的位置参数能传递给 args，所以args返回一个空元组
    print(kwargs)                       #   **kwargs  只接受n个关键字参数，并转化成字典形式
text8('alex',age = 34,sex = '男',hobby = 'tesla')




