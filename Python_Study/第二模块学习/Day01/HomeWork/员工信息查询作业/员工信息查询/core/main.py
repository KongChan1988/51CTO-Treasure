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
    print('''\t\t\t-----------------------------------------------------------------------------------            
                语法示例:
                select name,age from db.emp where age > 22
                select * from db.xmp where dept like IT
                select * from db.emp where id >= 2
                select * from db.emp where id <5 limit 3
\t\t\t-----------------------------------------------------------------------------------''')
    while True:
        user_sql = input('请输入查询sql语句>>>:').strip()
        sql_list = user_sql.split(' ')  # 将用户输入的sql语句转换成列表格式
        func = sql_list[0]

        if func != 'select':
            print('\033[31;1m请输入相应sql关键字\033[0m')
            if user_sql == 'b':
                break
        else:
            parses.parse(user_sql,func,sql_list)

def main_add():
    '''
    定义main_add函数——insert查询信息管理模块
    用来接受解析并完成的insert语句，并显示查询结果
    :return:
    '''
    print('''\t\t\t-----------------------------------------------------------------------------------            
                语法示例:
                insert db.emp value Mark,32,13655818285,CTO,2014-08-08
                insert db.xmp value Mark,32,13655818285,CTO,2014-08-08
\t\t\t-----------------------------------------------------------------------------------''')
    while True:
        user_sql = input('请输入查询sql语句>>>:').strip()
        sql_list = user_sql.split(' ')  # 将用户输入的sql语句转换成列表格式
                                        # split()输出结果为[]此时会报错  建议split(' ')输出结果['']
                                        # 以空格为分隔符切分成列表形式
        func = sql_list[0]
        if func != 'insert':
            print('\033[31;1m请输入相应sql关键字\033[0m')
            if user_sql == 'b':
                break
        else:
            parses.parse(user_sql,func,sql_list)


def main_update():
    '''
    定义main_update函数——update查询信息管理模块
    用来接受解析并完成的update语句，并显示查询结果
    :return:
    '''
    print('''\t\t\t-----------------------------------------------------------------------------------            
                语法示例:
                update db.xmp set dept = Market where dept like IT
                update db.emp set phone = 15618285621 where phone = 110
                update db.emp set enroll_data = 2014-08-11 where dept like 运维
\t\t\t-----------------------------------------------------------------------------------''')
    while True:
        user_sql = input('请输入查询sql语句>>>:').strip()
        sql_list = user_sql.split(' ')  # 将用户输入的sql语句转换成列表格式
        func = sql_list[0]
        if func != 'update':
            print('\033[31;1m请输入相应sql关键字\033[0m')
            if user_sql == 'b':
                break
        else:
            parses.parse(user_sql,func,sql_list)


def main_delect():
    '''
    定义main_delect函数——delect查询信息管理模块
    用来接受解析并完成的delect语句，并显示查询结果
    :return:
    '''
    print('''\t\t\t-----------------------------------------------------------------------------------            
                语法示例:
                delect from db.emp
                delect from db.emp where id = 3 
                delect from db.emp where  id < 10 and name like alex
\t\t\t-----------------------------------------------------------------------------------''')
    while True:
        user_sql = input('请输入查询sql语句>>>:').strip()
        sql_list = user_sql.split(' ')  # 将用户输入的sql语句转换成列表格式
        func = sql_list[0]

        if func != 'delect':
            print('\033[31;1m请输入相应sql关键字\033[0m')
            if user_sql == 'b':
                break
        else:
            parses.parse(user_sql,func,sql_list)

