# -*- coding:utf-8 -*-
# Author:D.Gray
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("file:///E:/Selenium_version/SeleniumDemo/%E8%A2%AB%E6%B5%8Bdemo/uploadfile.html")
driver.find_element_by_xpath("//input[@id='file']").send_keys("E:\Selenium_version\SeleniumDemo\被测demo\info.txt")
sleep(3)
driver.find_element_by_xpath("//input[@name='submit']").click()
driver.quit()
