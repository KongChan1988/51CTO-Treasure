# -*- coding:utf-8 -*-
# Author:D.Greay
name = input('name: ')

age = int(input('age: '))
print(type(age))    #打印变量类型

job = input('job: ')
salary = input('salary: ')

#多行打印方法三
print('\n多行输入打印方法三')
info = '''
------  info of  {_name} -----
Name:{_name}
Age:{_age}    
Job:{_job}
Salary:{_salary}
'''  .format(_name=name,
             _age=age,
             _job=job,
             _salary=salary)
print(info)
