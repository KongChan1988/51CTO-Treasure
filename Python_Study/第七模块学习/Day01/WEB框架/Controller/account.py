#-*-coding:utf-8 -*-
# Author: D.Gray
def handle_index():
    f = open("E:\Python_Pycharm_work\第七模块学习\Day01\WEB框架\View\s1.html",mode="rb")
    data = f.read()
    # print(data)
    f.close()
    return [data,]

def handle_date():
    return ['<h1>Hello Date</h1>'.encode('utf-8'), ]

handle_index()