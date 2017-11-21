#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
作业需求：
   模拟实现一个ATM + 购物商城程序
   额度 15000或自定义
   实现购物商城，买东西加入 购物车，调用信用卡接口结账
   可以提现，手续费5%
   支持多账户登录
   支持账户间转账
   记录每月日常消费流水
   提供还款接口
   ATM记录操作日志
   提供管理接口，包括添加账户、用户额度，冻结账户等。。。
   用户认证用装饰器
'''
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import main

main.run()

