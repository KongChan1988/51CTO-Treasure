# -*- coding:utf-8 -*-
# Author:D.Gray
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
sleep(5)

# #右击操作
# right_click = driver.find_element_by_xpath("//a[@href='http://news.baidu.com']")
# ActionChains(driver).context_click(right_click).perform()

# #悬停操作
# on_stop = driver.find_element_by_xpath("//a[@href='http://www.baidu.com/gaoji/preferences.html']")
# ActionChains(driver).move_to_element(on_stop).perform()

#双击操作
driver.find_element_by_xpath("//input[@id='kw']").send_keys("Bela")
driver.find_element_by_xpath("//input[@id='su']").click()
print("点击搜索后")
sleep(5)
double_click = driver.find_element_by_xpath("//input[@id='kw']")
ActionChains(driver).double_click(double_click).perform()       #对double_click对象进行双击
print("双击操作完成")