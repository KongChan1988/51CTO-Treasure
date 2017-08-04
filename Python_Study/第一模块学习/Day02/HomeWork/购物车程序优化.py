#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
需求：
      1. 启动程序后，第一次用户通过账号密码登录，然后打印商品列表。
      2.第二次登录时直接调取之前购物所剩余额
      3. 允许用户根据商品编号购买商品。
      4. 用户选择商品后，检测余额是否足够，够就直接扣款，不够就提醒充值。
      5. 可随时退出，退出时，打印已购买的商品和余额。
'''
import os,sys
count = 0
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
                    print('欢迎 \033[31;1m %s \033[0m 登录英雄联盟收银台,您的余额还剩 0 元' % login_name)
                    user_action = input('请选择操作>>> 按任意键进入商品列表购买商品>>>退出请按:Q')
                    if user_action == 'q' or 'Q':
                        print('')
                else:
                    print('密码错误请重新输入密码')
    else:
        sys.exit('用户名不存在')
else:
    print('欢迎 \033[31;1m %s \033[0m 登录英雄联盟收银台,您的余额还剩 \033[33;1m %s \033[0m ' % (shop[0], shop[1]))