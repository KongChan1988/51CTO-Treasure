# -*- coding:utf-8 -*-
# Author:D.Gray
import copy
person = ['alex',['saving',100],'jack']
person2 = person.copy()   #person2浅copy一份person
print(person)
print(person2)

print('\n修改person中某个元素后浅copy后person2不会变')
person[0]='mary'
print(person)   #['mary', ['saving', 100], 'jack']
print(person2)  #['alex', ['saving', 100], 'jack']

print('\n修改person中第二层列表某个元素后浅copy后person2会变')
person[1][1] = 500
print(person)   #['mary', ['saving', 500], 'jack']
print(person2)  #['alex', ['saving', 500], 'jack']  浅copy只是copy第一层列表，第一层列表修改后person2是不会改变
                #但第二层列表只是复制了一个内存地址所以person2也会改变

print('\n深copy一份person，person2会完全复制一份修改后的person')
person2 = copy.deepcopy(person)
print(person)  #['mary', ['saving', 500], 'jack']
print(person2) #['mary', ['saving', 500], 'jack']