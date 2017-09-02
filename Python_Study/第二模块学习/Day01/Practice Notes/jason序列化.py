#-*- Coding:utf-8 -*-
# Author: D.Gray
import json     #json 只能处理简单的转换，如字典，列表

# def sayhi(name):          #json不能转换函数
#     print('hello',name)

info = {
    'name':'alex',
    'age':22,
    #'func':sayhi
}
f = open('text','w')
#f.write(str(info))          # 文件只能存字符串，不能存字典
print(json.dumps(info))     #   将字典转换城字符串，并存入text文件
f.write(json.dumps(info))   # 3.0里只能dumps一次
f.close()

