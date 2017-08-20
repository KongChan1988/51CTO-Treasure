# -*- coding:utf-8 -*-
# Author:D.Gray

list_1 = [1,4,5,7,3,6,7,9]
list_1 = set(list_1)

list_2 = set([2,6,0,66,22,8,4])
print(list_1,'\n',list_2)

print('\n******取出list_1和list_2的交集*******')
print(list_1.intersection(list_2))      #  .intersection()方法 取list_1和list_2的交集
print(list_1 & list_2)

print('\n******取出list_1和list_2的并集*******')
print(list_1.union(list_2))             #  .union()方法 取list_1和list_2的并集
print(list_1 | list_2)

print('\n******取出list_1和list_2的差集*******')
print(list_1.difference(list_2))       #  .difference()方法  取list_1和list_2的差集(list_1有的list_2里没有的)
print(list_1 - list_2)
print(list_2.difference(list_1))        #同理 list_1有的list_2里没有的

print('\n******取出list_1和list_3的子集、父集*******')
list_3 = set([1,3,7])
print(list_3.issubset(list_1))      #  .issubset()子集    list_3集合中的元素在list_1里都有，list_3是list_1的子集
print(list_1.issuperset(list_3))    #  .issuperset()父集  同理list_1是list_3的父集

print('\n******取出list_1和list_2的对称差集*******')
print(list_1.symmetric_difference(list_2))  #把list_1和list_2相互没有的都取出来，就是剔除list_1和list_2的交集
print(list_1 ^ list_2)

print('\n******判断交集之间是否有交集*******')
list_4 = set([2,5,8])
print(list_1.isdisjoint(list_2))      #list_1和list_2有交集，则返回结果 False
print(list_3.isdisjoint(list_4))        #list_3和list_4没有交集，则返回结果 True