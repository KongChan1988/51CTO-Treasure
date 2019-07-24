# -*- coding:utf-8 -*-
# Author:D.Gray
import logging
import os
import time
from AutoRunFrame.config.Settings import log_path

class Logger(object):
    def __init__(self,logger_name,CmdLevel,FileLevel):
        '''

        :param logger_name:
        :param CmdLevel: 控制台日志级别
        :param FileLevel: 文件日志级别
        '''
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)
        self.fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        #定义日志文件名并保存到指定Report/Log路径下
        self.LogFileName = os.path.join(log_path,"{0}.log".format(time.strftime("%Y-%m-%d")))

        #定义控制台日志
        sh = logging.StreamHandler()
        sh.setFormatter(self.fmt)
        sh.setLevel(CmdLevel)

        #文件日志
        fh = logging.FileHandler(self.LogFileName,encoding="utf-8")
        fh.setFormatter(self.fmt)
        fh.setLevel(FileLevel)

        #将logger添加Handler
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)

    def debug(self, mesg):
        '''
        定义debug级别的日志
        :param mesg:
        :return:
        '''
        self.logger.debug(mesg)

    def info(self, mesg):
        self.logger.info(mesg)

    def warning(self, mesg):
        self.logger.warning(mesg)

    def error(self, mesg):
        self.logger.error(mesg)

    def critical(self, mesg):
        self.logger.critical(mesg)

# if __name__ == '__main__':
#     logger = Logger("FOX",CmdLevel=logging.DEBUG,FileLevel=logging.ERROR)
#     logger.debug("debug message!")  # 调用日志级别函数并传参
#     logger.info("info message!")
#     logger.warning("warning message!")
#     logger.error("error message!")
#     logger.critical("critical message!")
