# -*- coding:utf-8 -*-
# Author:D.Gray
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep,ctime
driver = webdriver.Firefox()
'''
implicitly_Wait是隐士等待
判断某元素，如果超过10秒未发现，则抛出异常
如果在10秒内发现，则对元素进行操作
'''
driver.implicitly_wait(30)          #有隐士等待和显示等待 最长等待时间取他两最大值
driver.get("https://www.baidu.com")
try:
    print(ctime())      #谁先找到元素就先执行谁
    WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.ID,"kw")))
    driver.find_element_by_xpath("//input[@id='kw']").send_keys("Bela")
    driver.find_element_by_xpath("//input[@id='su']").click()
    sleep(5)
    driver.quit()
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    driver.quit()