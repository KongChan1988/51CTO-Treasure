#-*- Coding:utf-8 -*-
# Author: D.Gray
import os,sys
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
# print("PATH",sys.path)

from core import parses

def main_parse(user_input):
    '''
    定义一个main_parse函数，来接受用户操作菜单的选择，并根据用户输入的操作序号进入相应的模块
    :param user_input:用户输入操作菜单序号
    :return:
    '''
    main_dict = {
        '1': main_select,
        '2': main_add,
        '3': main_update,
        '4': main_delect,
    }
    if user_input in main_dict.keys():
        main_dict[user_input]()  # 执行输入号码对应的函数
                                #main_select等主函数没有定义形参所以main_dict[user_input]()括号里不要传参数
    if user_input == '5':
        exit("已退出程序，欢迎下次使用")
    else:
        print("\033[31;1m输入格式无效\033[0m")

def main_select():
    '''
    定义main_select函数——select查询信息管理模块
    用来接受解析并完成的select语句，并显示查询结果
    :return:
    '''
    print('''\t\t\t-------------------------------------------            
              语法示例:
              select * from db.emp
              select * from db.emp where id > 10 and id < 20
              select in,name form db.emp where name like anlex limit 3
\t\t\t-------------------------------------------''')
    parses.parse()
    #print('in the main_select:')


def main_add():
    print('''\t\t\t-------------------------------------------            
              语法示例:
              insert into  * from db.emp
              select * from db.emp where id > 10 and id < 20
              select in,name form db.emp where name like anlex limit 3
\t\t\t-------------------------------------------''')
    parses.parse()
    print('in the main_add:')

def main_update():
    print('''\t\t\t-------------------------------------------            
              语法示例:
              update * from db.emp
              select * from db.emp where id > 10 and id < 20
              select in,name form db.emp where name like anlex limit 3
\t\t\t-------------------------------------------''')
    print('in the main_update:')

def main_delect():
    print('''\t\t\t-------------------------------------------            
                  语法示例:
                  delect * from db.emp
                  select * from db.emp where id > 10 and id < 20
                  select in,name form db.emp where name like anlex limit 3
\t\t\t-------------------------------------------''')
    print('in the main_delect:')
