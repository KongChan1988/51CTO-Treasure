# -*- coding:utf-8 -*-
# Author:D.Gray
import requests,uuid,os
from bs4 import BeautifulSoup
reponse = requests.get(
    url="https://ai235.com/qq/list-all-6.html",
)
reponse.encoding = reponse.apparent_encoding
# print(reponse.text)
soup = BeautifulSoup(reponse.text,features="html.parser")
target = soup.find(id="grid")
a_list = target.find_all('a')
for i in a_list:
    img_url = i.find("img").attrs.get("src")
    print("开始下载gif动图",img_url)
    img_res = requests.get(url=img_url)
    file = str(uuid.uuid4()) + ".gif"
    path = os.path.join("picture",file)
    with open(path,'wb') as f:
        f.write(img_res.content)