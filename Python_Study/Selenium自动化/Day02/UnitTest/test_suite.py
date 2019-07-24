# -*- coding:utf-8 -*-
# Author:D.Gray
from Day02.UnitTest.StringReplace import StringReplaceTestCase
import unittest,os
from time import strftime
from HTMLTestRunner import HTMLTestRunner
if __name__ == '__main__':
    '''
    执行全部测试用例
    '''
    allSuite = unittest.makeSuite(StringReplaceTestCase,"test")
    path = os.path.join("E:\\python_work\\51CTO_Python\Selenium自动化\Day02\\UnitTest\\TestReport","HTMLRun.html")
    with open(path,"wb") as f:
        runner = HTMLTestRunner(
            stream = f,
            title = "测试结果",
            description="测试用例执行情况"
            )
        runner.run(allSuite)
    runner = unittest.TextTestRunner(verbosity=2)  #verbosity=2 输出详细信息



    # '''
    #         运行部分测试用例方式二
    #         '''
    # suite = unittest.TestSuite()  # 定义TestSuite类
    # tests = [StringReplaceTestCase("testOrd"), StringReplaceTestCase("testOrdBlack")]
    # suite.addTests(tests)
    # runner = unittest.TextTestRunner()  # 控制测试套件运行
    # runner.run(suite)  # 运行测试套件


    # '''
    # 运行部分测试用例方式一
    # '''
    # suite = unittest.TestSuite()  # 定义TestSuite类
    # suite.addTest(StringReplaceTestCase("testOrd"))
    # suite.addTest(StringReplaceTestCase("testOrdBlack"))
    # runner = unittest.TextTestRunner()  #控制测试套件运行
    # runner.run(suite)           #运行测试套件




