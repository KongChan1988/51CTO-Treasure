# -*- coding:utf-8 -*-
# Author:D.Gray
import xlrd
'''
将读取Excel操作封装在一个类中
'''
class ReadExcel(object):
    def __init__(self,file_name,sheet_name):
        self.workexcel = xlrd.open_workbook(file_name)
        self.sheetName = self.workexcel.sheet_by_name(sheet_name)   #获取Excel表中sheet名

    def read_excel(self,rowNum,colNum):
        value = self.sheetName.cell(rowNum,colNum).value   #获取sheet页中第X行 X列数据
        return value
Data = ReadExcel("Demo.xls","Sheet1").read_excel(1,1)
print(Data)






'''
读取Excel
'''
# workbook = xlrd.open_workbook("Demo.xls")   #打开Demo.xls
# print(workbook.nsheets)     #打印Excel中的sheets个数
# table = workbook.sheet_by_index(0)   #获取第一个sheet表
# rows = table.nrows  #获取行数
# print("行数:",rows)
# cols = table.ncols  #获取列数
# print("列数:",cols)
#
# #获取某1单元格的内容  方式一
# cell_value = table.cell(1,0).value  #取第1行第0列数据
# print(cell_value)
#
# #获取某1单元格的内容  方式二
# row_data = table.row_values(1)   #获取第1行数据所有内容 以['xxx','xxx',...]列表形式
# cell_data = row_data[2]   #获取第1行[0]个元素  也就是第1行第1个参数
# print("方式2：",cell_data)
# # print(cell_value)


# #将Excel数据循环取出
# workExcel = xlrd.open_workbook("Demo.xls")
# table = workExcel.sheet_by_index(0)
# row_count = table.nrows  #获取行数
# cols_count = table.ncols  #获取列数
# for row in range(0,int(row_count),1):
#     for cols in range(0,int(cols_count),1):
#         cell_value = table.cell(row,cols)
#         print(cell_value)