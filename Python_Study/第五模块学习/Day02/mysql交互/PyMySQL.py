# -*- coding:utf-8 -*-
# Author:D.Gray
import pymysql
conn = pymysql.connect(host = 'localhost',port = 3306,user = 'root',password = 'admin1988',db = 'oldboy')

cursor = conn.cursor()

recount = cursor.execute('select * from student')

print(cursor.fetchall())