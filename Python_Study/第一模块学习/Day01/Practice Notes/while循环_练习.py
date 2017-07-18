#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
熟食店：创建一个名为sandwich_orders的列表，在其中包含各种三明治的名字;再创建一个名为finished_sandwiches的
空列表。遍历列表sandwich_orders,对于其中的每种三明治，都打印一条消息，如 I made your tuna sandwich,并将
其移到列表finished_sandwiches。所有三明治都制作好后，打印一条消息，将这些三明治列出来
'''
sandwich_orders = ['Eel_sandwich','Ham_sandwich','Bacon_sandwich']
finished_sandwiches = []

while sandwich_orders:
    finishing_sandwich = sandwich_orders.pop()#定义一个finishing_sandwich变量  并使用pop（）方法循环删除
                                              #sandwich_orders表中元素
    print('I made you ',finishing_sandwich)
    finished_sandwiches.append(finishing_sandwich)#循环将finishing_sandwich元素，添加到
                                                  #finished_sandwiches列表中
print('\n---Your sandwich is ready ---')
for finished_sandwiche in finished_sandwiches: #循环遍历finished_sandwiches列表中的元素
    print(finished_sandwiche)



