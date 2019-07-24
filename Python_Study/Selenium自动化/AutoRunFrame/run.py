# -*- coding:utf-8 -*-
# Author:D.Gray
from HTMLTestRunner import HTMLTestRunner
import unittest
import time,os
from AutoRunFrame.config import Settings
from AutoRunFrame.Public.common import SendEmail

#测试报告路径
report_path = Settings.TestReport_path
#测试用例路径
TestCase_path = Settings.TestCase_path
def AutoRun(TestCaseName):
    '''
    测试用例名称
    :param TestCaseName: 测试用例名称
    :return:
    '''
    #加载测试用例
    discover = unittest.defaultTestLoader.discover(TestCase_path,pattern=TestCaseName)
    #获取当前时间并重命名测试报告名称
    now = time.strftime("%Y-%m-%d %H%M%S")
    reportName = "%s.html"%now
    reportPath = os.path.join(report_path,reportName)
    #打开报告路径
    with open(reportPath,"wb") as f:
        runner = HTMLTestRunner(stream=f,title="测试报告",description="测试执行结果")
        runner.run(discover)
    #获取最新测试报告
    New_Restport = SendEmail.newReport(report_path)
    # SendEmail.sendReport(new_report)  #以邮件形式发送测试报告

if __name__ == '__main__':
    AutoRun("TC_BaiduSearch.py")