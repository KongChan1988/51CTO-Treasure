# -*- coding:utf-8 -*-
# Author:D.Gray

f = open('yesterday','r',encoding='utf-8')
'''
print(f.readline())             # 读yesterday前一行
print(f.readline())             # 读yesterday前二行
print(f.readlines())            # 以列表形式打印文本yesterday  f.readlines()只适合读小文件
'''
'''
比较low的写法
#循环遍历yesterday文本，遍历到第10行打印分割线
for index,line in enumerate(f.readlines()):    #使用enumerate方法把每一行下标取出来
    if index == 9:                             #当下标值=9
        print('--------分割线--------')
        continue
    print(line.strip())
'''
count = 0
for line in f:
    count += 1
    if count == 10:
        print('--------分割线--------\n')
    print(line.strip())                 #一行一行读 读一行删一行 内存中只存一行

