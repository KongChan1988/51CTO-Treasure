# -*- coding:utf-8 -*-
# Author:D.Gray

es=0
res_out=0
for i in range(0,101):
    if i%2 != 0:
        res=i*(i+1)
        res_out=res_out+res
        print(res_out)

