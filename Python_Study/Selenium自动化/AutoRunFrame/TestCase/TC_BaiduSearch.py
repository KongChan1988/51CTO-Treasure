# -*- coding:utf-8 -*-
# Author:D.Gray
import unittest
import logging
from time import sleep
from AutoRunFrame.LOG.log import Logger
from AutoRunFrame.Public.common import TestCaseinfo,DoExcel,ReadConfigIni,SendEmail,ComConfig as CC
from AutoRunFrame.Public.pages.baidu import Search

#从测试数据文件中读取测试数据
baidu_sarch_value = DoExcel.ReadExcel("Demo.xls","你好").read(3,1)
baidu_sarch_url = DoExcel.ReadExcel("Demo.xls","你好").read(3,0)
print(baidu_sarch_url,baidu_sarch_value)

#开始写测试用例
class Test_Baidu_Search(unittest.TestCase):
    def setUp(self):
        self.base_url = baidu_sarch_url
        self.CaseInfo = TestCaseinfo.TestCaseInfo(id=1,name="Baidu",owner="Kyo",
                                                  result="",starttime=str(CC.getCurrentTime()),
                                                  endtime="",secondsDuration="",errorinfo="")

    def testSearch(self):
        try:
            #实例化baidu.py中的Search
            self.Baidu_search = Search()
            #打开百度URL
            self.Baidu_search.open(self.base_url)
            sleep(3)
            #打开后进行赋值操作
            self.Baidu_search.Search_Value(baidu_sarch_value)
            #调用日志
            self.log = Logger("FOX",CmdLevel=logging.DEBUG,FileLevel=logging.ERROR)
            self.log.debug(u"执行成功")
            self.log.error(u"执行成功")
            self.CaseInfo.result = "successful!!"
        except Exception as f:
            self.CaseInfo.result = "False"
            self.CaseInfo.errorinfo = str(f)
            self.log.error("因为异常:%s，执行失败"%f)
            self.log.debug("因为异常:%s，执行失败" % f)

    def testDown(self):
        pass

# if __name__ == '__main__':
#     unittest.main()
