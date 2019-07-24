# -*- coding:utf-8 -*-
# Author:D.Greay

name = input('name: ')

age = int(input('age: '))
print(type(age))    #打印变量类型

job = input('job: ')
salary = input('salary: ')

#多行打印方法二
print('\n多行输入打印方法二')
info = '''
------  info of  %s -----
Name:%s
Age:%d     
Job:%s
Salary:%s
'''  %(name,name,age,job,salary)
print(info)