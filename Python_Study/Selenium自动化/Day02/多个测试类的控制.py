# -*- coding:utf-8 -*-
# Author:D.Gray
import unittest
'''
多个测试类的控制
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
        expect = "selenium"
        result = self.source.replace("m","mm")
        self.assertEqual(expect,result)

class StringStripTestCase(unittest.TestCase):
    def setUp(self):
        self.source = "Pythmn"

    def testBlack(self):
        expect = "Python"
        result = self.source.replace("m","8")
        self.assertEqual(expect,result)

    def testOrd(self):
        expect = "Python"
        result = self.source.replace("m","o")
        self.assertEqual(expect,result)

def suite():
    StringReplaceTestSuit = unittest.makeSuite(StringReplaceTestCase,"test")    #执行StringReplaceTestCase类中所有用例
    StringStripTestSuit = unittest.makeSuite(StringStripTestCase,"test")

    alltests = unittest.makeSuite(StringReplaceTestSuit,StringStripTestSuit)  #测试套件里面嵌套测试套件
    return alltests