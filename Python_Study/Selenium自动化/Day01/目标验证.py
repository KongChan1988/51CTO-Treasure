# -*- coding:utf-8 -*-
# Author:D.Gray
'''
获取验证信息，操作某页面后确认进入的是期望结果
'''
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
print("The Baidu Page".center(50,"-"))
First_title = driver.title      #获取页面Title值
print("The first pages title is %s"%First_title)
print("The Hao123 Page".center(50,"-"))
driver.find_element_by_xpath("//a[@href='https://www.hao123.com']").click()
sleep(5)
Second_title = driver.title
print("Hao123_Title：%s"%(Second_title))
Expect_Title = "hao123_上网从这里开始"
if Expect_Title == Second_title:
    print("验证通过")
else:
    print("验证失败")
driver.quit()
