# -*- coding:utf-8 -*-
# Author:D.Gray
from selenium import webdriver
from time import  sleep
driver = webdriver.Firefox()
driver.get("file:///E:/Selenium_version/SeleniumDemo/%E8%A2%AB%E6%B5%8Bdemo/iframe.html")
driver.switch_to.frame("iname")     #跳到嵌套网页内  id = 'iname'
driver.find_element_by_name("q").send_keys("Bela")
sleep(5)
driver.find_element_by_name("go").click()

print("开始准备跳出去了".center(50,"-"))
driver.switch_to.parent_frame()     #必须先要跳回上一层
sleep(5)
driver.find_element_by_xpath("//a[@class = 'alert-link']").click()
driver.quit()
