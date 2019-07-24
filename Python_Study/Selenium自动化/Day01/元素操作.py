# -*- coding:utf-8 -*-
# Author:D.Gray
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
input_size = driver.find_element_by_xpath("//input[@id = 'kw']").get_attribute("class")   #获取文本class属性值
print(input_size)
btn_size = driver.find_element_by_xpath("//input[@id = 'su']").get_attribute("class")     #获取搜索按钮class属性值
print(btn_size)
driver.quit()
# driver.find_element_by_id("kw").send_keys("Bela")
# sleep(10)
# driver.find_element_by_id("kw").clear()     #清空文本
# sleep(5)
# driver.find_element_by_id("kw").send_keys("Kyo")    #重新赋值
# driver.find_element_by_id("su").submit()        #模仿回车
# sleep(5)
# driver.close()