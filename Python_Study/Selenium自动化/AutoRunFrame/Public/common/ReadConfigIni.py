# -*- coding:utf-8 -*-
# Author:D.Gray
import configparser
import codecs
import os
from AutoRunFrame.config.Settings import Test_Data_path
class ReadConfigIni(object):
    '''
    读取INI配置文件类
    '''
    def __init__(self,file_name):
        '''
        执行方法
        :param file_name: 获取INI配置文件名
        '''
        file_path = os.path.join(Test_Data_path,file_name)
        self.Config_Ini = configparser.ConfigParser()
        self.Config_Ini.read(file_path)

    def ReadConfig(self,section,name):
        '''
        接受调用函数传参
        :param section:节名
        :param name:url名
        :return:
        '''
        value = self.Config_Ini.get(section,name)
        return value

# if __name__ == '__main__':
#     read_config = ReadConfigIni("config.ini")
#     value = read_config.ReadConfig("url","Hao123_url")
#     print(value)