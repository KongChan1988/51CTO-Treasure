# -*- coding:utf-8 -*-
# Author:D.Gray
import requests
import os
from bs4 import BeautifulSoup
url="https://www.autohome.com.cn/news/"
response = requests.get(url)
response.encoding = response.apparent_encoding
# print(response.text)
soup = BeautifulSoup(response.text,features='html.parser')   #featrues是python自带的 实际场合用lxml
target = soup.find(id='auto-channel-lazyload-article') #使用BeautifulSoup获取页面中 id = auto-channel-lazyload-article的标签
li_list = target.find_all('li')     #获取id='auto-channel-lazyload-article'下的所有li标签   find_all():获取所有标签
for i in li_list:
    a = i.find('a') #获取所有a标签
    if a:
        txt = a.find('h3').text         #获取所有a标签下的h3标签  txt是个tag对象
        print("h3-txt：",txt,type(txt))
        img_url = a.find('img').attrs.get("src")  #获取img标签的src属性
        print("img图片:",img_url)
        new_img_url = 'http:%s'%img_url     #重新定义图片URL
        img_response = requests.get(url=new_img_url)    #获取图片
        import uuid
        file_name = str(uuid.uuid4()) + ".jpg"      #随机生成图片名
        path = os.path.join('picture',file_name)
        with open(path,'wb') as f:
            f.write(img_response.content)       #写入相应文件目录


