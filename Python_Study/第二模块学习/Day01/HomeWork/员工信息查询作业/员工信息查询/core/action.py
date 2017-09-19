#-*- Coding:utf-8 -*-
# Author: D.Gray
import os,sys,re

#语句主分配模块
def sql_action(sql_dic):
    '''
    该函数接收hand_parse()传过来的整理完毕后的字典sql_dic,并根据字典中 par_res键分配调用相应的语句执行模块函数
    :return:
    '''
    return sql_dic.get('par_res')(sql_dic)  #根据字典中 par_res为键 将sql_dic做为参数分配调用相应的语句执行模块函数

#select查询语句执行模块
def select_action(sql_dic):
    '''
    该函数通过sql_action主语句执行函数传来的参数‘sql_dic字典’进行语句执行操作
    :param sql_dic: sql_action主语句执行函数传来的参数
    :return:
    '''
    #优先处理最高from部分
    if len(sql_dic.get('from')) == 0:
        print('\033[31;1mfrom字段不能为空\033[0m')
    else:
        db,table = sql_dic.get('from')[0].split('.') #将{from:['db.emp'}中['db.emp']拆分成 table = emp  db = db
        db_pash = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r'/%s/%s'%(db,table)
        with open(db_pash,'r',encoding='utf-8')as fh:

    #其次处理where部分
            where_res = where_action(fh,sql_dic.get('where'))  #定义where_res变量存储where_action的执行处理结果
    # 再次处理limit部分
            limit_res = limit_action(where_res,sql_dic.get('limit'))
    # 最后处理select部分
            select_res = select(limit_res,sql_dic.get('select'))
            for record in select_res:
                print("查询结果为: \033[34;1m%s\033[0m"% record)
            print('查询结果数量为: \033[34;1m%s\033[0m'%len(record))
            return select_res

def where_action(fh, where_l):
    '''
    该函数将接收过来的db.emp文件变成字典形式，并将该字典与用户输入的where条件进行对比解析，最后将对比结果为True的查询
    条件储存在where_action_res列表中
    :param fh: 接收select_action函数传过来的db.emp文件路径
    :param where_l:接收 select_action函数传过来的sql_dic.get(where')
    :return:
    '''
    where_action_res = []
    title = 'id,name,age,phone,dept,enroll_data'
    if len(where_l) != 0:
        for item in fh:
            db_dic = dict(zip(title.split(','), item.split(',')))
            '''
            定义db_dic函数以字典形式将emp文件中的内容为值，title
            为字典中的键做下拉链拼接。例：db_dic = {
                                                'name':'Mark'
                                                'age':'4'
                                                    ......
                                                    }
            '''
            logice_res = logic_action(where_l,db_dic)  # logice_res  = logic_action_res
            if logice_res:  # 判断logic_action的返回结果是否为True
                where_action_res.append(item.split())  # 将fh和where_l比对后都为True的那条记录添加到where_action_res列表
            else:           # 查询结果都为False，给出提示
                print('正在努力为您查询请稍后...')
    else:
        where_action_res = fh.readlines()
    #print('in the where_action_res: \033[32;1m%s\033[0m'%where_action_res)
    return where_action_res

def logic_action(where_l,db_dic):
    '''
    该函数处理where部分与db.emp文件中的信息进行逻辑分析和对比。并将对比结果为True的信息返回给where_action
    :param where_l:
    :param db_dic:
    :return:
    '''
    logic_action_res = []
    for exp in where_l:
        if type(exp) is list:  # 判断exp是否是列表形式 ['id','>','10']
            exp_k, opt, exp_v = exp  # 将该列表参数赋值成 exp_k=='id'  opt = '>' ,exp_v = '10'
            if exp[1] == '=':
                opt = "%s=" % exp[1]  # 将exp列表中 '=' 变为 '=='
            if db_dic[exp_k].isdigit():  # 判断 db_dic['id'] 是否是数字  如：10
                dic_v = int(db_dic[exp_k])  # 将  db_dic['id']的值变成int类型
                exp_v = int(exp_v)
            else:
                dic_v = '%s' % db_dic[exp_k]  # 将不是数字的例如: 员工姓名 alex,Jim
            if opt != 'like':
                exp = str(eval('%s%s%s' % (dic_v, opt, exp_v)))  # 将emp表中员工db_dic[exp_k]值与exp_v值进行eval字符串比较
            else:
                if exp_v in dic_v:
                    exp = 'True'
                else:
                    exp = 'False'
        logic_action_res.append(exp)  # 将exp  "'True',and,'False'" 字符串变成['True',and,'False']形式
    logic_action_res = eval(' '.join(logic_action_res))  # 先将['True',and,'False']使用join函数变成'Falase'，然后在用
    # eval函数最终将logic_action_res变成False
    #print('in the logic_action_res\033[33;1m%s\033[0m' %logic_action_res)
    return logic_action_res

