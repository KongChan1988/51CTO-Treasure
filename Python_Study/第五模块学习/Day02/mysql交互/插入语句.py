# -*- coding:utf-8 -*-
# Author:D.Gray
import pymysql
conn = pymysql.connect(host = 'localhost',port = 3306,user = 'root',password = 'admin1988',db = 'oldboy')

cursor = conn.cursor()
data = [
    ('Mary',33,'2017-09-28','A'),
    ('kyo',23,'2018-02-28','N'),
]

recont = cursor.executemany('insert into student(name,age,register_date,sex) values(%s,%s,%s,%s)',data)

