# -*- coding:utf-8 -*-
# Author:D.Gray
'''
装饰器：高阶函数+嵌套函数
定义：本质是函数（装饰其他函数）就是为其他函数添加附加功能
原则：1、不能修改被装饰函数的源代码
        2、不能修改被装饰函数的调用凡是
实现装饰器知识储备：
1、函数即变量
2、高阶函数
    a: 把一个函数名当做实参传给另外一个函数（在不修改被装饰函数源代码的情况下为其添加功能）
    例：
        def bar():
            print('in the bar')

        def test1(func):  #test1函数 形参 func
            func()       #  func = bar  func() = bar()
        test1(bar)       # 掉用test1函数时，将bar函数作为一个实参传参给形参func
    b: 返回值中包含函数名 （不修改函数的调用方式）
        def bar():
            print('in the bar')

        def test1(func):  # test1函数 形参 func
            func            # func = bar 内存地址
            return func     #将bar的内存地址返回给test1函数
        bar1 = test1(bar)  # 掉用test1函数时，将bar函数作为一个实参传参给形参func
        bar1()              #调用bar1函数

3、函数嵌套
定义：在一个函数体内使用def去定义一个新的函数
        def foo():
            print('in the foo')
            def bar():
                print('in the bar')
            bar()    #调用bar函数  打印结果 print('in the bar')
        foo()       #调用foo()函数和bar函数  打印结果 print('in the foo') print('in the bar')

'''
import time

def timer(func):
    def sign():
        while True:
            signs = input('请输入用户名>>>')
            if signs== 'alex':
                time.sleep(3)
                pwd = input('请输入密码>>>')
                if pwd == '123':
                    func()      # func() = login() 调用login()运行结果
                else:
                    print('密码不正确')
            else:
                print('用户不正确')
    return sign

@timer
def login():
    print('欢迎登陆')
login()