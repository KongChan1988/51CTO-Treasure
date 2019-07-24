# -*- coding:utf-8 -*-
# Author:D.Gray
from selenium import webdriver
from time import sleep
import uuid,os
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.find_element_by_xpath("//input[@id='kw']").send_keys("Bela")
driver.find_element_by_xpath("//input[@id='su']").click()
sleep(1)
picture = '%s.png'%str(uuid.uuid4())
file_path = os.path.join("E:\\python_work\\51CTO_Python\Selenium自动化\Day01\截图文件",picture)
driver.get_screenshot_as_file(file_path)        #屏幕截图并保存到指定文件路径下

# driver.set_window_size(800,600)
# driver.find_element_by_xpath("//input[@id='kw']").send_keys("Bela")
# driver.find_element_by_xpath("//input[@id='su']").click()
# sleep(5)
# js = "window.scrollTo(300,600)"   #x轴移动100  y轴移动500
# driver.execute_script(js)

# cookies = driver.get_cookies()          #获取cookie
# print(cookies)
# for row in cookies:
#     print("获取cookie中的name",row["name"])