# -*- coding:utf-8 -*-
# Author:D.Gray
import shelve
#创建两个用户字典信息
zhangsan = dict(zip(["name","age"],['zhangsan',32]))
lisi = dict(zip(["name","age"],['lisi',23]))
db = shelve.open('shelvedb')        #打开数据文件
db["zhangsan"] = zhangsan
db["lisi"] = lisi
db.close()

db = shelve.open("shelvedb")
print(db["zhangsan"])         #key一定是字符串形式
print(db["lisi"])



