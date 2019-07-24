# -*- coding:utf-8 -*-
# Author:D.Gray
import requests
from concurrent.futures import ProcessPoolExecutor

def fetch_request(url):
    response = requests.get(url)
    print(response.text)

url_list = [
    "www.baidu.com",
    "www.bing.com"
]
pool = ProcessPoolExecutor(10)  # 创建进程池 最多10个进程
for url in url_list:
    # 去进程池拿个进程去执行feth_request方法
    pool.submit(fetch_request, url)
    print(url)

pool.shutdown(True)