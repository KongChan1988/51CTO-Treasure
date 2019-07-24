# -*- coding:utf-8 -*-
# Author:D.Gray
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.set_window_size(800,600)
# driver.maximize_window()
sleep(5)
# driver.find_element(by="id",value="kw").send_keys("Bela")
# driver.find_element(by="id",value="su").click()

# driver.find_element_by_css_selector("#sb_form_q").send_keys("Bela")
# driver.find_element_by_css_selector("#sb_form_go").click()
# driver.find_element_by_css_selector("[name='q']").send_keys("Bela")
# driver.find_element_by_css_selector("[name='go']").click()
# driver.find_element_by_css_selector("#kw").send_keys("Bela")
#sb_form_q

# driver.close()