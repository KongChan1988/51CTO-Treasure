# -*- coding:utf-8 -*-
# Author:D.Gray

msg = "我爱北京天安门"
print(msg)
print(msg.encode())  #没有指定编码 默认系统中自带的编码转换格式
#print(msg.encode(encoding = "utf-8"))
print(msg.encode(encoding = "utf-8")).decode(decoding="utf-8")