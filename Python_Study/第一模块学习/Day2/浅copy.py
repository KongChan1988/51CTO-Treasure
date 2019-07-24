# -*- coding:utf-8 -*-
# Author:D.Gray

import copy
person = ['name',['saving',100]]
'''
p1 = person.copy()  #第一种方式浅copy
print(p1)
p2 = person[:]      #第二种方式浅copy
print(p2)
p3 = list(person)   #第三种方式浅copy
print(p3)
'''
p1 = person[:]    #p1和p2都浅copy了person列表
p2 = person[:]
print(p1,p2)
p1[0] = 'alex'     #把p1列表中序号0的元素变为'alex'
p2[0] = 'fengjie'
print(p1,p2)
p1[1][1] = 50     #把p1列表中子列表中序号 100 变为 50
print(p1,p2)
print(p2)





