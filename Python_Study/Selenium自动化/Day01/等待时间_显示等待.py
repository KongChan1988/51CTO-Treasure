# -*- coding:utf-8 -*-
# Author:D.Gray
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   #异常处理
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
el = driver.find_element_by_xpath("//input[@id='kw']")
if el.is_displayed():
    el.send_keys("Bela")
    driver.find_element_by_xpath("//input[@id='su']").click()
    driver.quit()
else:
    print("搜索框不存足")

# element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"kw")))     #显示等待
# element.send_keys("Bela")
# driver.find_element_by_xpath("//input[@id='kw']").send_keys("Bela")