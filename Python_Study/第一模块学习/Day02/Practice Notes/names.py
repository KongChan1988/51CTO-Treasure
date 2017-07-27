# -*- coding:utf-8 -*-
# Author:D.Gray

#names = 'ZhangYang Guyun Xiangpeng Xuliangchen'
names = ['Zhang Yang', 'gu yun', 'xiang peng', '纳兹','chen rong hua','xu liang chen']

print(names[0].title())
print(names[1:3])  #列表切片   把guyun和xiangpeng 一块取出来  1是起始值   3表示不包括 xu liang chen
print(names[-1].title()) # 取列表 最后一个元素
print(names[-2:]) #取列表倒数第N个元素
print(names[0:3]) #取列表前3个元素
print(names[:3]) #取列表前3个元素

print('\n************(在列表中添加元素)***************')
names.append('lei hai dong')  #添加列表元素 默认添加在列表最后
print(names)

print('\n**********(在列表中插入元素)*********')
names.insert(1,'chen rong hua ') # 把'chen rong hua'插入在列表1的位置 也就是'gu yun'的前面
print(names)
names.insert(3,'xin zhi yun')  #把'xin zhi yun'插入在列表3的位置 也就是'xiang peng'的前面
print(names)

print('\n**********(更改列表中的元素)*********')
print('原列表',names)
names[2] = 'xie di'    #将原列表中第2个元素 更改为'xie di'
print('更改列表后',names[:4])

print('\n**********(删除列表中的元素)*********')
#names.remove('chen rong hua')  #第一种方法
#del names[1]  = names.pop(1) #第二种方法

names.pop()  #默认不输入下标删掉最后一个列表元素，输入下标就删除下标所对应的列表元素
print(names)


print('\n**********(查找列表中的元素)*********')
print(names.index('xie di'))  #打印出xiedi所在列表位置
print( names[names.index('xie di')] )  #打印出'xie di'



print('\n**********(统计列表中的元素)*********')
print(names.count('chen rong hua'))    #count()  统计列表中某元素的个数


print('\n**********(反转列表中的元素)*********')
names.reverse()
print(names)

print('\n**********(按首字母排序列表中的元素)*********')
names.sort()  #优先级：特殊字符>>>数字>>>大写字母>>>字母>>>汉字
print(names)

print('\n**********(合并列表中的元素)*********')
names2 = [1,2,3,4]
names.extend(names2)  #把names2列表合并到names列表中
#del names2           #把列表2删除后，在合并会报错
print(names,names2)   #合并后names2列表扔存在

print('\n**********(清空列表中的元素)*********')
names.clear()  #clear() 清空列表元素
print(names)




