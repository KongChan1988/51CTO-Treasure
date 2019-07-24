# -*- coding:utf-8 -*-
# Author:D.Gray

'''
class Person(object): #新式类
    super

class Person: #经典类
    ParentClass.__init__

广布查询：一层一层的查
深度查询：一条线的查
python3中经典类和新式类都是广布查询
python2中经典类是深度查询，新式类是广布查询
'''

class A(object):
    def __init__(self):
        self.n = 'A'

class B(A):
    def __init__(self):
        self.n = 'B'

class C(A):
    def __init__(self):
        self.n = 'C'

class D(B,C):   # python3 中从左到右开始继承，有B就先找B，没B就找C
                # python2 中 经典类：有B就找B，没B就找A
    pass
    # def __init__(self):
    #     self.n = 'D'

d = D()
print(d.n)

