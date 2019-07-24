# -*- coding:utf-8 -*-
# Author:D.Gray
import configparser
'''
将读取配置文件方法封装成一个类
'''
class ReadConfigIni(object):

    def __init__(self,file_name):
        self.cf = configparser.ConfigParser()
        self.cf.read(file_name)

    def readConfigUrl(self,section,name):
        value = self.cf.get(section,name)
        return value

ReadConfig = ReadConfigIni("config.ini")
url = ReadConfig.readConfigUrl("url","baidu")
print(url)



'''
写入ini文件，添加节
'''
# cf = configparser.ConfigParser()
# cf.read("config.ini")
# cf.add_section("title")   #新增title节
# cf.set("title","name","百度一下")  #设置title节下的name参数值 = 百度一下
# with open('config.ini',"w",encoding="utf-8") as f:
#     cf.write(f)
#
# #如果ini文件中存在相同名称的节，该做如何处理
# try:
#     cf.add_section("title")
#     cf.set("title","name2","alex")
#     cf.set("title", "name3", "kyo")
#     cf.set("title", "name5", "Mary")
# except configparser.DuplicateSectionError:
#     print("Section Title already exists")
# with open('config.ini',"w",encoding="utf-8") as f:
#     cf.write(f)


'''
读取配置文件
'''
# cf = configparser.ConfigParser()
# #读取config.ini文件
# cf.read("config.ini")
# # value = cf.get("url","baidu")
# # print(value)
# def getConfig(section,name):
#     value = cf.get(section,name)
#     return value
#
# Baidu = getConfig("url","baidu")
# print(Baidu)


