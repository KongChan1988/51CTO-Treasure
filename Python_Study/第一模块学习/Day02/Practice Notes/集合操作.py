# -*- coding:utf-8 -*-
# Author:D.Gray

print('\n*******添加集合*******')
list_1 = set([1,4,5,7,3,6,7,9])
list_1.add(99)                      # .add()方法就是在list_1集合中添加单个集合元素
print(list_1)

list_1.update([20,777,45])          #   .update()方法就是在 list_1集合中添加多个集合元素
print(list_1)

print('\n*******删除集合*******')
list_1.remove(20)                  #    .remove()方法就是 在 list_1集合中删除集合元素20
#list_1.remove(21)                 #   使用.remove()删除一个不包含在list_1集合中的元素时会报错
print(list_1)
list_1.discard(777)                 #   .discard()方法和remove()方法相同
list_1.discard('ddd')               #  只是使用.discard()方法后删除list_1中不包含的元素时也不会报错
print(list_1)

print('\n*******随机删除集合元素*******')
print(list_1.pop())
print(list_1.pop())




