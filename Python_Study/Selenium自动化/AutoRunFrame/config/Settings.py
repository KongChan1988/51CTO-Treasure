# -*- coding:utf-8 -*-
# Author:D.Gray
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)

#日志文件路径
log_path = os.path.join(BASE_DIR,"Report","Log")
# print(log_path)

#测试报告路径
TestReport_path = os.path.join(BASE_DIR,"Report","TestReport")
# print(TestReport_path)

#测试数据路径
Test_Data_path = os.path.join(BASE_DIR,"Data","TestData")
# print(Test_Data_path)

#测试用例路径
TestCase_path = os.path.join(BASE_DIR,"TestCase")
# print(TestCase_path)

