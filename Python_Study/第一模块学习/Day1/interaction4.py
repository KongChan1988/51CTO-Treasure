# -*- coding:utf-8 -*-
# Author:D.Greay

name = input('name: ')

age = int(input('age: '))
print(type(age))    #打印变量类型

job = input('job: ')
salary = input('salary: ')

#多行打印方法四
print('\n多行输入打印方法四')
info = '''
------  info of  {0} -----
Name:{0}
Age:{1}    
Job:{2}
Salary:{3}
'''  .format(name,age,job,salary)
print(info)