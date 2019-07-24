#-*- Coding:utf-8 -*-
# Author: D.Gray
import os
#数据文件的路径
BASE_DIR = '\\'.join(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])
data_path = os.path.join(BASE_DIR,"databases")

#数据文件的名称
school_file = os.path.join(data_path,"school")