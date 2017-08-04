# -*- coding:utf-8 -*-
# Author:D.Gray

'''
购物车需求
    用户入口：
1.商品信息存在文件里
2.已购商品，余额记录。第一次启动程序时需要记录工资，第二次启动程序时谈出上次余额
3.允许用户根据商品编号购买商品
4.用户选择商品后，检测是否够，够就直接扣款，不够就提醒
5.可随时退出，退出时，打印移购买商品和余额
    商家入口：
2.可以添加商品，修改商品价格
'''

import os,sys
count = 0
shop_lists = []
porduct_lists = [
    ('Iphon',5800),
    ('Alex Python',50),
    ('Mac Pro',12000),
    ('Bike',800),
('Starbuck Latte',31)
]

user_shop_file = open('user_shop','r+')
user_shop_lists = user_shop_file.readlines()

for user_shop_list in user_shop_lists:
    _shop = user_shop_list.split()
if len(user_shop_lists) == 0:
    login_name = input('请输入用户名>>>:')
    user_info_file = open('user_info','r+')
    user_info_lists = user_info_file.readlines()

    for user_info_list in user_info_lists:
        _user = user_info_list.split()
        if login_name in _user:
            while True:
                login_pwd = input('请输入密码>>>:')
                if login_pwd == _user[1]:
                    print('欢迎 \033[32;1m%s\033[0m来到英雄联盟收银台'%login_name)
                    user_action = input('请输入操作>>>按任意键查看购物列表...按Q退出')
                    if user_action != 'q' or 'Q':
                        while True:
                            user_salary = input('请输入您的工资>>>')
                            if user_salary.isdigit():
                                user_salary = int(user_salary)

                                for item in porduct_lists:
                                    print(porduct_lists.index(item), item)
                                while True:
                                    user_chorise = input('请输入您需购买的商品编号>>>:')
                                    if user_chorise.isdigit():
                                        user_chorise = int(user_chorise)
                                        if user_chorise <= porduct_lists.index(item) and user_chorise >= 0:
                                            p_item = porduct_lists[user_chorise]
                                            print(p_item)
                                            if user_salary >= p_item[1]:
                                                print('买的起')
                                            else:
                                                print('对不起您的金额不足,无法购买此商品')
                                        else:
                                            print('\033[31;1m 请输入范围内商品编号\033[0m')
                                    else:
                                        print('请输入有效商品编号')
                            else:
                                print('请输入有效工资')
                else:
                    print('密码错误请重新输入')
    else:
        sys.exit('用户不存在')
else:
    print('欢迎 \033[31;1m%s\033[0m来到英雄联盟收银台...您还剩 \033[34;1m%s\033[0m 余额'% (_shop[0],_shop[1]))
