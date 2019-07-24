#-*-coding:utf-8 -*-
# Author: D.Gray
from conf import setting
import os,pickle
ol = os.listdir(setting.HOST_NAME_PATH)
print(ol)
for i in ol:
    if i.endswith('.json'):
        print(i)