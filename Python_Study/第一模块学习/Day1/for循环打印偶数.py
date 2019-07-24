# -*- coding:utf-8 -*-
# Author:D.Greay
for i in range(0,10,3):  #3为步长
    print('lop:',i)

print('\nfor循环练习二')
for i in range(0,10):
    if i < 3:
        print('lop ', i)
    else:
        continue  #跳出本次循环继续下一个循环
    print('hehe...')

print('\nfor循环练习三')
for i in range(10):
    print('--------',i)
    for j in range(10):
        print(j)
        if j > 5:
            break
