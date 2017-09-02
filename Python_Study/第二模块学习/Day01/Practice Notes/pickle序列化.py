#-*- Coding:utf-8 -*-
# Author: D.Gray
import pickle       #pickle可以序列化python所有数据类型
                    #pickle只能在python本语言中使用
def sayhi(name):
    print('hello：',name)

info = {
    'name':'alex',
    'age':22,
    'func':sayhi
}

f = open('text','wb')   #  pickle.dumps必须要用wb或rb
# f.write(pickle.dumps(info))
pickle.dump(info,f)     # 这个方法替代了 f.write(pickle.dumps(info))
f.close()
