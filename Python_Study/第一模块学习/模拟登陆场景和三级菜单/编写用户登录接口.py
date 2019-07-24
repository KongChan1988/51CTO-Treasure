# -*- coding:utf-8 -*-
# Author:D.Gray
# Date:2017/07/17

#作业需求：
#1）用户输入账号密码进行登录
#2）用户信息保存在文件内
#3）用户密码输入错误三次后锁定用户

import sys,getpass,os

count = 0
print('************欢迎来到英雄联盟************')
user_login = input('请输入用户名>>>:')

lock_file = open('lock_info','r+')
lock_list = lock_file.readlines()

for lock_info in lock_list:
    lock = lock_info.split()


    if user_login in lock:
        sys.exit('该用户已被锁定...请联系管理员')

user_file = open('user_info','r+')
user_list = user_file.readlines()

for user_info in user_list:
    user = user_info.split(':')
    password = user[1].split('\n')[0]
    if user_login in user[0]:
        while count < 3:
            user_pwd = input('请输入密码>>>:')
            if user_pwd == password:
                sys.exit('用户验证成功，欢迎\033[32;1m %s \033[0m来到英雄联盟！'% user_login)
            else:
                count += 1
                print('密码错误请重新输入，您还有 %s 次机会' % (3-count))
        else:
            lock_file.write(user_login+'\n')
            sys.exit('该用户已被锁定...请联系管理员')
else:
    sys.exit('该用户不存在...请先注册')

