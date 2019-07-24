# -*- coding:utf-8 -*-
# Author:D.Gray
from datetime import datetime
def baseUrl():
    url = "https://www.baidu.com"
    return url

def getCurrentTime():
    '''
    定义一个获取当前时间函数
    :return:
    '''
    format = "%a %b %d %H:%M:%S %Y"       #x日x月 x时x分x秒 xxxx年
    return datetime.now().strftime(format)

def timeDiff(starttime,endtime):
    '''
    定义一个持续时间函数
    :param starttime:
    :param endtime:
    :return:
    '''
    format = "%a %b %d %H:%M:%S %Y"  # x日x月 x时x分x秒 xxxx年
    return datetime.strftime(endtime,format) - datetime.strftime(starttime,format)

print(getCurrentTime())
