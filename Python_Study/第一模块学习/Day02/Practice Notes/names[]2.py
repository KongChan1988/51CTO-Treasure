# -*- coding:utf-8 -*-
# Author:D.



names = ['Zhang Yang', 'gu yun', 'xiang peng',['alex','jack'] ,'纳兹','chen rong hua','xu liang chen']


print('\n************(复制列表中添加元素)***************')
names2 = names.copy()  #浅copy 只copy列表第一层
print(names)
print(names2)

print('\n************(复制列表后修改原列表中元素)***************')
names[2] = '向鹏'   #将原列表中'xiang peng'更改为'向鹏'
print(names)        #原列表‘xiang peng’变为‘向鹏’
print(names2)       #names2列表中元素不变

print('\n************(列表嵌套修改原列表中元素)***************')
names[3][0] = 'ALEXADER' #将嵌套列表中的 'alex' 更改为 'ALEXADER'
print(names)
print(names2)   #浅copy只把names列表中第一层copy到了names2中，names子列表['alex','jack']没有被copy到
                #浅copy只是把未改动过的列表元素copy了下来

