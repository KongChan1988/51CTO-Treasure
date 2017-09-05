#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
作业需求:
模拟实现一个ATM+购物车商城程序
1、额度15000或自定义
2、实现购物商城，买东西加入购物车，调用信用卡接口结账
3、可以提现、手续费5%
4、支持多账户登录
6、支持账户间转账
7、记录每月日常消费流水
8、提供还款接口
9、ATM记录操作日志
10、提供管理接口，包括添加账户、用户额度、冻结账户等
11、用户认证用装饰器
'''

import sys,os
#程序主目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#添加环境变量
sys.path.append(BASE_DIR)

from modules import admincenter,shopping,authentication,creditcard

while True:
    print("\33[35;1m欢迎进入信用卡购物模拟程序\33[0m".center(50, "*"),
          "\n1 购物中心\n"
          "2 信用卡中心\n"
          "3 后台管理\n"
          "q 退出程序\n")
    choice_id = input("\33[34;0m选择要进入模式的ID\33[0m:")
