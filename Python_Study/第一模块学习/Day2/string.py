# -*- coding:utf-8 -*-
# Author:D.Gray

name = 'alex'
print(name.capitalize())    #首字母大写

name = 'my name is alex'
print(name.count('a'))      #统计字符串总a的个数

print('\n********字符串补足*********')
print(name.center(50,'-'))  #一共打印50个字符，不足的以‘-’补足
print(name.ljust(50,'*'))   #一共打印50个字符，不足的在字符串最后以‘*’补足
print(name.rjust(50,'+'))   #一共打印50个字符，不足的在字符串开头以‘+’补足

print(name.encode())        #把字符串转出二进制
print(name.endswith('ex'))  #判断字符串是否以什么结尾    可判断邮箱是否以 .com结尾

name = 'my \t name is alex'
print(name.expandtabs(tabsize=30))      #把Tab键转出多少个空格

print('\n********字符串切片*********')
print(name.find('name'))    #取出 'name' 所在下标
print(name[name.find('name'):])   #字符串切片，从name开始 切片到 字符串结束

print('\n********字符串format赋值*********')
name = 'my name is {name} and i am {year} old '
print(name.format(name = 'alex',year = 23))
print(name.format_map({'name':'alex','year':23}))

print('\n********字符串是否包含英文字符和数字*********')
print('ab123'.isalnum())  #检查字符串是否包含  英文字符和数字
print('ab123/'.isalnum())

print('\n********字符串是否是否纯英文字符*********')
print('abA'.isalpha())   #检查字符串是否  纯英文字符
print('abA123'.isalpha())

print('\n********字符串是否是整数*********')
print('1.23'.isdigit())   #检查字符串是否是整数
print('1'.isdigit())
print('1A'.isidentifier())  #判断是不是一个合法的标识符
print('33'.isnumeric())     #检查字符串是否是整数
print('My Name Alex'.istitle())     #检查字符串是否首字母大写
print('My Name Is   '.isupper())    #检查字符串是否都大写
print('+'.join(['1,2,3,4']))


print('\n********字符串大小写转换*********')
print('AlEx'.lower())  #将字符串变成小写
print('alex'.upper())   #将字符串变成大写
print('\nAlex'.lstrip())    #去掉字符串左边换行
print('Alex\n'.rstrip())    #去掉字符串右边换行
print('    Alex\n'.strip())     #去掉字符串左右两边换行和空格

print('\n********将字符串转换成对应的字符*********')
p = str.maketrans('abcdefli','123$@456')
print('alex li'.translate(p))
print('------')

print('\n********将字符串中某一字符替换成另一个字符*********')
print('alex li'.replace('e','E'))  #将字符串中某一字符替换成另一个字符
print('alex li'.replace('l','L',2))  #将‘alex li’字符串中的两个 l 替换成 L  最后一个数字表示 替换多少个

print('alex li'.rfind('l'))     #将字符串从左往右数，找到最右边字符的下标  此时最右边'l'字符下标为5
print('alex lil'.rfind('l'))    #将字符串从左往右数，找到最右边字符的下标  此时最右边'l'字符下标为7

print('\n********剔除字符串中的某一字符作为分隔符以列表形式输出*********')
print('1+2+3+4+5+6'.split('+'))     #将字符串中的‘+’剔除作为分隔符，以列表形式打印[1,2,3,4,5,6]
print('1+2\n+3+4+5+6'.splitlines())     #
print('1+2\n+3+4+5+6'.split('\n'))

print('Alex Li'.swapcase())     #将字符串中大小写互换，小写变大写，大写变小写

print('Alex Li'.zfill(50))      #