#!/usr/bin/env python
# -*- coding:utf-8 -*-


# def f1():
# a = 888
#     def f2():
#         return 123
#     return f2
#
# a = f1()
# result = a()
# print(result)

def f1(b, a=[]):
    a.append(b)
    print(a)


f1(1)
f1(2)
f1(3, [1, 2, 3, 4])
f1(5)