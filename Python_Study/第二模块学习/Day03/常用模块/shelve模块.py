#-*- Coding:utf-8 -*-
# Author: D.Gray

import shelve
import datetime
'''
shevle模块是一个简单的键、值将内存数据通过文件持久化任何pickle可支持的python数据样式
'''
d = shelve.open('shelve_test')  #用shelve打开一个文件
print(d.get('name'))
print(d.get('info'))
print(d.get('date'))
info = {'age':22,"job":'IT'}
name = ["alex",'rain','test']

d['name'] = name  #持久化列表  将d['name']为键，赋值 name列表为值
d['info'] = info  #持久化dict
d['date'] = datetime.datetime.now()
d.close()