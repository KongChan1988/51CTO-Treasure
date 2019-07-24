# -*- coding:utf-8 -*-
# Author:D.Gray
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BasePage(object):
    '''
    封装所有页面的公共方法
    '''
    def __init__(self):
        try:
            self.driver = webdriver.Firefox()
        except Exception:
            raise NameError("Not FireFox!!")    #raise抛出异常 未找到火狐

    def open(self,url):
        '''
        打开访问地址
        :param url:
        :return:
        '''
        if url  != "":
            self.driver.get(url)
        else:
            raise ValueError("Please import URL!!")  #抛出异常 请输入正确URL

    def findElement(self,element):
        '''
        解析定位单个元素函数
        :param element: 定义find_element_by_XXX(type=value)
        :return:
        '''
        try:
            type = element[0]
            value = element[1]
            if type == "id" or type == "ID" or type == "Id":
                elem = self.driver.find_element_by_id(value)
            elif type == "name" or type == "Name" or type == "NAME":
                elem = self.driver.find_element_by_name(value)
            elif type == "class" or type == "Class" or type == "CLASS":
                elem = self.driver.find_element_by_class_name(value)
            elif type == "xpath" or type == "Xpatch" or type == "XPATCH":
                elem = self.driver.find_element_by_xpath(value)
            elif type == "link_text" or type == "Link_text" or type == "LINK_TEXT":
                elem = self.driver.find_element_by_link_text(value)
            else:
                raise NameError("请输入有效type")
        except NameError:
            raise ("NO TYPE")
        return elem

    def findElements(self,element):
        '''
        解析定位单个元素函数
        :param type: 定义find_element_by_XXX(type=value) 中元素属性id或name或class....
        :param value: 定义find_element_by_XXX(type=value)中元素属性值  type='kw',type='su'
        :return:
        '''
        try:
            type = element[0]
            value = element[1]
            if type == "id" or type == "ID" or type == "Id":
                elem = self.driver.find_elements_by_id(value)
            elif type == "name" or type == "Name" or type == "NAME":
                elem = self.driver.find_elements_by_name(value)
            elif type == "class" or type == "Class" or type == "CLASS":
                elem = self.driver.find_elements_by_class_name(value)
            elif type == "xpath" or type == "Xpatch" or type == "XPATCH":
                elem = self.driver.find_elements_by_xpath(value)
            elif type == "link_text" or type == "Link_text" or type == "LINK_TEXT":
                elem = self.driver.find_elements_by_link_text(value)
            else:
                raise NameError("请输入有效type")
        except NameError:
            raise ("NO TYPE")
        return elem

    def type(self,element,text):
        '''
        driver.find_element_by_link_text(value).send_keys()操作函数
        :param element:
        :param text:
        :return:
        '''
        element.send_keys(text)

    def click(self,element):
        '''
        driver.find_element_by_link_text(value).click()操作
        :param element:
        :return:
        '''
        element.click()

    def enter(self,element):
        element.send_keys(Keys.RETURN)   #发送回车

    def quit(self):
        self.driver.quit()

    def getAttrbute(self,element,attribute):
        '''
        接受获取属性值的函数
        :param element:
        :param attribute: 接收用户想要获取属性参数
        :return:
        '''
        return element.get_attributed(attribute)

    def display(self,x,y):
        '''

        :param x: x轴移动多少
        :param y: y轴移动多少
        :return:
        '''
        js = "window.scrollTo(%s,%s)"%(x,y)
        self.driver.execute_script(js)