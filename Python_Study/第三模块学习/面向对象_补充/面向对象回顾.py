#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
1、什么是面向对象编程？
    -   以前使用函数
    -   类 + 对象
2、什么是类什么是对象、又有什么关系？
    class 类：
        def 函数1（）：
            pass
        def 函数2（）：
            pass

    #obj是对象，实例化的过程
    obj = 类（）   实例化一个对象
    obj.函数1()   对象使用函数1功能

3、什么时候适用面向对象?
    -

5、封装？
        -   类中封装了：字段和方法
        -   对象中封装了：普通字段的值
6、继承：

7、静态方法：保存在类中，调用者类（无需创建对象），可以有任意个参数：
            只是名义上归类管理，实际上在静态方法里访问不了类或实例中的任何属性
            实际上使用静态方法后，这个类中方法只是一个函数
class F1:
    @staticmethod
    def a1():
        print('alex')
F1.a1()     # 静态方法：类.方法名----无需创建对象

类方法：
    -   只能访问类变量，不能访问实例变量
类：
    -   属性
            实例变量  =  普通属性
            类变量    =  公有属性
            私有属性  __属性名
    -   方法
            构造方法
            析构函数    实例化被销毁后自动执行一些方法
            私有方法
对象
    -   实例化后一个类之后得到的对象

封装
    -   把一些功能的实现细节不对外暴露

继承
    继承的方式 ---1、继承 2、组合
    -   代码的重用
    -   多继承
        2.7 经典类---深度优先     新式类，广度优先
        3.x 均是广度优先
        class Foo(object): 新式类
            def __init__(self,属性1，属性2,....)
            super(类名,self).__init__(属性1，属性2，属性3)  #新式类写法多继承先继承后重构
    -   单继承
    -   组合
        class Foo(object): 新式类
            def __init__(self,属性1，属性2,....)
            self.person = Person(self,job) 组合的一种方式

多态
    -   接口重用，一种接口，多种实现
'''
class F1(object):
    def __init__(self,n):
        self.N = n
        print("F1")

class F2(object):
    def __init__(self,arg1):
        self.a = arg1
        print("F2")

class F3(object):
    def __init__(self,arg2):
        self.b = arg2
        print("F3")

o1 = F1("alex")
o2 = F2(o1)
o3 = F3(o2)
print(o3.b.a.N)
