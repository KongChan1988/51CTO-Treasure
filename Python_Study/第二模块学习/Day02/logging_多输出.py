#-*- Coding:utf-8 -*-
# Author: D.Gray

import logging
# create logger
logger = logging.getLogger('Test_LOG')  #起个日志名
logger.setLevel(logging.DEBUG)  #设置日志最低等级

#建立一个屏幕handler
ch = logging.StreamHandler()  #StreamHandler()---屏幕Handler
ch.setLevel(logging.WARNING)

#建立一个文件handler
fh = logging.FileHandler('access.log',encoding='utf-8') #FileHandler('access.log')----文件Handler
fh.setLevel(logging.ERROR)

#定义各handler的日志输出格式
fh_formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(message)s ',
                                 datefmt='%m/%d/%Y %H:%M:%S')
ch_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s ',
                                 datefmt='%m/%d/%Y %H:%M:%S')

#绑定关联相应的 日志输出格式
ch.setFormatter(ch_formatter)
fh.setFormatter(fh_formatter)

#绑定相应的handler给logger（整个日志的入口）
logger.addHandler(fh)
logger.addHandler(ch)

logger.warning('test_warning')
logger.error('test_error')