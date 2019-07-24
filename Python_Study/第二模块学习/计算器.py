#-*- Coding:utf-8 -*-
# Author: D.Gray
import re,sys
'''
要求：
1\实现加减乘除及拓号优先级解析
2\用户输入
1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
等类似公式后，必须自己解析里面的(),+,-,*,/符号和公式(不能调用eval等类似功能偷懒实现)，
运算后得出结果，结果必须与真实的计算器所得出的结果一致
'''
def compute_mul_div(mg):
    '''
    定义一个乘除函数
    :param mg:
    :return:
    '''
    num = mg[0]  #  -40/5
    match = re.search("\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*",num)
    if not match:
        return
    content = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',num).group()
    if len(content.split('*')) > 1:
        v1,v2 = content.split('*')
        value = float(v1) * float(v2)
        # print('v1>>>%s and v2>>>%s'%(str(v1),str(v2)))
        # print('computer_mul:%s and %s'% (str(content),str(value)))
    else:
        v1, v2 = content.split('/')
        value = float(v1) / float(v2)
        # print('v1>>>%s and v2>>>%s' % (str(v1), str(v2)))
        # print('computer_del:%s and %s' % (str(content),str(value)))
    pur,suf = re.split('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',num,1)
    new_str = '%s%s%s'%(pur,value,suf)
    mg[0] = new_str
    #print('pur>>>%s    value>>>%s     uer>>>%s   new_str>>>%s' % (pur, value,suf,new_str))
    compute_mul_div(mg)

def compute_add_sub(mg):
    '''
    运算表达式加减函数
    :param mg:
    :return:
    '''
    while True:
        if mg[0].__contains__('+-') or mg[0].__contains__('++') or mg[0].__contains__('-+') or mg[0].__contains__('--'):
            mg[0] = mg[0].replace('+-', '-')  # 将-替换掉+-
            mg[0] = mg[0].replace('++', '+')  # 将+替换掉++
            mg[0] = mg[0].replace('-+', '-')  # 将-替换掉-+
            mg[0] = mg[0].replace('--', '+')  # 将+替换掉--
        else:
            break
    if mg[0].startswith('-'):  # 如果arg的第0个元素是以-开头
        mg[1] += 1  # arg的第一个元素自加1
        mg[0] = mg[0].replace('-', '&')
        mg[0] = mg[0].replace('+', '-')
        mg[0] = mg[0].replace('&', '+')  # 将-变+，+变-
        mg[0] = mg[0][1:]  # 将arg中第0个元素中前面多出来的符号去掉
    num = mg[0]  # -40/5
    match = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*',num)
    if not match:
        return
    content = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*',num).group()
    if len(content.split('+')) > 1:
        v1, v2 = content.split('+')
        value = float(v1) + float(v2)
        # print('v1>>>%s and v2>>>%s' % (str(v1), str(v2)))
        # print('computer_add:%s and %s' % (str(content),str(value)))
    else:
        v1, v2 = content.split('-')
        value = float(v1) - float(v2)
        # print('v1>>>%s and v2>>>%s' % (str(v1), str(v2)))
        # print('computer_sub:%s and %s' % (str(content),str(value)))
    pur,suf = re.split('\d+\.*\d*[\+\-]{1}\d+\.*\d*',num,1)
    new_str = '%s%s%s'%(pur,value,suf)
    mg[0] = new_str
    compute_add_sub(mg)

def calate(match_group):
    '''
    计算表达式函数
    :param match_group:
    :return:
    '''
    mg = [match_group.strip('()'),0]   # mg = ['-40/5']
    compute_mul_div(mg)     #调用乘除运算函数
    compute_add_sub(mg)     #调用加减运算函数
    if divmod(mg[1],2)[1] == 1:
        result = float(mg[0])
        result *= -1
        #print('divmod_result:%s'%result)
    else:
        result = float(mg[0])
    #print('in the calator-new_str():%s'%mg)
    return result

def kuohao(calculate):
    '''
    取出表达式中括号函数
    :param calculate:
    :return:
    '''
    while True:
        match = re.search('\([^()]+\)',calculate)   #使用正则表达式 取出优先级最高的括号 并计算
        if match:   #如果表达式中有括号
            match_group = match.group() #
            match_result = calate(match_group)  #调用计算函数
            calculate = calculate.replace(match_group,str(match_result)) #将括号计算后的结果替换原参数
        else:   #若表达式中没有括号
            calate(calculate)
            break
    return calate(calculate)

print('\033[33m 欢迎使用计算器 ：\033[0m'.center(50,'-'))
print('例：1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))')
while True:
    calculate_input = input('\033[32m请输入计算的表达式 | (退出:q)>>>\033[0m')
    calculate_input = re.sub('\s*','',calculate_input)
    if calculate_input == 'q':
        exit('程序退出')
    if len(calculate_input) == 0:
        continue
    if re.search('[^\d\+\-\*/\(\)]',calculate_input):   #使用正则表达式判断用户输入是否是数字、"+-*/"、"()"
        print('\033[31m 输入错误，请重新输入!!!\033[0m')
    else:
        result = kuohao(calculate_input)    #调用去除括号的函数
        print('\033[34m 计算结果>>>%s\033[0m'%result)
        print('\033[35m 正确结果>>>%s\033[0m' % eval(calculate_input))


