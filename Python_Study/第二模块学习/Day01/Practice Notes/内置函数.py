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