#-*- Coding:utf-8 -*-
# Author: D.Gray
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
#print("PATH",sys.path)

from core import main
'''
需求
(1).工信息表程序，实现增删改查操作：
(2).可进行模糊查询，语法至少支持下面3种:
   select name,age from staff_table where age > 22
   select * from staff_table where dept = "IT"
   select * from staff_table where enroll_date like "2013"
(3).查到的信息，打印后，最后面还要显示查到的条数
(4).可创建新员工纪录，以phone做唯一键，staff_id需自增
(5).可删除指定员工信息纪录，输入员工id，即可删除
(6).可修改员工信息，语法如下:
 　　UPDATE staff_table SET dept = "Market" where dept = "IT"
 注意：以上需求，要充分使用函数，请尽你的最大限度来减少重复代码
 '''
while True:
    print("""\033[35;1m******欢迎来到英雄联盟信息系统*********
        1.查询员工信息
        2.添加员工信息
        3.修改员工信息
        4.删除员工信息
        5.退出\033[0m""")

    user_input = input('请输入操作序号>>>:').strip()

    main.main_parse(user_input)