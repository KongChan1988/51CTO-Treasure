# -*- coding:utf-8 -*-
# Author:D.Gray
import logging
class Logger(object):
    def __init__(self,name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        #定义日志输出到文件
        fh = logging.FileHandler(name)
        fh.setLevel(logging.ERROR)
        fh.setFormatter(self.fmt)
        #定义日志输出到控制台
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)
        sh.setFormatter(self.fmt)
        #给logger添加handler
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self,mesg):
        '''
        定义debug级别的日志
        :param mesg:
        :return:
        '''
        self.logger.debug(mesg)
    def info(self,mesg):
        self.logger.info(mesg)
    def warning(self,mesg):
        self.logger.warning(mesg)
    def error(self,mesg):
        self.logger.error(mesg)
    def critical(self,mesg):
        self.logger.critical(mesg)

if __name__ == '__main__':
    logger = Logger("logging.log")      #实例化Logger类
    logger.debug("debug message!")      #调用日志级别函数并传参
    logger.info("info message!")
    logger.warning("warning message!")
    logger.error("error message!")
    logger.critical("critical message!")
