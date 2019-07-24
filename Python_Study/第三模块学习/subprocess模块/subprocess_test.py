#-*- Coding:utf-8 -*-
# Author: D.Gray

import os,subprocess
'''
os.system()----输出命令结果到屏幕，返回命令执行状态结果  命令执行结果成功:0  命令执行结果不成功:非0
os.popen()---只是获得一个内存对象
    例：
    >>> os.popen('dir')
    <os._wrap_close object at 0x0000000002A04278>
os.popen().read()-----会保存命令的执行结果输出   read（）完需要在print下整理显示样式
subprocess.run()----比system、popen模块更强大
subprocess.run("df -h |grep sda1",shell = True)  #有管道符 '|' 必须 shell

#接收字符串格式命令，返回元组形式，第1个元素是执行状态，第2个是命令结果
>>> subprocess.getstatusoutput('ls /bin/ls')
(0, '/bin/ls')
'''
#接收字符串格式命令，返回元组形式，第1个元素是执行状态，第2个是命令结果
res = subprocess.getstatusoutput('dir')
print(res)




