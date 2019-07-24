# -*- coding:utf-8 -*-
# Author:D.Gray

import sys,time
for i in range(20):
    sys.stdout.write('#')   #   sys.stdout.write  标准输出
    sys.stdout.flush()      #   刷新缓存
    time.sleep(0.1)         #   停顿0.1秒钟