#-*- Coding:utf-8 -*-
# Author: D.Gray

print(all([0,-1,3]))          # 非0就是true，有0就是false

print(any([0,-1,3]))        #有一个ture，就为真。空列表为false

print('\n------ascii()函数-----')
a = ascii([0,-1,'HelloWorld'])
print(type(a),[a])   #将列表变成可打印的字符串

print('\n------bin()函数-----')
print(bin(10))          #把一个整数转成二进制

print('\n------bool()函数-----')
print(bool([]))      #空列表、空字典、0都为 Fanlse
print(bool(1))

print('\n------bytearray()函数-----')
a = bytes('abcde',encoding='utf-8')     #字符串不能修改
print('原字符串：',a.capitalize(),a)
b = bytearray('abcde',encoding='utf-8')     #使用bytearray将字符串变成ascii码的形式
print('未修改：',b[0])         #  b列表第一个元素a想对应   ascii码=97
b[0] = 50           #将b列表第一个元素a的ascii码97 更改为50，第一个元素a将被赋予新值
print('修改后：',b[0],b)

print('\n------callable()函数-----')
print(callable([]))     #判断是否可调用，后面可以加括号的比如：函数和类 属于可调用
def sayhi():
    pass
print(callable(sayhi))  #函数和类 属于可调用

print('\n------chr()和ord()函数-----')
print('Ascii里97位置所对应的字符：',chr(97))       #chr()括号里只能填一个数子
print('字符所对应Ascii里的位置：',ord('i'))    #ord()括号里只能填单个字符

print('\n------compile()函数-----')
code = '''
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'
f = fib(10)
print(f.__next__())
'''
py_obj = compile(code,'','exec')    #将“生成器.py”文件变成字符串，在“内置函数.py”
exec(py_obj)            #中使用compile（）方法来执行“生成器.py”


print('\n------dir()函数-----')
a = {}
print(dir(a))       #查询a可使用的方法

print('\n------divmod(a,b)函数-----')
b = divmod(5,2)         # 5除以2
print(b)                # 返回结果：（商,余数）

print('\n------filter()函数-----')
def sayhi(n):           #正常函数
    print(n)
sayhi(3)

calc = lambda n:print(n)       #匿名函数，只能处理3元运算，不能处理for循环之类
calc(5)

res1 = filter(lambda n:n>5,range(10))   #一组数据中过滤出你想要的数据。例如：1~10过滤出大于5的
for i in res1:
    print('过滤大于5的数子:',i)

res2 = map(lambda n:n**2,range(10))   #[n**2 for i in range(10)]
for i in res2:                        #把1~10集合里的每一个值进行平方处理
    print('1-10各个数的平方：',i)

import functools
res3 = functools.reduce(lambda x,y:x+y ,range(10))
print('1-10累计相加:',res3)

res4 = functools.reduce(lambda x,y:x*y,range(1,10))
print('从1-10阶乘：',res4)

print('\n------frozenset()函数-----')
a = set([1,4,333,212,33,33,12,4])  #普通形式集合，可以有pop,clear等方法操作
b = frozenset([1,4,33,22,22,12])    #使用frozenset()函数把集合变成不可变集合

print('\n------globals()函数-----')
print(globals())        #返回整个程序的所有变量的k,valus（键值对）格式

print('\n------hash()函数-----')
print(hash('jack'))     #hash字符串的映射，折半算法

print('\n------hex()函数-----')
print(hex(255))         #转化成十六进制

print('\n------locals()函数-----')
def text1():
    local_var = 333
    print(locals())     #打印函数内部局部变量
    print(globals())    #打印全局变量
text1()
print(globals().get('local_var:'))

print('\n------oct()函数-----')
print(oct(255))         #转化成八进制

print('\n------round()函数-----')
print(round(1.3223,2))         #保留2位小数

print('\n------sorted()函数-----')
a = {6:2,8:0,-5:6,1:4,99:11}
print(sorted(a.items()))       #将字典中元素变成列表按key来排序
print(sorted(a.items(),key = lambda x:x[1]))    #将字典中元素按values来排序
print(a)                #字典打印的时候默认是无序排列

print('\n------zip()函数-----')
a = [1,2,3,4,5,6]       #按小的来
b = ['a','b','c','d']
for i in zip(a,b):
    print(i)            #将列表a、b相互对应在一起 例：1对应'a'.


# import 装饰器小高潮 =  _import_('装饰器小高潮')