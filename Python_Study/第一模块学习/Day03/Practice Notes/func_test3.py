# -*- coding:utf-8 -*-
# Author:D.Gray

import sys
'''
函数返回值的作用：就是后面的程序要根据当前函数的返回值来执行相应的操作
'''
def text1():
    print('in the test1')       #return前的print会运行，返回值return为0后面的代码块就不会运行了
    return 0
    print('test end')

def text2():
    print('in the test3')

def text3():
    print('in the test3')
    return 1,'hello',['alex','wupeiqi'],{'name':'alex'}

x = text1()                     #将return=0的结果赋值给x变量
y = text2()
z = text3()
print('text1的返回值:',x)
print('text2的返回值:',y)
print('text3的返回值:',z)
