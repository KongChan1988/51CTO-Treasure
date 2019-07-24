# -*- coding:utf-8 -*-
# Author:D.Gray
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("file:///E:/Selenium_version/SeleniumDemo/%E8%A2%AB%E6%B5%8Bdemo/checkbox.html")
#方法一：
list = driver.find_elements_by_tag_name("fruit")
for item in list:
    if item.get_attribute("type") =="checkbox":        #循环获取没个item的type属性值
        item.click()
        sleep(1)
driver.quit()

# #方法二：
list = driver.find_elements_by_tag_name("fruit")
for item in list:
        item.click()
driver.quit()
