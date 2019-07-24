# -*- coding:utf-8 -*-
# Author:D.Gray
import unittest
'''
组织多个测试用例
'''
class StringReplaceTestCase(unittest.TestCase):
    def setUp(self):
        self.source = "selenium"

    '''测试空字符串的替换'''
    def testBlack(self):
        expect = "selenium"
        result = self.source.replace("","")
        self.assertEqual(expect,result)

    '''测试空字符串的替换为常规字符 *号'''
    def testBlackOrd(self):
        expect = "se*le*n*ium"
        result = self.source.replace("","*")
        self.assertEqual(expect,result)

    '''测试常规字符串的替换为空字符串'''
    def testOrdBlack(self):
        expect = "seleni"
        result = self.source.replace("um","")
        self.assertEqual(expect,result)

    '''测试常规字符串的替换为其他字符串'''
    def testOrd(self):
        expect = "seleniumm"
        result = self.source.replace("m","mm")
        self.assertEqual(expect,result)
'''
执行全部测试用例
'''
def suite():
    StringReplaceTestSuite = unittest.makeSuite(StringReplaceTestCase,"test")
    return StringReplaceTestSuite


# '''
# 执行部分测试用例
# '''
# def suite():
#     StringReplaceTestSuite = unittest.TestSuite()
#     StringReplaceTestSuite.addTest(StringReplaceTestCase("testBlackOrd"))
#     StringReplaceTestSuite.addTest(StringReplaceTestCase("testBlack"))
#     return StringReplaceTestSuite


# '''
# 构建测试套件 testsuite
# '''
# StringReplaceTestSuite = unittest.TestSuite()
# StringReplaceTestSuite.addTest(StringReplaceTestCase("testOrd"))     #TestSuite对象.addTest(用例类名(用例名称test开头))
# StringReplaceTestSuite.addTest(StringReplaceTestCase("testOrdBlack"))     #TestSuite对象.addTest(用例类名(用例名称test开头))

# '''
# 构建测试固件
# '''
# class StringReplaceTestCase(unittest.TestCase):
#     '''定义源测试字符串'''
#     def setUp(self):
#         self.source = "selenium"
#
# class StringReplaceTestCase1(StringReplaceTestCase):
#     '''测试空字符串的替换'''
#     def runTest(self):
#         expect = "selenium"         #预期结果
#         result = self.source.replace("","")      #将源字符串中空字符串替换为空字符串后的结果
#         self.assertEqual(expect,result)  #将将源字符串中空字符串替换为空字符串后的结果 与 expect进行对比
#
# class StringReplaceTestCase2(StringReplaceTestCase):
#     '''测试空字符串的替换为常规字符 *号'''
#     def runTest(self):
#         expect = "se*le**n*ium"         #预期结果
#         result = self.source.replace("","*")      #将源字符串中空字符串替换为"*"后的结果
#         self.assertEqual(expect,result)   #将源字符串中空字符串替换为"*"后的结果 与 expect进行对比
#
# class StringReplaceTestCase3(StringReplaceTestCase):
#     '''测试常规字符串的替换为空字符串'''
#     def runTest(self):
#         expect = "seleni"         #预期结果
#         result = self.source.replace("um","")      #将源字符串中常规字符串的替换为空字符串
#         self.assertEqual(expect,result)  #将源字符串中常规字符串的替换为空字符串后在与expect进行对比
#
# class StringReplaceTestCase4(StringReplaceTestCase):
#     '''测试常规字符串的替换为其他字符串'''
#     def runTest(self):
#         expect = "selenium"         #预期结果
#         result = self.source.replace("m","mm")      #将源字符串中常规字符串的替换为空字符串
#         self.assertEqual(expect,result)  #将源字符串中常规字符串的替换为空字符串后在与expect进行对比




'''
构建单元测试用例
'''
# class StringReplaceTestCase1(unittest.TestCase):
#     '''测试空字符串的替换'''
#     def runTest(self):
#         sourse = "selenium"         #源字符串
#         expect = "selenium"         #预期结果
#         result = sourse.replace("","")      #将源字符串中空字符串替换为空字符串后的结果
#         self.assertEqual(expect,result)  #将将源字符串中空字符串替换为空字符串后的结果 与 expect进行对比
#
# class StringReplaceTestCase2(unittest.TestCase):
#     '''测试空字符串的替换为常规字符 *号'''
#     def runTest(self):
#         sourse = "selenium"             #源字符串
#         expect = "se*le**n*ium"         #预期结果
#         result = sourse.replace("","*")      #将源字符串中空字符串替换为"*"后的结果
#         self.assertEqual(expect,result)   #将源字符串中空字符串替换为"*"后的结果 与 expect进行对比
#
# class StringReplaceTestCase3(unittest.TestCase):
#     '''测试常规字符串的替换为空字符串'''
#     def runTest(self):
#         sourse = "selenium"             #源字符串
#         expect = "seleni"         #预期结果
#         result = sourse.replace("um","")      #将源字符串中常规字符串的替换为空字符串
#         self.assertEqual(expect,result)  #将源字符串中常规字符串的替换为空字符串后在与expect进行对比
#
# class StringReplaceTestCase4(unittest.TestCase):
#     '''测试常规字符串的替换为其他字符串'''
#     def runTest(self):
#         sourse = "selenium"             #源字符串
#         expect = "selenium"         #预期结果
#         result = sourse.replace("m","mm")      #将源字符串中常规字符串的替换为空字符串
#         self.assertEqual(expect,result)  #将源字符串中常规字符串的替换为空字符串后在与expect进行对比