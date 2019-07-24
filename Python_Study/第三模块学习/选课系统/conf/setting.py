# -*- coding:utf-8 -*-
# Author:D.Gray
import os,pickle
#数据处理路径
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])
data_path = os.path.join(BASE_DIR,"databases")
#print(data_path)

#数据文件名
school_file = os.path.join(data_path,"school")
#print(school_file)

