# -*- coding:utf-8 -*-
# Author:D.Gray
from selenium import webdriver
from AutoRunFrame.Public.pages.BasePage import BasePage
from AutoRunFrame.Public.common.DoExcel import ReadExcel
from AutoRunFrame.Public.common.ReadConfigIni import ReadConfigIni
import unittest,time,os
class Search(BasePage):
    Search = ("xpath","//input[@id='kw']")
    SearchBtn = ("xpath","//input[@id='su']")

    def Search_Value(self,SearchValue):
        '''
        1、调用BasePage类中findElement()方法 来定位元素
        2、然后在将findElement()方法Return值 self.driver.find_elements_by_link_text(value) 通过type()方法进行send_keys
        :param SearchValue: 接收TextCae传来的文本内容 即send_keys("xxx")
        :return:
        '''
        search = self.findElement(self.Search)
        self.type(search,SearchValue)

        #通过点击按钮进行搜索
        time.sleep(3)
        btn =self.findElement(self.SearchBtn)
        self.click(btn)
        #退出
        time.sleep(3)
        self.quit()

        # # 通过回车进行搜索
        # time.sleep(3)
        # self.enter(search)
        # time.sleep(3)

# if __name__ == '__main__':
#     test = Search()
#     ini_path = "E:\\python_work\\51CTO_Python\Selenium自动化\AutoRunFrame\Public\common\config.ini"
#     exc_path = "E:\\python_work\\51CTO_Python\Selenium自动化\AutoRunFrame\Public\common\Demo.xls"
#     value  = ReadExcel(exc_path,"你好").read(3,1)  #从Excel中获取搜索内容
#     url = ReadConfigIni(ini_path).ReadConfig("url","Baidu_url")     #从INI配置文件中获取URL
#     print(url,value)
#     test.open(url)
#     test.Search_Value(value)


