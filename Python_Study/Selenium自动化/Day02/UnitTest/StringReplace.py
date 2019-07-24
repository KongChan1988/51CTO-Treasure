# -*- coding:utf-8 -*-
# Author:D.Gray
import unittest
class StringReplaceTestCase(unittest.TestCase):
    def setUp(self):
        self.source = "selenium"

    def testBlack(self):
        '''测试空字符串的替换'''
        expect = "selenium"
        result = self.source.replace("", "")
        self.assertEqual(expect, result)

    # @unittest.skipUnless(4<3,"don't run this case")     #条件为True时执行此用例
    # @unittest.skipIf(4<3,"don't run this case")     #条件为True时跳过此用例，条件为False执行此用例
    @unittest.skip("don't run this case")           #强制跳过此用例
    def testBlackOrd(self):
        '''测试空字符串的替换为常规字符 *号'''
        expect = "se*le*n*ium"
        result = self.source.replace("", "*")
        self.assertEqual(expect, result)

    def testOrdBlack(self):
        '''测试常规字符串的替换为空字符串'''
        expect = "seleni"
        result = self.source.replace("um", "")
        self.assertEqual(expect, result)

    def testOrd(self):
        '''测试常规字符串的替换为其他字符串'''
        expect = "selenium"
        result = self.source.replace("m", "mm")
        self.assertEqual(expect, result)

