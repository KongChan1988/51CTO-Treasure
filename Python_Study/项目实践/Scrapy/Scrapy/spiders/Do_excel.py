# -*- coding:utf-8 -*-
# Author:D.Gray
import xlwt
stus = [["性名","年龄","性别","分数"],["mary",20,"女",89],["mary",20,"女",89],["mary",20,"女",89]]
wbk = xlwt.Workbook()               #创建Excel文件
sheet = wbk.add_sheet("food_sheet")     #创建Excel中Sheet页
row = 0
for stu in stus:
    # print(stu)
    col = 0
    for item in stu:
        # print(item)
        sheet.write(row,col,item)       #将数据写入
        col += 1
    row += 1
wbk.save('stu_1.xls')   #将文件名str_1保存Excel

