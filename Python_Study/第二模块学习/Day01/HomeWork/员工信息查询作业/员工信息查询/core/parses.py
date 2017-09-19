#-*- Coding:utf-8 -*-
# Author: D.Gray
import os,sys
from core import action
def parse(user_sql,func,sql_list):
    '''
    定义用户输入的sql并统一格式化后分配到各个sql解析模块
    :param user_sql:用户输入的sql语句
    :return:
    '''
    parse_dic = {
        'select':select_parse,
        'update':update_parse,
        'delect':delect_parse,
        'insert':insert_parse
    }
    par_res = ''
    if func in parse_dic.keys():    #根据用户输入的sql关键字，分配到相应函数中进行解析
        par_res = parse_dic[func](sql_list) #将parse_dic[func](sql_list)中的(sql_list)作为位置参数传给select_parse()
                        #select_parse()有定义个形参，所以parse_dic[func]()后要定义一个位置参数给select_parse()
    return par_res                      #定义一个函数返回值，传给相应的解析函数

def select_parse(par_res):
    '''
    定义select_parse函数，接受用户输入的查询sql语句（parse()函数传递过来的返回值 res=parse_dic[func](sql_list)）
    并返回参数给hand_parse(res,sql_dic)函数进行sql解析
    :param sql:
    :return:
    '''
    sql_dic = {
        'par_res': action.select_action,
        'select':[],
        'from':[],
        'where':[],
        'limit':[]
    }
    #print('in the select_parse-parse_res:',par_res,sql_dic)
    return hand_parse(par_res,sql_dic)


def insert_parse(par_res):
    '''
    定义insert_parse函数，接受用户输入的查询sql语句并进行sql解析
    :param sql:
    :return:
    '''
    sql_dic = {
        'par_res': action.insert_action,
        'insert': [],
        'value': [],
        'into':[]
    }
    print('in the insert_parse:', par_res)
    return hand_parse(par_res, sql_dic)


def update_parse(par_res):
    '''
    定义update_parse函数，接受用户输入的查询sql语句并进行sql解析
    :param sql:
    :return:
    '''
    sql_dic = {
        'par_res': action.update_action,
        'update': [],
        'set': [],
        'where': [],
    }
    #print('in the update_parse:',par_res)
    return hand_parse(par_res, sql_dic)

def delect_parse(par_res):
    '''
    定义delect_parse函数，接受用户输入的查询sql语句并进行sql解析
    :param sql:
    :return:
    '''
    sql_dic = {
        'par_res':action.delect_action,
        'delect': [],
        'from': [],
        'where':[]
    }
    #print('in the delect_parse:',par_res)
    return hand_parse(par_res, sql_dic)

def hand_parse(par_res,sql_dic):
    '''
    该函数把接受过来的函数进行格式化解析操作，并将整合后的sql字典作为返回值传参给  sql_action（）语句主执行函数
    :param sql_list:
    :param sql_dic:各sql模块所对应的sql语句结构字典
    :return:
    '''
    for item in par_res:        #循环遍历select_parse()函数传过来的：用户输入的sql语句
        if item in sql_dic:     #判断语句中的关键字是否在相应函数sql_dic字典中
            key = item
        else:
            sql_dic[key].append(item)   #将字典转化为 select:[*]  from:[db.emp] 格式
    #print('in the hand_parse:',sql_dic)

    if sql_dic.get('where'):        #整理并格式化where[id < 10...]字段内容
        res_list = []
        key = ['and','or','not']
        char = ''
        for item in sql_dic.get('where'):
            if len(item) == 0:
                continue
            if item in key:
                if len(char) != 0:
                    char = where_parse(char)  #将char最为实参传参给where_parse()函数。例：char = 'id ','>','10'
                    res_list.append(char)
                    res_list.append(item)
                    char = ''
            else:
                char += item
        else:
            char = where_parse(char)    ##将char最为实参传参给where_parse()函数。例：char = 'id ','>','10'
            res_list.append(char),
        sql_dic['where'] = res_list         #将where列表内容整理成 where['id > 10','and','id < 20']的格式
        #print('where字段列表元素:',sql_dic['where'],sql_dic)
    return  action.sql_action(sql_dic)     #将where['id > 10','and','id < 20']的列表格式作为返回值,
                                            # 传参给where_parse()函数进行最终整理

def where_parse(where_char):
    '''
    该函数接收hand_parse()传递过来的char参数，并把这些参数整理成['id ','>','10']这样的格式,并返回一个where_res_list值
    :param where_char: where_parse(where_char)函数中where_char形参接收的是hand_parse()传递过来的char参数
    :return: 把整理完毕的参数格式作为一个 where_res_list列表 的返回值
    '''
    key = ['<','>','=']
    where_res_list = []
    opt = ''
    char = ''
    tag = False
    for item in where_char: #循环遍历where_char字符串，如: 'id > 10'
        if len(item) == 0:
            continue
        if item in key:
            tag = True      #将tag状态变为True
            if len(char) != 0 :
                where_res_list.append(char)
                char = ''
            opt += item
        if not tag:         #判断tag状态是否是False
            char += item
        if tag and item not in key:     #判断tag状态为False并且不在key列表中
            tag = False                 #将tag状态变为False
            where_res_list.append(opt)
            opt = ''
            char += item
    else:
        where_res_list.append(char)

    if len(where_res_list) == 1 : # 将列表中'namelikealex'字符串内容转换成['name','like','alex']格式
        where_res_list = where_res_list[0].split('like')
        where_res_list.insert(1,'like')
    #print('in the where_parse:', where_res_list)
    return where_res_list




