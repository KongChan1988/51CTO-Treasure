# -*- coding:utf-8 -*-
# Author:D.Gray

import os,re
list = []
with open('ttt','r') as f:
        lines = f.readlines()
        for line in lines:
            if not re.search('Alex',line):
                list.append(line)

with open('ttt','w') as f:
    f.writelines(list)
