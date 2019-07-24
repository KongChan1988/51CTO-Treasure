# -*- coding:utf-8 -*-
# Author:D.Gray
import requests
import requests
from concurrent.futures import ThreadPoolExecutor

def fetch_request(url):
    response = requests.get(url)
    print(response.text)

url_list = [
    "www.baidu.com",
    "www.bing.com"
]
pool = ThreadPoolExecutor(10)  #创建线程池 最多10个线程
for url in url_list:
    # 去线程池拿个线程去执行feth_request方法
    pool.submit(fetch_request,url)
    print(url)

pool.shutdown(True)
