# -*- coding:utf-8 -*-
# Author:D.Gray
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("file:///E:/Selenium_version/SeleniumDemo/%E8%A2%AB%E6%B5%8Bdemo/alert.html")

driver.find_element_by_xpath("//input[@name='b1']").click()
#返回alert文字信息
text = driver.switch_to.alert.text          #获取alert对话框中内容
print(text)
sleep(5)
# driver.switch_to.alert.accept()     #接受警告框  相当于点击“确定”
driver.switch_to.alert.dismiss()        #解散警告框  相当于点击“取消”
driver.quit()