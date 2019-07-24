# -*- coding:utf-8 -*-
# Author:D.Gray
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.find_element_by_xpath("//input[@id = 'kw']").send_keys("Beal")
sleep(15)
driver.find_element_by_xpath("//input[@id = 'su']").click()
driver.close()