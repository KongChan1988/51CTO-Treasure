# -*- coding:utf-8 -*-
# Author:D.Gray
import requests
from bs4 import BeautifulSoup
r1 = requests.get(url="https://hc.lzybd.com/UserControl/ImageCode.aspx")
r1.encoding = r1.apparent_encoding
cookie = r1.cookies.get_dict()
soup = BeautifulSoup(r1.text,features="html.parser")
value = soup.find(id="__VIEWSTATE").attrs.get("value")
print(value)


r2 = requests.get(url="https://hc.lzybd.com/store/")
r2.encoding = r2.apparent_encoding
cookie2 = r2.cookies.get_dict()
soup = BeautifulSoup(r2.text,features="html.parser")
value2 = soup.find(id="__VIEWSTATE").attrs.get("value")
print(value2)
