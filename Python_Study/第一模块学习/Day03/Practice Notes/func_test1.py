#-*- Coding:utf-8 -*-
# Author: D.Gray

'''
几种编程方式：
1、面向对象----比作华山派----->类----->class
2、面向过程----比作少林派----->过程----->def
3、函数式编程----比作逍遥派---->函数---->def
'''
'''
函数定义
1、初中数学函数定义：y=2x    x是自变量  y是因变量  y是x函数
2、编程语言中函数定义： 函数是逻辑结构化和过程化的一种编程方法
3、函数优点：1、代码重用性  2、保持一致性  3、可扩展

python中函数定义方法:
def test(x):
    'The function definitions'
    x += 1
    return x
def：定义函数的关键字
test：函数名
（）：内可定义形参
''：文档描述。强烈建议为你的函数添加描述信息
x += 1 ：泛指代码块或程序处理逻辑
return：定义返回值
'''
def func1():
    '''定义函数'''
    print('in the func1')
    return 0

def func2():
    '''定义过程'''       #过程就是没有返回值的函数
    print('in the func2')

x = func1()     #func1的返回值是0
y = func2()     #func2没有返回值，结果为None

print('from func1 return is %s' %x)
print('from func2 return is %s' %y)
