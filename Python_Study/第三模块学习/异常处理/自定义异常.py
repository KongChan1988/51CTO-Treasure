#-*- Coding:utf-8 -*-
# Author: D.Gray
class AlexException(Exception):
    def __init__(self,msg):
        self.message = msg

    # def __str__(self):
    #     return self.message

try:
    raise  AlexException('数据库连不上')
except  AlexException as e:
    print(e)