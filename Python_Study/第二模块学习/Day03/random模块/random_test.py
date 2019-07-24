#-*- Coding:utf-8 -*-
# Author: D.Gray

'''
random模块
random.random：随机0-1的浮点数
random.randint(x,y):  随机x-y之间的整数
random.randrange(x,y)：随机 x-（y-1）之间的整数
random.choice('str'或者[1,2,3]或者(1,2,3)) : 随机取字符串、列表、元组中的某一元素
random.sampie('序列类型',x):  随机取序列类型中 x个元素
random.uniform(x,y):随机x-y之间的浮点数
random.shuffle([1,2,3,5,6]) ： 随机打乱序列类型中元素的位置顺序
例：
l = [1,2,3,4,5]
random.shuffle(l)
print(l)
'''
import random

checkcode = ''  # i=0时--->根据current判断给checkcode赋值第一个字符串 循环四次
for i in range(11):  # 定义一个 0-3的for循环
    current = random.randint(0,11)  # 定义一个随机整数变量 current
    #print(i,current)
    if current == i:     # 当 current == i时
        tmp = chr(random.randint(65,90))   # 给tmp赋值一个 随机大写字母
    else:           #当 current != i时
        tmp = random.randint(0,9)   # 给tmp赋值一个 0-9随机数子
    checkcode += str(tmp)
print(checkcode)



