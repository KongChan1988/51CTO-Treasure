#-*- Coding:utf-8 -*-
# Author: D.Gray
import time
def logger():
    time_format = '%Y-%m-%d %X'   #定义time日期时间格式  年月日  时分秒
    time_current = time.strftime(time_format)  #函数接受时间元组，并返回
  #可读字符串表示当地时间，格式由format决定
    with open('a','a+') as f:
        f.write('%s end action\n' %time_current)

def test1():
    print('test1 starting action...')
    logger()

def test2():
    print('test2 starting action...')
    logger()

def test3():
    print('test3 starting action...')
    logger()

test1()
test2()
test3()