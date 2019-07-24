# -*- coding:utf-8 -*-
# Author:D.Gray
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    '''
    BasePage封装了所有页面的公共方法，比如Driver、find_element等
    '''
    #实例化BasePage类时，让其最先执行__init__方法，该方法参数就是BasePage的入参
    #__init__方法不能有返回值
    def __init__(self,selenium_driver,base_url):
        self.driver = selenium_driver
        self.base_url  = base_url

    def on_page(self,page_title):
        '''
        获取页面title值方法
        :param page_title:
        :return:
        '''
        return page_title in self.driver.title  #把获取到页面的title值返回给 page_title

    def _open(self,url):
        '''
        获取页面url和将浏览器最大化方法
        :param url:
        :return:
        '''
        self.driver.get(url)            #获取页面URL
        self.driver.maximize_window()  #浏览器打开最大化

    def open(self):
        '''
        打开url地址 获取title
        :return:
        '''
        self._open(self.base_url,self.page_title)

    def find_element(self,*loc):
        '''
        定义一个等待并定位元素方法
        *loc  任意数量的位置参数
        :param loc:
        :return:
        '''
        try:
            WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print("%s 页面未能识别到 %s 元素"%(self,loc))

    def script(self,src):
        '''
        定义一个js操作方法
        :param src:
        :return:
        '''
        self.driver.excute_script(src)

    def send_keys(self,loc,value,clear_first=True,click_first=True):
        '''
        首先检查*loc是否为空，如果为空则先清空在重新赋值
        :param loc:
        :param value:
        :param clear_first:
        :param click_first:
        :return:
        '''
        try:
            loc = getattr(self,"%s"%loc)     #getattr相当于实现了self.loc
            if click_first:
                self.find_element(*loc).click()     #点击按钮能不点 能点的就先点进去
            if clear_first:
                self.find_element(*loc).clear()     #查看输入框中是否有默认值，如有默认值就先清空
                self.find_element(*loc).send_keys(value)    #重新赋值
        except AttributeError:
            print("%s 页面未能识别到 %s 元素" % (self, loc))
