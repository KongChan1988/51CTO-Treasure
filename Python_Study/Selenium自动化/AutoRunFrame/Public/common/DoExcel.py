# -*- coding:utf-8 -*-
# Author:D.Gray
import xlrd
import os,json
from AutoRunFrame.config.Settings import Test_Data_path

class ReadExcel(object):
    '''
    打开Excel并读取Excel
    获取数据驱动测试
    '''
    def __init__(self,excel_name,sheetname):
        '''

        :param excel_name: 获取Excel名
        :param sheetname: 获取Excel中的sheet名
        '''
        path = os.path.join(Test_Data_path,excel_name)
        self.wordexcel = xlrd.open_workbook(path)
        self.sheet = self.wordexcel.sheet_by_name(sheetname)

    def read(self,RowNum,ColNum):
        '''
        根据收到的传参（行数，列数）获取Excel中数据并返回
        :param RowNum: 行数
        :param ColNum: 列数
        :return:
        '''
        value = self.sheet.cell(RowNum,ColNum).value
        return value

# if __name__ == '__main__':
#     read_excel = ReadExcel("Demo.xls","你好")
#     value = read_excel.read(3,1)
#     print(value)

