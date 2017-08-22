#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
作业需求
1、从info.txt文件中读取员工及其工资信息，最后将修改或增加的员工工资信息也写入原info.txt文件。
2、能增查改员工工资
3、增、改员工工资用空格分隔
4、实现退出功能
'''
import sys,os

operation_lists = '''1.查询工资
2.修改工资
3.增加新员工记录
4.删除员工信息
5.退出'''
user_dict = {}                  #定义一个存储员工姓名及工资的空字典
def user_information():
    '''定义一个员工信息函数'''
    with open('info','r') as f:
        for i in f:
            i = i.strip()           #剔除字符串中的前后空格和换行
            user_dict[i.split()[0]] = i.split()[1]      #将员工姓名及工资存储到user_dict字典中，i.split()[0]=员工姓名 作为键
                                                        #i.split()[0]=员工工资  作为值
            print('当前员工姓名：',i.split()[0])

def user_operations():
    '''定义一个用户操作的函数'''
    while True:
        print(operation_lists)
        user_operation = input('请选择操作编号>>>:')
        if user_operation.isdigit():
            user_operation = int(user_operation)
            if user_operation > 5:
                print('\033[31;1m请输入有效操作编号\033[0m')
            if user_operation == 1:
                user_enquiries()
            if user_operation == 2:
                salary_change()
            if user_operation == 3:
                add_users()
            if user_operation == 4:
                print('删除')
            if user_operation == 5:
                sys.exit('程序退出')
        else:
            print('\033[31;1m请输入有效操作编号\033[0m')
def user_enquiries():
    '''定义一个用户查询的函数'''
    user_information()
    enquirie_name = input('请输入要查询的员工姓名（例如：Alex）：')
    if enquirie_name.capitalize() in user_dict:     #将输入的员工姓名首字母变大写，方便用户输入
        print('\033[32;1m%s\033[0m 工资为: \033[32;1m%s\033[0m元'
              %(enquirie_name.capitalize(),user_dict[enquirie_name.capitalize()]))
    else:
        print('\033[31;1m该用户不存在\033[0m')
def salary_change():
    '''定义一个修改工资函数'''
    user_information()
    change_salary = input('请输入要修改的员工姓名和工资，用空格分隔（例如：Alex 10）：')
    salary_lists = change_salary.split()   #将用户输入的姓名和工资以列表形式打印
    if len(salary_lists) < 2:               #判断输入内容格式是否正确 姓名 工资
        print('\033[31;1m请输入正确格式内容\033[0m')
    elif not salary_lists[1].isdigit():     #判断输入的工资是否是数字
        print('\033[31;1m请输入有效工资金额\033[0m')
    else:
        _name = salary_lists[0].capitalize()        #定义_name变量存储 用户输入的姓名
        _salary = salary_lists[1]                   #定义_salary变量存储 用户输入的工资
        if _name in user_dict:
            print('已将 \033[32;1m%s\033[0m 的工资修改为 \033[32;1m%s\033[0m元'%(_name,_salary))
        else:
            print('\033[31;1m该用户不存在\033[0m')
def add_users():
    '''定义一个增加员工函数'''
    user_information()
    add_user = input('请输入要增加员工姓名和工资，用空格分隔（例如：Eric 100000）：')
    add_lists = add_user.split()
    if len(add_lists) < 2:               #判断输入内容格式是否正确 姓名 工资
        print('\033[31;1m请输入正确格式内容\033[0m')
    elif not add_lists[1].isdigit():     #判断输入的工资是否是数字
        print('\033[31;1m请输入有效工资金额\033[0m')
    else:
        _name = add_lists[0].capitalize()  # 定义_name变量存储 用户输入的姓名
        _salary = add_lists[1]  # 定义_salary变量存储 用户输入的工资
        if _name in user_dict:  #判断输入的姓名是否已存在
            print('\033[31;1m该用户已存在\033[0m')
        elif not _name.isalpha():       #判断输入的姓名是否是纯英文
            print('\033[31;1m请输入正确姓名\033[0m')
        else:
            with open('info','a') as f:
                f.write(_name+' ')
                f.write(_salary+'\n')
            print('已将 \033[32;1m%s\033[0m 的信息添加成功' % _name)




user_operations()


