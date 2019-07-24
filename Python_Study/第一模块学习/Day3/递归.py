# -*- coding:utf-8 -*-
# Author:D.Gray
'''
递归：在函数内部可以调用其他函数，如果一个函数调用自己就要递归
递归特性：
1、必须有一个明确的结束条件
2、每次进入更深一层递归时，问题规模相比上次递归都应有所减少
3、递归效率不高，递归层次过多导致栈溢出
'''
'''
def calc(n):
    print(n)
    return calc(n+1)
calc(0)                 #最大递归999
'''
def calc2(n):
    print(n)
    if int(n/2) > 0:
        return calc2(int(n/2))
calc2(20)