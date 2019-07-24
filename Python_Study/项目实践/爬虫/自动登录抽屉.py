# -*- coding:utf-8 -*-
# Author:D.Gray
import requests
post_dict = {
    "phone":"86dsadsa",
    "password":"sadsad",
    "oneMonth":1
}
response = requests.post(
    url="https://dig.chouti.com/login",
    data = post_dict
)
print(response.text)
cookie_dict = response.cookies.get_dict()
print(cookie_dict)