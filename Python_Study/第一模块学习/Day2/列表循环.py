# -*- coding:utf-8 -*-
# Author:D.Gray

names = ['Zhang Yang', 'gu yun', 'xiang peng',['alex','jack'] ,'纳兹','chen rong hua','xu liang chen'] #原始列表数据

print('\n************(打印列表下标一)***************')
for item in names:                #先循环遍历names列表
    print(names.index(item),item) #然后使用.index()方法打印出列表的下标

print('\n************(打印列表下标二)***************')
for index,item in enumerate(names):    #先循环并使用 enumerate()方法包围names列表
    print(index,item)                  #打印index下标

print('\n************(打印语句变色)***************')
print('你好 \033[31;1m %s \033[0m' % names[2].title())   #31是红色  32是绿色