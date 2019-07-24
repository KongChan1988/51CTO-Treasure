#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
os.getcwd()-----获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")------改变当前脚本工作目录，相当于shell下的cd
os.curdir------返回当前目录
os.makedirs("dirname1\dirname2")------可生产多层递归目录   os.mkdir()升级优化
os.removedirs("dirname")------若目录为空则删除，并递归到上一级目录，如若为空也删除，以此类推
os.mkdir("dirname")------生产单级目录，相当于shell中mkdir dirname
os.rmdir("dirname")-----删除单级空目录，若目录为空则删除  一次命令只删一级空目录
os.listdir("dirname")------列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.listdir('.')-----当前目录下所有文件夹
os.listdir(r"D:")-----获得D盘下所有文件夹
os.remove("文件名")-----删除一个文件
os.rename("X","Y")-----重命名文件/目录  os.rename(r"C:\a\1.txt",r"C:\a\2.txt")
os.stat("path/filename")----获取文件/目录信息     os.stat(r"C:\a\1.txt")
os.sep----输出操作系统特定的路径分隔符，win下为"\\"  Linux下为"/"
os.linesep------输出当前平台使用的行终止符, win下为"\r\n"  Linux下为"\n"
os.pathsep-----输出用于分隔文件路径的字符串   win下为";"  Linux下为":"
os.environ-----查看当前系统环境变量
os.name----输出当前系统名。 win----nt   Linux---posix
os.system()----执行当前系统命令   os.system("dir")、os.system("ipconfig")、os.system("cnd")
os.path.abspath("dirname") ---- 返回path规范化的绝对路径
os.path.split(path)----将path分割成目录和文件名二元组返回
os.path.dirname(path)----返回path的目录，其实就是os.path.split(path)的第一个元素
os.path.basename(path)----返回path的目录，其实就是os.path.split(path)的最后一个元素
os.path.exists(r"C:")-----path路径存在 True  反之False
os.path.isabs()----判断是否是绝对路径
os.path.isfile(psth)----判断是否是文件  os.path.isfile(r"C:\a\b\c\2.txt")
os.path.isdir(path)-----判断是否是目录
os.path.join(r"C:\",r"a",r"b",r"c")----将多个路径组合返回，第一个绝对路径之前的参数将会被返回
os.path.getatime(path)----返回path所指向文件或者目录的最后存取时间   os.path.getatime(r"C:\a\b\c\2.txt")
os.path.getmtime(path)-----返回path所指向文件或者目录的最后修改时间
'''

import os
print(os.environ)
#os.remove("E:\Python_Pycharm_work\第二模块学习\Day03\常用模块学习.zip")