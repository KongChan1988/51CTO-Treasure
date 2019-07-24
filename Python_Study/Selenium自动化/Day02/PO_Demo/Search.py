# -*- coding:utf-8 -*-
# Author:D.Gray
from selenium.webdriver.common.by import By
from Base_Page import BasePage
from selenium import webdriver

class SearchPage(BasePage):
    '''
    此类继承BasePage
    '''
    #定位元素
    search_loc = (By.ID,"kw")       #定义输入框元素
    btn_loc = (By.ID,"su")          #定义搜索按钮元素

    def open(self):
        '''
        由于继承了BasePage类 我们可以直接重写其中的元素
        :return:
        '''
        self._open(self.base_url)

    def search_content(self,content):
        '''
        定义一个文本输入函数
        content:估计是接收Test_Case用例参数值
        :param content:
        :return:
        '''
        Baicontent = self.find_element(*self.search_loc)   #将self.search_loc值传给BasePage中find_element()函数
        Baicontent.send_keys(content)

    def btn_click(self):
        Baibtn = self.find_element(*self.btn_loc)
        Baibtn.click()