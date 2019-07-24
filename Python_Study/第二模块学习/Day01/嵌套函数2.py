# -*- coding:utf-8 -*-
# Author:D.Gray

def outer():
    def inter():
        print('in the inter')
    return inter

foo = outer()
print(foo())
