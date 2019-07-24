# -*- coding:utf-8 -*-
# Author:D.Gray
import os,sys,socket
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#IP地址和端口
IP_PORT = ("localhost",6969)

#数据文件路径
USER_FILE = BASE_DIR + r"\db\user.db"

#用户文件目录
USER_HOME = BASE_DIR