def limit_action(where_res,limit_l):
    limit_res = []
    if len(limit_l) != 0:
        index = int(limit_l[0])         #定义index变量取 limit_l[0]所对应的值 如 limit['3'] index=3
        limit_res = where_res[0:index]  #将where_res里面的内容进行切片，从0-index
    else:
        limit_res = where_res
    return limit_res

def select(limit_res,select_l):
    '''
    该函数为执行select[name,id]模块查询语句，也是其最终查询结果。如用户输入 select * from db.emp则显示所有字段结果
    若 select name,id,dept from db.emp 则只显示 name,age,dept字段的查询结果
    :param limit_res: limit_res函数过滤后的查询结果
    :param select_l: 用户输入的 select ['name','age','dept']列表信息
    :return:
    '''
    select_list = []
    exp = []
    char = ''
    if len(select_l) != 0:
        if select_l[0] != '*':
            title = 'id,name,age,phone,dept,enroll_data'
            for item in limit_res:

                for index in item:
                    select_dic = dict(zip(title.split(','),index.split(',')))
                    exp = select_l[0].split(',')
                    for i in exp:
                        select_list.append(select_dic[i].strip())
        else:
            select_list = limit_res
    else:
        print('\033[31;1m请输入有效select * 语句\033[0m')
    return exp,select_list

#insert语句执行模块
def insert_action(sql_dic):
    '''
    该函数接收用户输入的insert语句，并分配给指定的insert执行函数进行原文件对比和执行程序
    :param sql_dic:
    :return:
    '''
    #首先处理insert部分
    if len(sql_dic.get('insert')) == 0:
        print('\033[31;1m insert 字段不能为空\033[0m')
    else:
        db,table = sql_dic.get('insert')[0].split('.') #将{from:['db.emp'}中['db.emp']拆分成 table = emp  db = db
        db_pash = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r'/%s/%s'%(db,table)
        with open(db_pash,'r',encoding='utf-8')as fh:
    #其次处理value值
            value_res = value_action(fh,sql_dic.get('value'),db_pash)
    return value_res

def value_action(fh,value_l,db_pash):
    '''
    该函数接收insert_action（）函数传递过来的fh,value_l,db_pash值，并相应变量进行解析整理并执行用户输入的insert语句
    :param fh: 数据库文件
    :param value_l: 用户输入的 value字段参数
    :param db_pash: 数据库文件路径
    :return:
    '''
    phone = []
    for index in value_l:
        index_l = index.split(',')  #遍历用户输入的value值，并将其转换为['5','Mark','32'....]格式
    for item in fh:               #遍历数据库表文件也将其转换为['5','Mark','32'....]格式
        info = item.strip().split(',')
        phone.append(info[3])

    tag = True
    if index_l[2] in phone:   #以手机号作唯一键，判断用户输入的value值是否存在数据文件中
        tag = False
        tag_res = print('\033[31;1m该用户已存在不能重复添加\033[0m')
    if tag and len(index_l) < 5:
        tag = False
        tag_res = print('\033[31;1m用户输入value信息不够\033[0m')
    if tag:
        index_l[0] = int(info[0][-1]) + 1  # 完成id自增：info[0][-1] 取info列表 id的字段最后一个值,然后自动+1
        with open(db_pash,'a',encoding='utf-8') as f:
            f.write(''.join('\n%s,'%index_l[0]+index)) #使用join函数将['6','mark','32'...]拼接字符串成 8,Mark,32的样式
            tag_res = print("已成功添加信息: \033[34;1m%s\033[0m" %index)
    return tag_res,index_l

