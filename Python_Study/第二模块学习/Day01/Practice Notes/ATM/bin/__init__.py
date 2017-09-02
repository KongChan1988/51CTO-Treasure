#-*- Coding:utf-8 -*-
# Author: D.Gray

import os
print(__file__) #获取当前程序所在相对路径
print(os.path.abspath(__file__))    #返回绝对路径
print(os.path.dirname(os.path.abspath(__file__))) #返回目录名，不要文件名

print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  #返回到ATM目录下
import sys  #添加环境变量
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)
from conf import settings     #导入conf目录中的 settings文件
from core import main         #导入core目录中的 main文件

main.login()                    #调用mian文件中的login函数

