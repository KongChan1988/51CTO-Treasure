#-*- Coding:utf-8 -*-
# Author: D.Gray
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print("PATH",sys.path)

from core import main

while True:
    print("""\033[35;1m******欢迎来到英雄联盟信息系统*********
        1.查询员工信息
        2.添加员工信息
        3.修改员工信息
        4.删除员工信息
        5.退出\033[0m""")

    user_input = input('请输入操作序号>>>:').strip()
    #user_input = int(user_input)
    main.main_parse(user_input)