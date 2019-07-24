# -*- coding:utf-8 -*-
# Author:D.Gray

info = input('请输入行数>>>')
if info.isdigit():
    info = int(info)
    item = '*'
    for i in range(info+1):
        print(i*str(item))
else:
    print('请输入有效行数')