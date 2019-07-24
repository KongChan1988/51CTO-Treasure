#-*- Coding:utf-8 -*-
# Author: D.Gray
import os,sys,json
from conf import setting
class Users(object):

    def __init__(self,username):
        self.username = username
        self.user_file = setting.USER_FILE + "\%s.json"%(self.username)
        self.users_read = self.read_users()

    def read_users(self):
        if os.path.exists(self.user_file):
            with open(self.user_file, 'r') as f:
                user_read = eval(f.read())
                return user_read

    def get_user(self):
        try:
            user = self.users_read["username"]
            if user == self.username:
                return self.users_read
        except TypeError as e:
            pass

    def update_status(self):
        with open(self.user_file, 'r') as f:
            fr = f.read()
            user_read = eval(fr)

        with open(self.user_file,'w') as fw:
            res = fr.replace(str(user_read['status']),str(1))
            fw.write(res)
        return self.users_read