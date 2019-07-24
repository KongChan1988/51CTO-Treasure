#-*-coding:utf-8 -*-
# Author: D.Gray
import sqlalchemy
import os,sys
BASE_DESC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(BASE_DESC)
sys.path.append(BASE_DESC)


CONN = 'mysql+pymysql://root:admin1988@localhost/machine?charset=utf8'


