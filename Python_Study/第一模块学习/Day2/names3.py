# -*- coding:utf-8 -*-
# Author:D.Gray
import copy   #先导入copy模块
names = ['Zhang Yang', 'gu yun', 'xiang peng',['alex','jack'] ,'纳兹','chen rong hua','xu liang chen'] #原始列表数据

print('\n************(深copy列表中元素)***************')
names2 = copy.deepcopy(names)  #用copy.deepcopy()方法深深copy一份names
names[2] = '向鹏'              #将names列表中'xiang peng'更改为 向鹏
names[3][0] = 'ALESANDER'      #将names子列表中'alex'变为'ALEXANDER'
print(names)
print(names2)                  #names2列表完全复制了name原始列表数据

print('\n************(列表步长切片)***************')
print(names[0:-1:2])  #从第一个索引开始到'chen rong hua'结束,隔2步长取一个元素
print(names[::2])     #