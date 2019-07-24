#-*- Coding:utf-8 -*-
# Author: D.Gray
import os,sys,socket
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

#IP和端口信息
IP_PORT = ("192.168.72.128",6969)

#用户数据文件
USER_FILE = os.path.join(BASE_DIR,'db\\user_info')
#用户文件目录
USER_HOME = BASE_DIR