# -*- coding:utf-8 -*-
# Author:D.Gray
import sys
'''
作业需求：
1.启动程序后，让用户输入工资，然后打印商品列表
2.允许用户根据商品编号购买商品
3.用户选择商品后，检测是否够，够就直接扣款，不够就提醒
4.可随时退出，退出时，打印移购买商品和余额
'''
shop_list = []

product_list = [
    ('Iphone',5800),
    ('Mac Pro',12000),
    ('Starbuck Latte',31),
    ('Alex Python',81),
    ('Bike',800),
]
user_salary = input('请输入工资>>>:')
if user_salary.isdigit():
    user_salary = int(user_salary)

    while True:
        for index,item in enumerate(product_list):
            print(index,item)

        user_choice = input('请输入商品>>>:')
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice <= len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= user_salary:
                    shop_list.append(p_item)
                    user_salary -= p_item[1]
                    print('商品%s已加入购物车,还剩\033[32;1m %s \033[0m' %(p_item,user_salary))
                else:
                    print('您还剩\033[41;1m %s \033[0m余额，买毛线啊' % user_salary)
            else:
                print('您输入的商品不存在')
        elif user_choice == 'q':
            print('-----Shop List----')
            for p in shop_list:
                print(p)
            sys.exit('您还剩\033[41;1m %s \033[0m余额' % user_salary)
        else:
            print('退出程序')




