# -*- coding:utf-8 -*-
# Author:D.Gray
import unittest,os
from time import strftime
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from time import sleep

class Baidu(unittest.TestCase):
    '''
    定义一个百度搜索类
    '''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.baidu.com"

    def testBaidu_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("//input[@id='kw']").send_keys("Bela")
        driver.find_element_by_xpath("//input[@id='su']").click()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
