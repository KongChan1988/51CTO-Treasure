#-*- Coding:utf-8 -*-
# Author: D.Gray
'''

导入方法：
import module_name
import module1_name,module2_name
from module_alex import *  （不建议使用）
from module_alex import logger as XX

2、import本质（路劲搜索和搜索路径）
包：用来从逻辑上组织模块，本质就是一个目录（必须带有一个__init__.py文件
导入模块的本质就是把python文件解释一遍
导入包的本质就是执行该包下的__init__.py文件

4、导入优化

5、模块的分类
1、标准库
2、开源模块
3、自定义模块
'''

import module_alex,os,sys
#from module_alex import *  不建议使用,使用时要避免 冲突
from module_alex import logger as la
print(module_alex.name)
module_alex.say_hello()

def logger():
    print('in the core')

logger()        # main模块下的logger()

la()    #module_alex模块下的logger()函数