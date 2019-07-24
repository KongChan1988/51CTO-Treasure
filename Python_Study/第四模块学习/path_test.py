# -*- coding:utf-8 -*-
# Author:D.Gray
import os
list = ['E:', 'python_work', '51CTO_Python', '第四模块学习', '高级FTP', 'home', 'alex', 'user_home', 'test']
hear = ''
for index in list:
    hear = os.path.join(hear,index)
    #print(hear)
print(hear)
print('list[1]:',list[0])
list[0] = '%s%s'%(list[0],'\\')

