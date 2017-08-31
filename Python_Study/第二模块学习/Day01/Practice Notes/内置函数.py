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