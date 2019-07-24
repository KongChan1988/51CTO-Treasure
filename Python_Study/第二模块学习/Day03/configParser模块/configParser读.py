#-*- Coding:utf-8 -*-
# Author: D.Gray
import configparser

conf = configparser.ConfigParser()
conf.read("example.ini")

print(conf.sections())
print(conf.defaults())
print(conf['DEFAULT']['serveraliveinterval'])
print(conf['topsecret.server.com']['host port'])

sec = conf.remove_section('bitbucket.org')  #删除conf文件中 'bitbucket.org'元素  创建新文件
conf.write(open('new_example.ini','w'))     #将刷新后的内容赋值到新文件 new_example.ini文件中