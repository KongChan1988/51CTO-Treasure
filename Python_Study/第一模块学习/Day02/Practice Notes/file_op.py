# -*- coding:utf-8 -*-
# Author:D.Gray

#data = open('yesterday',encoding='utf-8').read()   #文件句柄
f = open('yesterday2','w',encoding='utf-8')     # 文件模式  w  表示该文本只能写  不能读
                                                # 文件读模式  是新创建新文本 yesterday2
f.write('我爱北京天安门\n')
f.write('天安门上太阳升\n')

f = open('yesterday2','a',encoding='utf-8')   #文件模式   a = append（追加） 表示追加该文本内容,不覆盖原来文件
f.write('\n我爱北京天安门....')               #但不能读
f.write('\n天安门上太阳升....')
f.close()

f = open('yesterday','r',encoding='utf-8')      # 文件模式  r 表示该文本只能读 不能写
data = f.read()
data2 = f.read()
print(data)

print('\n-------f.tell()方法-------')
f = open('yesterday','r',encoding='utf-8')
#print(f.read(5))                            #f.tell()方法表示 读出多少个字符，这里只读前5个字符'每一个寂静'
#print(f.tell())                             # 一个中文占3个字符  就计数 15

print(f.readline())
print(f.readline())
print(f.readline())                         #读了3行总共90个字符数
print(f.tell())                             #打印3行总字符数

print('\n-------f.seek()方法-------')
f.seek(0)                                   # 使用f.seek()方法将光标移动到 0 句柄起始位置
print(f.readline())                         # 从句柄起始位置开始读文本

print(f.encoding)                           #打印文本 字符编码 例 utf-8  gdk
print(f.fileno())                           #打印操作系统文本接口编号

print('\n-------f.flush()方法-------')
f = open('test.text','w')               #新创建 test.text文本
f.write('helloworld1\n')                # 使用 .write()方法 将'helloworld1' 写入test.text文本中
f.flush()                               # 使用 .flush 强制刷新 确保内容100% 写入硬盘test.text文本中
f.write('helloworld2\n')                # 如果不使用.flush()方法  write内容不一定100%写入硬盘中，可能会缓存在内存中


print('\n-------r+ 读写模式方法-------')
f = open('yesterday2','r+',encoding='utf-8')
print(f.readlines())
print(f.readlines())
print(f.readlines())
f.write('---------diao-----')
print(f.readlines())

print('\n-------f.truncate()方法-------')
f = open('yesterday','a',encoding='utf-8')
#f.truncate()            #默认不写为清空'yesterday'文本
f.truncate(20)          #从文本开头开始截断20个字符


