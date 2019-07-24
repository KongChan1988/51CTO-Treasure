# -*- coding:utf-8 -*-
# Author:D.Gray
class TestCaseInfo(object):
    '''
    定义测试用例信息函数
    测试编号、测试时间、测试人员、测试结果....
    '''
    def __init__(self,*args,**kwargs):
        self.id=kwargs["name"]
        self.name = kwargs["name"]
        self.owner = kwargs["owner"]
        self.result = kwargs["result"]
        self.starttime = kwargs["starttime"]
        self.endtime = kwargs["endtime"]
        self.secondsDuration = kwargs["secondsDuration"]
        self.errorinfo = kwargs["errorinfo"]