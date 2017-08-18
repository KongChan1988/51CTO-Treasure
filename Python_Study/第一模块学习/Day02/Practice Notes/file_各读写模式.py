# -*- coding:utf-8 -*-
# Author:D.Gray

#print('\n-------r+ 读写模式方法-------')       #用处最多
#print('\n-------a+ 写读模式方法-------')       #追加读写模式
print('\n-------w+ 写读模式方法-------')        #实际没啥卵用
f = open('yesterday2','w+',encoding='utf-8')    #写读模式  新创建一个新文本
f.write('------diao-----\n')
f.write('------diao-----\n')
f.write('------diao-----\n')
f.write('------diao-----\n')
print(f.tell())             # 打印字符数
f.seek(10)                  # 回到光标第10行
print(f.readline())        # 打印一行
f.write('should be at the begining of the second line')     # 在写一行到yesterday2文本中


print('\n-------rb 二进制模式方法-------')
f = open('yesterday2','rb')         #文件句柄   二进制文件
print(f.readline())                 #网络传输必须用二进制传输
print(f.readline())                 #二进制文件 最好用二进制  rb 打开读取

f = open('yesterday2','wb')
f.write('hello binary\n'.encode())      #没有根字符集 默认utf-8  不写.encode()会报错
f.close()

#f = open('yesterday2','ab')