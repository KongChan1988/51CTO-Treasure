# -*- coding:utf-8 -*-
# Author:D.Gray
from selenium import webdriver
from time import  sleep
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
# driver.find_element_by_xpath("//input[@id='kw' and @class = 's_ipt']").send_keys("Bela")
driver.find_element_by_xpath("//input[@id = 'kw'][@class = 's_ipt']").send_keys("Bela")
driver.find_element_by_xpath("//span[@class='bg s_btn_wr']/input").click()      #层级识别

# driver.find_element_by_class_name("s_ipt").send_keys("Bela")
# driver.find_element_by_partial_link_text("新").click()       #link关键字匹配
# driver.find_element_by_link_text("新闻").click()          #通过link来定位元素
# driver.find_element_by_name("wd").send_keys("Bela")
# driver.find_element_by_id("kw").send_keys("Bela")
# driver.find_element_by_id("su").click()
sleep(5)
driver.close()