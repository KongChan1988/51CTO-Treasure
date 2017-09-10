#-*- Coding:utf-8 -*-
# Author: D.Gray
import os,sys
def spare(user_sql):
    func =user_sql.split(' ')
    print('in the spare-func:',func)
    spare_dic = {
        'select':select_sql,
        'inster':inster_sql,
        'delect':del_sql,
        'update':update_sql
    }
    res = ''
    if func[0] in spare_dic:
        res = spare_dic[func[0]](func)
        print('in user_dic:', func,res)
    return res

def inster_sql(func):
    print('in the inster_sql:',func)

def select_sql(func):
    sql_dic = {
        'func':select,
        'select':[], #查询字段
        'from':[],  #表数据库.表
        'where':[], #过滤条件
        'limit':[], #显示查询数目
    }
    return hand_parse(func,sql_dic)

def del_sql(func):
    pass

def update_sql(func):
    pass

def hand_parse(func,sql_dic):

    tag = False
    for item in func:
        if tag and item in sql_dic:
            tag = False
        if not tag and item in sql_dic:
            tag = True
            key = item
            continue
        if tag:
            sql_dic[key].append(item)

    if sql_dic.get('where'):
        sql_dic['where']=where_parse(sql_dic.get('where'))
    print('in the hand_parse:', sql_dic)
    return sql_dic

def where_parse(where_l):
    res = []
    key = ['and','or','not']
    char = ''
    for i in where_l:
        if len(i) == 0:
            continue
        if i in key:
            if len(char) != 0:
                char = three_parse(char)
                res.append(char)
                res.append(i)
                char = ''
        else:
            char += i
    else:
        char = three_parse(char)
        res.append(char)
    print('in the where_parse res is :', res,where_l)
    return res

def three_parse(exp_str):
    print('in the three_parse-exp_str:', exp_str)
    key = ['<',">",'=']
    res = []
    char = ''
    opt = ''
    tag = False
    for i in exp_str:
        if i in key:
            tag =True
            if len(char) != 0:
                res.append(char)
                char =''
            opt += i
        if not tag:
            char += i
        if tag and i not in key:
            tag = False
            res.append(opt)
            opt = ''
            char += i
    else:
        res.append(char)
    #新增解析like功能
    if len(res) == 1:
        res = res[0].split('like')
        res.insert(1,'like')
    print('in the three_parse res is :', res, exp_str)
    return res


#第二部分
def sql_action(sql_dic):
    return sql_dic.get('func')(sql_dic)

def select(sql_dic):
    print('from select sql_dic is %s' %sql_dic)
    #优先级最高处理from部分
    db,table = sql_dic.get('from')[0].split('.')
    fh = open('%s/%s' %(db,table),'r',encoding='utf-8')

    #其次要处理where部分
    filter_res = where_action(fh,sql_dic.get('where'))
    for record in filter_res:
        print('filter res is \033[32;1m%s\033[0m'%record)

    #处理limit操作
    limit_res = limit_action(filter_res,sql_dic.get('limit'))
    for record in limit_res:
        print('limit_res is \033[32;1m%s\033[0m'%record)
    #最后处理select信息

def where_action(fh,where_l):
    print('in the where_action:\033[33;1m%s\033[0m'% where_l)
    res = []
    logic_l = ['and','or ','not']
    title = 'id,name,age,phone,dept,enroll_data'
    if len(where_l) != 0:
        for line in fh:
            dic = dict(zip(title.split(','),line.split(',')))
            #逻辑判断
            logic_res = logic_action(dic,where_l)
            if logic_res:
                res.append(line.split(','))
    else:
        res = fh.readlines()
    return res

def logic_action(dic,where_l):
    print('from logic_action %s'%dic)
    res = []
    for exp in where_l:
        if type(exp) is list:
            exp_k,opt,exp_v=exp
            if exp[1] == '=':
                opt = '%s='%exp[1]
            if dic[exp_k].isdigit():
                dic_v=int(dic[exp_k])
                exp_v=int(exp_v)
            else:
                dic_v = '%s'%dic[exp_k]
            if opt != 'like':
                exp = str(eval('%s%s%s'%(dic_v,opt,exp_v)))
            else:
                if exp_v in dic_v:
                    exp = 'True'
                else:
                    exp = 'False'
        res.append(exp)
    res = eval(' '.join(res))
    return res

def limit_action(filter_res,limit_l):
    res = []
    if len(limit_l) != 0:
        index = int(limit_l[0])
        res = filter_res[0:index]
    else:
        res = filter_res
    return res








while True:
    user_sql = input('sql>>:').strip()

    if user_sql == 'exit':
        exit('退出程序')
    elif len(user_sql) == 0:
        print('不能为空')

    sql_dic = spare(user_sql)
    print('sql_dic:',sql_dic)
    if len(sql_dic) == 0:
        print('sql关键字输入有误')
        continue
    res = sql_action(sql_dic)
    print('sql_action:',res)