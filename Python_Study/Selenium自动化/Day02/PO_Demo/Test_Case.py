# -*- coding:utf-8 -*-
# Author:D.Gray
import unittest
from Search import SearchPage
from time import sleep
from selenium import webdriver

class TestRun(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        sleep(2)
        self.driver.implicitly_wait(30)     #隐式等待
        self.url = "https://www.baidu.com"
        self.content = "Bela"

    def test_search(self):
        '''
        实例化SearchPage
        :return:
        '''
        baidu_page = SearchPage(self.driver,self.url)  #将self.url传参给 SearchPage()类
        baidu_page.open()       #在调用SearchPage类中 open()方法
        baidu_page.search_content(self.content) #将"Bela"传参给SearchPage()类中 search_content()方法
        baidu_page.btn_click()  #然后在调用btn_click()函数
        sleep(5)

    def testDown(self):
        '''
        该函数是用例执行后重置测试环境用
        :return:
        '''
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()     #运行