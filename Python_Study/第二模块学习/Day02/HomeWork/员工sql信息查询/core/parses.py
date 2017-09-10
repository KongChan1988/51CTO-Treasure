#-*- Coding:utf-8 -*-
# Author: D.Gray
import os,sys

def parse():
    '''
    定义用户输入的sql并统一格式化后分配到各个sql解析模块
    :param user_sql:
    :return:
    '''
    while True:
        user_sql = input('请输入查询sql语句>>>:').strip()
        if len(user_sql) == 0:
            print("\033[31;1m输入不能为空\033[0m")
            continue
        elif user_sql == 'exit':
            exit('退出程序')
        else:
            sql_list = user_sql.split(' ')  #将用户输入的sql语句转换成列表格式
            func = sql_list[0]
            parse_dic = {
                'select':select_parse,
                'update':update_parse,
                'delect':delect_parse,
                'insert':insert_parse
            }
            par_res = ''
            if func in parse_dic.keys():    #根据用户输入的sql关键字，分配到相应函数中进行解析
                par_res = parse_dic[func](sql_list) #将parse_dic[func](func)中的(sql_list)作为位置参数传给select_parse()
                                #select_parse()有定义个形参，所以parse_dic[func]()后要定义一个位置参数给select_parse()
            else:
                print("\033[31;1m输入语句错误错误\033[0m")
    return par_res                      #定义一个函数返回值，传给相应的解析函数

def select_parse(par_res):
    '''
    定义select_parse函数，接受用户输入的查询sql语句（parse()函数传递过来的返回值 res=parse_dic[func](sql_list)）
    并返回参数给hand_parse(res,sql_dic)函数进行sql解析
    :param sql:
    :return:
    '''
    sql_dic = {
        #'res':select,
        'select':[],
        'from':[],
        'where':[],
        'limit':[]
    }
    print('in the select_parse-parse_res:',par_res)
    return hand_parse(par_res,sql_dic)


def insert_parse(res):
    '''
    定义main_sql函数，接受用户输入的查询sql语句并进行sql解析
    :param sql:
    :return:
    '''
    sql_dic = {
        # 'res':slect,
        'insert': [],
        'from': [],
        'where': [],
        'limit': []
    }
    print('in the insert_parse:', res)
    return hand_parse(res, sql_dic)


def update_parse(res):
    '''
    定义main_sql函数，接受用户输入的查询sql语句并进行sql解析
    :param sql:
    :return:
    '''
    print('in the select_parse:',res)

def delect_parse(res):
    '''
    定义main_sql函数，接受用户输入的查询sql语句并进行sql解析
    :param sql:
    :return:
    '''
    print('in the select_parse:',res)


def hand_parse(par_res,sql_dic):
    '''
    该函数把接受过来的函数进行格式化解析操作，并将整合后的sql字典作为返回值传参给  sql_action（）语句主执行函数
    :param sql_list:
    :param sql_dic:
    :return:
    '''
    for item in par_res:        #循环遍历select_parse()函数传过来的：用户输入的sql语句
        if item in sql_dic:     #判断语句中的关键字是否在相应函数sql_dic字典中
            key = item
        else:
            sql_dic[key].append(item)   #将字典转化为 select:[*]  from:[db.emp] 格式
    print('in the hand_parse:',sql_dic)

    if sql_dic.get('where'):        #整理并格式化where[id < 10...]字段内容
        res_list = []
        key = ['and','or','not']
        char = ''
        for item in sql_dic.get('where'):
            if len(item) == 0:
                continue
            if item in key:
                if len(char) != 0:
                    for item_char in char:

                    #char = where_parse(char)
                    res_list.append(char)
                    res_list.append(item)
                    char = ''
            else:
                char += item
        else:
            #char = where_parse(char)
            res_list.append(char),
    sql_dic['where'] = res_list         #将where列表内容整理成 where['id > 10','and','id < 20']的格式
    print('where字段列表元素:',sql_dic['where'],sql_dic)
    return        #将where['id > 10','and','id < 20']的列表格式作为返回值,传参给where_parse()函数进行最终整理

def where_parse(where_char):
    key = ['<','>','=']
    res_list = []
    opt = ''
    char = ''
    for item in where_char:
        print('in the where_parse-where_char:',where_char,item)
        if len(item) == 0:
            continue
        if item in key:
            if len(char) != 0:
                opt += item
                res_list.append(char)
                res_list.append(opt)
                char = ''
                opt = ''
        else:
            char += item
    else:
        res_list.append(char)
        res_list.append(opt)
    print('in the where_parse:',res_list)


