# -*- coding:utf-8 -*-
# Author:D.Gray
import os,sys,shelve
from conf import setting
class Users(object):
    '''
    用户信息类
    '''
    def __init__(self):
        self.user_file = setting.USER_FILE
        self.users_reads = self.read_users()

    def read_users(self):
        print(self.user_file)
        with open(self.user_file,"r") as f:
            users_read = eval(f.read())
        return users_read

    def get_users(self):
        print(self.users_reads)
        return self.users_reads

    def get_user(self,username):
        '''
        获取user.db信息字典内容
        :param username: 接受客户端中格式化输出cmd[1] 用户名
        :return:
        '''
        for user in self.users_reads:
            if user["username"] == username:
                return user

