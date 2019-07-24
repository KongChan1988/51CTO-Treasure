#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
shutil.copyfilobj("f1","f2")----将f1文本内容复制给 "f2"
shutil.copyfile("本节笔记","笔记2") # shutil.copyfileobj()强化功能  自动打开文件并复制内容给另一个文件
shutil.copymode(src,dst)-----仅拷贝权限，内容、组、用户均不变
shutil.copystart(src,dst)------拷贝状态的所有信息，包括 modebits,atime,mtime...
shutil.copy(src,dst)-----
shutil.copytrue("dir1","dir2")-----递归的去拷贝文件目录
shutil.rmtree("dirname)------删除文件目录
shutil.make_archive("压缩包的文件名","压缩形式(zip、tar)","目标文件压缩路径")
例：
将E:\Python_Pycharm_work\第二模块学习\Day01\ATM" 路径下的ATM文件压缩到当前目录下
shutil.make_archive("shutil_archive_test","zip","E:\Python_Pycharm_work\第二模块学习\Day01\ATM")
'''
import shutil
# f1 = open("本节笔记",encoding='utf-8')
# f2 = open("笔记2",'w',encoding='utf-8')
# shutil.copyfileobj(f1,f2)  #将本节笔记文本内容复制给 "笔记2"

# shutil.copyfile("本节笔记","笔记2") # shutil.copyfileobj()强化功能  自动打开文件并复制内容给另一个文件
# shutil.copystat("本节笔记","笔记3")

#shutil.copytree("a","new_a") #递归的去拷贝文件目录
#shutil.rmtree("new_a")

#shutil.make_archive("shutil_archive_test","zip","E:\Python_Pycharm_work\第二模块学习\Day01\ATM")

# import zipfile
# z = zipfile.ZipFile("day5.zip",'w')  # 压缩"本节笔记和笔记2"两个文件到当前脚本目录下 压缩包名'day5.zip'
# z.write("本节笔记")
# print('----')
# z.write("笔记2")