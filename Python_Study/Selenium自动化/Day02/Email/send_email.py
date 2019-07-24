# -*- coding:utf-8 -*-
# Author:D.Gray
import unittest
import smtplib
import time
import os
from email.mime.text import MIMEText
from email.header import Header
from HTMLTestRunner import HTMLTestRunner

print("开始发送邮件".center(50,"-"))
def sendReport(file_new):
    with open(file_new,'rb') as f:
        email_body = f.read()
    msg = MIMEText


# print("发送邮件".center(50,"-"))
# def sendReport(file_new):
#     '''
#
#     :param file_new:
#     :return:
#     '''
#     with open(file_new,"rb") as f:
#         new_body = f.read()
#     msg = MIMEText(new_body,"html","utf-8")  #构造MIMEText对象，作为邮件内容的形式进行附加
#     msg["Subject"] = Header("自动化测试报告","utf-8")
#     msg["From"] = "wangwei@linkmores.com"  #发送地址
#     msg["to"] = "wangwei@linkmores.com"    #收件地址
#
#     smtp = smtplib.SMTP("smtp.mxhichina.com")         #邮件服务器地址
#     smtp.login("wangwei@linkmores.com","sdchendijayD1988")    #邮箱账号和密码
#     smtp.sendmail(msg["From"],msg["to"].split(";"),msg.as_string())  #多个收件人用 ;号分割
#     smtp.quit()
#     print("The HTML Send Out".center(50,"-") )
#
# def newReport(testReport):
#     lists = os.listdir(testReport)  #操作本地目录  列出本地目录文件
#     lists2 = sorted(lists)      #获得排序后的测试报告列表
#     file_name = os.path.join(testReport,lists2[-1])  #获得最新一条HTML报告
#     # print(file_name)
#     return file_name
#
# print("开始运行".center(50,"-"))
# if __name__ == '__main__':
#     test_dir = "E:\\python_work\\51CTO_Python\Selenium自动化\Day02\Email"  #测试用例路径
#     test_report = "E:\\python_work\\51CTO_Python\Selenium自动化\Day02\Email\TestReport"  #测试报告路径
#
#     discover = unittest.defaultTestLoader.discover(test_dir,"baidu.py") #加载测试函数
#     now = time.strftime("%Y-%m-%d %H%M%S")  #当前时间
#     file_path = os.path.join(test_report,"%sresult.html"%now)   #拼接出测试报告名称
#     with open(file_path,"wb") as fe:
#         runner = HTMLTestRunner(stream=fe,title="测试结果",description="测试执行结果")
#         runner.run(discover)
#     new_report = newReport(test_report)     #获取最新测试报告
#     print(new_report)
#     sendReport(new_report)      #发送最新测试报告







