# -*- coding:utf-8 -*-
# Author:D.Gray
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
print("进入百度首页")
sleep(5)
url = "http://news.baidu.com/"
driver.get(url)
print("前往百度新闻：%s"%url)
sleep(5)
driver.refresh()        #刷新
print("刷新了页面")
sleep(5)
driver.back()       #返回上一级页面
print("返回了百度首页")
driver.close()