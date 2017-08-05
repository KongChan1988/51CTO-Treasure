#-*- Coding:utf-8 -*-
# Author: D.Gray
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
porduct_lists = [
    ('李白传说皮肤',3880),
    ('花木兰',1888),
    ('武则天皮肤',12000),
    ('小学生',80),
    ('貂蝉皮肤',590)
]
shop_lists = []
user_shop_file = open('user_shop','r+')
user_shop_lists = user_shop_file.readlines()

for user_shop_list in user_shop_lists:
    shop = user_shop_list.split()
if len(user_shop_lists) == 0:
    login_name = input('请输入用户名>>>:')
    user_info_file = open('user_info.txt','r+')
    user_info_lists = user_info_file.readlines()
    for user_info_list in user_info_lists:
        user = user_info_list.split()
        if login_name in user:
            while True:
                login_pwd = input('请输入密码>>>:')
                if login_pwd == user[1]:
                    user_shop_file.write(login_name + '\t')
                    print('欢迎 \033[33;1m%s\033[0m 登录英雄联盟收银台' % login_name)
                    user_salary = input('请输入您的充值金额>>>:')
                    if user_salary.isdigit():
                        user_salary = int(user_salary)
                        for item in porduct_lists:
                            print(porduct_lists.index(item),item)
                            p_index = porduct_lists.index(item)
                        while True:
                            user_choises = input('请选择您所需购买的商品编号>>>:退出请按:Q:')
                            if user_choises.isdigit():
                                user_choises = int(user_choises)
                                if user_choises <= p_index  and user_choises >= 0:
                                    p_item = porduct_lists[user_choises]
                                    if user_salary >= p_item[1]:
                                        shop_lists.append(p_item)
                                        user_salary -= p_item[1]
                                        user_shop_file.write(str(user_salary) + '\n')
                                        print("商品 \033[32;1m%s\033[0m 已加入购物车...您还剩\033[32;1m%s\033[0m余额" %(p_item[0],user_salary))
                                    else:
                                        print('\033[31;1m对不起您的金额不足，请去充值!\033[0m')
                                        print('已购商品清单'.center(30, '*'))
                                        sys.exit(shop_lists)
                                else:
                                    print('\033[31;1m请输入范围内商品编号\033[0m')
                            elif user_choises == 'q' or user_choises == 'Q':
                                print('已购商品清单'.center(30, '*'))
                                print(shop_lists)
                                sys.exit()
                            else:
                                print('\033[31;1m请输入有效商品编号\033[0m')
                    else:
                        print('\033[31;1m请输入有效工资金额\033[0m')
                else:
                    print('\033[31;1m密码错误请重新输入密码\033[0m')
    else:
        sys.exit('\033[31;1m用户名不存在\033[31;1m')
else:
    print('欢迎 \033[31;1m %s \033[0m 登录英雄联盟收银台,您的余额还剩 \033[32;1m %s \033[0m ' % (shop[0], shop[1]))