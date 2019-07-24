# -*- coding:utf-8 -*-
# Author:D.Gray
from gevent import monkey
from urllib import request
import time,gevent
monkey.patch_all()

def f(url):
    print("所爬网页:",url)
    rest = request.urlopen(url)
    data = rest.read()
    print("%s bytes from url:%s"%(len(data),url))

urls = [
    "https://www.python.org/downloads/",
    "https://www.cnblogs.com/",
    "https://github.com/"
]
start_time = time.time()
for url in urls:
    f(url)
print("同步IO所需时间:%s\n"%(time.time()-start_time))


print("异步IO".center(50,'-'))
async_start_time = time.time()
gevent.joinall([
    gevent.spawn(f,"https://www.python.org/downloads/"),
    gevent.spawn(f,"https://www.cnblogs.com/"),
    gevent.spawn(f,"https://github.com/")
])
print("异步IO所需时间:%s\n"%(time.time()-async_start_time))