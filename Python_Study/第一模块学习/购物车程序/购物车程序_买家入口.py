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

def user_shoping():             #定义一个用户购买商品操作函数
    while True:
        user_salary = input('请输入您的充值金额>>>:')
        if user_salary.isdigit():           #判断充值金额是否为数字
            user_salary = int(user_salary)
            user_shop_file.write(login_name + '\t')
            user_shop_file.write(str(user_salary) + '\n')
            for item in porduct_lists:      #循环遍历商品列表
                print(porduct_lists.index(item), item)      #使用index方法打印列表序号，item为列表元素
                p_index = porduct_lists.index(item)         #定义p_index方法存储列表序号
            while True:
                user_choises = input('请选择您所需购买的商品编号>>>:退出请按:Q:')
                if user_choises.isdigit():                 #判断用户输入的商品编号是否为数字
                    user_choises = int(user_choises)
                    if user_choises <= p_index and user_choises >= 0:   #用户输入编号小于列表序号
                        p_item = porduct_lists[user_choises]            #定义p_item方法获取用户选择的商品
                        p_item[1] = int(p_item[1])                      #将商品金额强制转换为int类型
                        if user_salary >= p_item[1]:                    #判断用户金额是否买得起商品
                            shop_lists.append(p_item)                   #将已购买的商品信息存储到shop_lists列表中
                            user_salary -= p_item[1]                    #扣除商品金额=还剩余额
                            user_shop_file.write(login_name + '\t')
                            user_shop_file.write(str(user_salary) + '\n')   #将用户信息和余额信息写入user_shop文本中
                            print("商品 \033[32;1m%s\033[0m 已加入购物车...您还剩\033[32;1m%s\033[0m余额" % (p_item[0], user_salary))
                        else:
                            print('\033[31;1m对不起您的金额不足，请去充值!\033[0m')
                            print('已购商品清单'.center(30, '*'))
                            print(shop_lists)
                            sys.exit()
                    else:
                        print('\033[31;1m请输入范围内商品编号\033[0m')
                elif user_choises == 'q' or user_choises == 'Q':
                    print('已购商品清单'.center(30, '*'))
                    print(shop_lists)
                    sys.exit()
                else:
                    print('\033[31;1m请输入有效商品编号\033[0m')
        else:
            print('\033[31;1m请输入有效充值金额\033[0m')
def user_top():             #定义一个用户充值操作函数
    while True:
        user_salary = input('请输入您的充值金额>>>:')
        if user_salary.isdigit():
            user_salary = int(user_salary)
            user_salary += int(shop[-1])        #用户现有余额=充值金额+上次还剩余额
            user_shop_file.write(shop[0] + '\t')
            user_shop_file.write(str(user_salary)+'\n')     #将用户名和现有余额（充值完成后还剩余额）写入user_shop文本中
            print('您当前余额为:\033[32;1m%s\033[0m'%user_salary)
            for item in porduct_lists:
                print(porduct_lists.index(item), item)
                p_index = porduct_lists.index(item)
            while True:
                user_choises = input('请选择您所需购买的商品编号>>>:退出请按:Q:')
                if user_choises.isdigit():
                    user_choises = int(user_choises)
                    if user_choises <= p_index and user_choises >= 0:
                        p_item = porduct_lists[user_choises]
                        if user_salary >= int(p_item[1]):
                            shop_lists.append(p_item)
                            user_salary -= int(p_item[1])
                            user_shop_file.write(shop[0] + '\t')
                            user_shop_file.write(str(user_salary) + '\n')
                            print("商品 \033[32;1m%s\033[0m 已加入购物车...您还剩\033[32;1m%s\033[0m余额" % (p_item[0], user_salary))
                        else:
                            print('\033[31;1m对不起您的金额不足，请去充值!\033[0m')
                            print('已购商品清单'.center(30, '*'))
                            print(shop_lists)
                            sys.exit()
                    else:
                        print('\033[31;1m请输入范围内商品编号\033[0m')
                elif user_choises == 'q' or user_choises == 'Q':
                    print('已购商品清单'.center(30, '*'))
                    print(shop_lists)
                    sys.exit()
                else:
                    print('\033[31;1m请输入有效商品编号\033[0m')
        else:
            print('\033[31;1m请输入有效充值金额\033[0m')
def porduct_shop():         #定义一个读取porduct_shop（商品信息文本）函数
    user_porduct_file = open('porduct_shop', 'r+', encoding='utf-8')
    user_porduct_lists = user_porduct_file.readlines()      #以列表形式读取porduct_shop商品信息文本内容
    for user_porduct_list in user_porduct_lists:            #循环遍历user_porduct_lists列表
        porduct_lists.append(user_porduct_list.split())     #将读取内容存储到porduct_lists商品列表中


login_name = ''
shop_lists = []
porduct_lists = []

porduct_shop()                            #调用porduct_shop（读取卖家商品信息）操作函数

user_shop_file = open('user_shop','r+')
user_shop_lists = user_shop_file.readlines()
for user_shop_list in user_shop_lists:          #循环遍历user_shop(用户信息及余额)文本内容
    shop = user_shop_list.split()
if len(user_shop_lists) == 0:                   #判断user_shop文本信息内容是否为空
    login_name = input('请输入用户名>>>:')      #如果为空，则判断为首次登陆，需要填写用户名和密码
    user_info_file = open('user_info','r+')
    user_info_lists = user_info_file.readlines()
    for user_info_list in user_info_lists:      #循环遍历user_info(用户信息：用户名和密码)文本内容
        user = user_info_list.split()
        if login_name in user:                  #判断输入的用户名是否存在
            while True:
                login_pwd = input('请输入密码>>>:')      #判断用户输入密码是否正确
                if login_pwd == user[1]:
                    print('欢迎 \033[33;1m%s\033[0m 登录英雄联盟收银台' % login_name)   #登陆成功
                    user_shoping()
                else:
                    print('\033[31;1m密码错误请重新输入密码\033[0m')
    else:
        sys.exit('\033[31;1m用户名不存在\033[31;1m')
else:                #用户不是首次登陆操作
    print('欢迎 \033[33;1m%s\033[0m 登录英雄联盟收银台,您的余额还剩\033[32;1m%s\033[0m元' % (shop[0], shop[-1]))
    user_top()      #调用 user_top(用户第二次登陆和充值操作)函数
































