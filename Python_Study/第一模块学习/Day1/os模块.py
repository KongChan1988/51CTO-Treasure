# -*- coding:utf-8 -*-
# Author:D.Greay

import os

#cmd_res = os.system('dir ')  #只执行命令，不保存结果
cmd_res = os.popen('dir').read()  # 这个方法可以取出文件
print( '---',cmd_res)

os.mkdir('New_dir')  #在day1 列表中创建一个 New_dir目录