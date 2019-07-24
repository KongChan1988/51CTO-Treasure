#-*- Coding:utf-8 -*-
# Author: D.Gray

import logging
#日志级别: debug(最低)----info----warning---error----critical
logging.basicConfig(filename='app.log',level=logging.INFO,                  #将日志打印在文件中
format='%(asctime)s %(levelname)s %(filename)s:%(lineno)d:%(funcName)s %(message)s', #日志打印格式如:日志时间 日志级别名称  日志内容等
                    datefmt='%m/%d/%Y %H:%M:%S')                   #日志打印时间
                                #定义输入日志级别(日志级别必须大写)，输出包含该级别

#logging.basicConfig(format='%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S') #日志打印时间
logging.debug("test debug")
logging.info("test info")
logging.warning("This is warning message")
logging.error("test error")
logging.critical("test critical")

def app_run():
    logging.warning('app has test warning')

app_run()

