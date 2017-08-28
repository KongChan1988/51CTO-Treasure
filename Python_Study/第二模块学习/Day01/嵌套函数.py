#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
函数嵌套：在一个函数体内用def 新定义一个函数
'''
def foo():
    print('in the foo')
    def bar():
        print('in the bar')
    bar()
foo()

x = 0
def grandpa():
    x =1
    def dad():
        x =2
        def son():
            x = 3
            print(x)
        son()
    dad()
grandpa()