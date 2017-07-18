# -*- coding:utf-8 -*-
# Author:D.Greay

print('多行输入打印方法一')
name = input('name: ')
age = input('age: ')
job = input('job: ')
salary = input('salary: ')

#多行打印方法一
info = '''
------  info of  ''' + name + ''' -------
Name:''' + name + '''
Age:''' + age + '''
Job:''' + job +''' 
Salary:'''+ salary + '''
'''
print(info)


