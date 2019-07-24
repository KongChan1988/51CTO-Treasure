#-*- Coding:utf-8 -*-
# Author: D.Gray
import pickle
def sayhi(name):
    print('hell:',name)

f = open('text','rb')
# data = (pickle.loads(f.read()))
data = pickle.load(f)       #这个方法替代简化了 # data = (pickle.loads(f.read()))

print('data:',data)
print('data[func]:',data['func'])
print('data[func](kyo)',data['func']('kyo'))