#update语句执行模块
def update_action(sql_dic):
    #优先处理update字段
    db,table = sql_dic.get('update')[0].split('.') #将{from:['db.emp'}中['db.emp']拆分成 table = emp  db = db
    db_pash = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r'/%s/%s'%(db,table)
    with open(db_pash,'r',encoding='utf-8') as fh:

    #其次处理where部分
        where_res = where_action(fh,sql_dic.get('where'))  # 定义where_res变量存储where_action的执行处理结果
    #最后处理set部分
    set_res = set_action(where_res,sql_dic.get('set'),fh,db_pash)
    print('参数已修改完成: \033[36;1m %s \033[0m' %set_res)
    return set_res

def set_action(where_res,set_l,fh,db_pash):
    '''
    该函数对用户输入的set字段进行处理执行，返回添加结果和修改数据库文本内容
    :param where_res: 接收where_action()函数传递过来的where_res返回值
    :param set_l: 用户输入的 set列表参数
    :param fh:
    :param db_pash:
    :return:
    '''
    set_list = []
    change_list = []
    title = 'id,name,age,phone,dept,enroll_data'
    if len(set_l) == 0 or set_l[0] == 'id':
        print('\033[31;1m用户id不能修改\033[0m')
    else:
        for item in where_res:
            for index in item:   # index参数格式: 1,'Alex',22...
                index_l= index.split(',')   #index_l参数格式：['1','Alex','22'...]
            set_dic = dict(zip(title.split(','),index_l))

            change_list.append(set_dic[set_l[0]])  # 将未修改的字段参数值添加到change_list列表
            change_list.append(set_l[2])  # 将需要修改的参数添加到change_list列表

            set_dic[set_l[0]] = set_l[2]  # 将字典根据用户输入的要修改的字段 如: dept,age 修改成 相应的数值

            set_list = (list(set_dic.values()))    #将重新赋值后的值取出并以列表形式存储,作为修改后的列表
            with open(db_pash, 'r', encoding='utf-8')as fh:
                fh_r = fh.readlines()

            with open(db_pash,'w',encoding='utf-8') as f:
                for line in fh_r:
                    if change_list[0] in line :   #判断未修改的参数值是否存在数据库表中
                            line = line.replace(change_list[0],change_list[1])  #修改文件中所对应的参数值
                    f.write(line)

    #print('in the set_action: \033[36;1m %s \033[0m'%set_list)
    return set_list

#delect语句执行模块
def delect_action(sql_dic):
    '''
    delect主执行函数，对用户输入的delect语句各字段进行分配到相应函数进行解析执行
    :param sql_dic:
    :return:
    '''
    # 优先处理from字段
    if len(sql_dic.get('from')) == 0:
        print('\033[31;1m insert 字段不能为空\033[0m')
    else:
        db, table = sql_dic.get('from')[0].split('.')  # 将{from:['db.emp'}中['db.emp']拆分成 table = emp  db = db
        db_pash = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r'/%s/%s' % (db, table)
        with open(db_pash, 'r', encoding='utf-8')as fh:
    #其次处理where字段
            where_res = where_action(fh,sql_dic.get('where'))  # 定义where_res变量存储where_action的执行处理结果
    #最后处理delect字段
    delect_res = delect(fh,where_res,where_l=sql_dic.get('where'),db_pash=db_pash)
    print('已删除\033[34;1m %s \033[0m员工信息:'%delect_res)
    return delect_res

def delect(fh,where_res,where_l,db_pash):
    '''
    该函数执行用户输入的 where条件参数解析并执行delect操作，并相应文本内容
    :param fh:
    :param where_res:
    :param where_l:
    :param db_pash:
    :return:
    '''
    delect_list = []
    for i in where_res:
        for i in i:
            pass
        if len(where_l) != 0:
            with open(db_pash,'r',encoding='utf-8') as fh:
                lines = fh.readlines()
                for line in lines:
                    if not re.search(i,line): #循环遍历出 不包含 想要删除的文本信息
                        delect_list.append(line)    #并将这些信息存储到字典中
            with open(db_pash,'w',encoding='utf-8') as f:
                f.writelines(delect_list)           #将不包含想要删除的文本信息 写入数据库文本中
        else:
            print('\033[31;1m无删除条件记录\033[0m')
    return where_res

