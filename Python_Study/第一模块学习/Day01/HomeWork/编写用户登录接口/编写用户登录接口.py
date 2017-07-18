#-*- Coding:utf-8 -*-
# Author: D.Gray

# 创建了user_info是用户文件，user_lock是被锁用户文件
# 作业需求：
# 1. 用户输入帐号密码进行登陆
# 2. 用户信息保存在文件内
# 3. 用户密码输入错误三次后锁定用户

import sys,getpass,os

count = 0  #定义一个while循环次数变量
print('****************欢迎来到英雄联盟******************')
login_name = input('请输入用户名>>>: ')

lock_file = open('user_lock.txt','r+')  #定义lock_file变量以读写模式打开 user_lock.txt文本
lock_list = lock_file.readlines()       #定义lock_list变量读取 user_lock.txt文本内容

for lock_info in lock_list:            #循环遍历user_lock.txt文本内容
    lock = lock_info.split()            #定义一个lock变量，以列表形式存储user_lock.txt文本内容
#print(lock)
    if login_name in lock:              #判断输入的用户名是否已在绑定名单中
        sys.exit('您已被锁定...请联系管理员')


user_file = open('user_info.txt','r+')  #定义user_file变量以读写模式打开 user_info.txt文本
user_list = user_file.readlines()       #定义user_list变量读取 user_info.txt文本内容
for user_info in user_list:             #循环遍历user_info.txt文本内容
    user = user_info.split()            #定义一个user变量，以列表形式存储user_info.txt文本内容
#print(user)
    if login_name in user:              #判断用户是否存在用户列表中
        while count < 3:                #当密码输入次数>3时，退出循环
            login_pwd = input('请输入密码>>>: ')
            if login_pwd == user[1]:    #判断输入密码是否正确
                sys.exit('登录成功,欢迎 %s 登录' % user[0])
            else:
                count += 1
                print('密码输入错误，请重新输入...您还有 %s 次机会' % (3-count))
        else:                          #密码输入>=3时,执行一下操作
            lock_file.write(login_name + '\n')  #把login_name写到文件中，write()并不会在str后加上一个换行符
            sys.exit('密码输错3次,该用户已被绑定')
else:
    sys.exit('用户不存在')             #输入的用户名不在user_info用户列表中，给出“用户不存在提示”
user_file.close()
lock_file.close()