# -*- coding:utf-8 -*-
# Author:D.Gray
import logging
#创建logger
logger = logging.getLogger("fox")
log_file = "test.log"
#设置默认log级别
logger.setLevel(logging.DEBUG)

#借助FileHandler（）将日志输出到日志文件中
fh = logging.FileHandler(log_file)
fh.setLevel(logging.ERROR)
#借助StreamHandler()创建一个Handler，将日志输出到控制台上
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

#定义输出handler格式
fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

#配置logger
fh.setFormatter(fmt)
ch.setFormatter(fmt)
#给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)

#应用日志
logger.debug("debug message!")
logger.info("info message!")
logger.warning("warning message!")
logger.error("error message!")
logger.critical("critical message!")



#将日志输出到文件中
# logging.basicConfig(filename="log.log",level=logging.INFO)
# logging.debug("debug message!")
# logging.info("info message!")
# logging.warning("warning message!")
# logging.error("error message!")
# logging.critical("critical message!")

#logger记录器
# logger = logging.getLogger("Demo")
# logger.debug("debug message!")
# logger.info("info message!")
# logger.warning("warning message!")
# logger.error("error message!")
# logger.critical("critical message!")
#
# FORMAT = logging.Formatter(fmt=None,)