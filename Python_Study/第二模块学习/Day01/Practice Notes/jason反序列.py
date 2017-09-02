#-*- Coding:utf-8 -*-
# Author: D.Gray
import json

f = open('text','r')
data = json.loads(f.read())     #反序列用json.loads
print(data,data['age'])

