#-*- Coding:utf-8 -*-
# Author: D.Gray

from lib.aa import Cat

obj = Cat()
print(obj.__module__)  #表示 cat这个类是从哪个模块导入过来的
print(obj.__class__)  #输出类本身