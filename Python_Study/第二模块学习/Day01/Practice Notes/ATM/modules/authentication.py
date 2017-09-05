#-*- Coding:utf-8 -*-
# Author: D.Gray

import os,json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''数据库文件相对路径'''
__db_users_dict = BASE_DIR + r"\database\users_dict"
__db_creditcard_dict = BASE_DIR + r"\database\creditcard_dict"

'''认证装饰器'''
def auth(auth_type):
    def outer_wrapper(func):
        if auth_type == "user_auth":
            def wrapper():
                res = func()
                username = input("\33[34;0m请输入用户名：\33[0m")
                password = input("\33[34;0m请输入密码：\33[0m")
                if len(username.strip())  > 0:
                    with open(__db_users_dict, "r+") as f_users_dict:
                        users_dict = json.loads(f_users_dict.read())
                        if username in users_dict.keys():
                            if password == users_dict[username]["password"]:
                                if users_dict[username]["locked"] == 0:
                                    print("\33[31;0m用户 %s 认证成功\33[0m"%(username))
                                    return res,username
                                else:
                                    print("\33[31;0m用户 %s 已经被锁定 认证失败\33[0m" % (username))
                            else:
                                print("\33[31;0m输入的密码不匹配 认证失败\33[0m")
                        else:
                            print("\33[31;0m输入的用户名不存在 认证失败\33[0m")
                else:
                    print("\33[31;0m输入的用户名为空 认证失败\33[0m")
            return wrapper

        if auth_type == "creditcard_auth":
            def wrapper():
                res = func()
                creditcard = input("\33[34;0m输入信用卡卡号(6位数字)：\33[0m")
                password = input("\33[34;0m输入信用卡的密码：\33[0m")
                if len(creditcard.strip()) > 0:
                    with open(__db_creditcard_dict, "r+") as f_creditcard_dict:
                        creditcard_dict = json.loads(f_creditcard_dict.read())
                        if creditcard in creditcard_dict.keys():
                            if password == creditcard_dict[creditcard]["password"]:
                                if creditcard_dict[creditcard]["locked"] == 0:
                                    print("\33[31;0m信用卡 %s 认证成功\33[0m" % (creditcard))
                                    return res,creditcard
                                else:
                                    print("\33[31;0m信用卡 %s 已经被冻结 认证失败\33[0m" % (creditcard))
                            else:
                                print("\33[31;0m输入的密码不匹配 认证失败\33[0m")
                        else:
                            print("\33[31;0m输入的信用卡卡号不存在 认证失败\33[0m")
                else:
                    print("\33[31;0m输入的信用卡卡号为空 认证失败\33[0m")
            return wrapper

        if auth_type == "admincenter_auth":
            def wrapper():
                res = func()
                admincenter_dict ={"admin":"admin"}
                username = input("\33[34;0m请输入管理用户名：\33[0m")
                password = input("\33[34;0m请输入管理密码：\33[0m")
                if len(username.strip()) > 0:
                        if username in admincenter_dict.keys():
                            if password == admincenter_dict[username]:
                                print("\33[31;0m管理用户 %s 认证成功\33[0m" % (username))
                                return res, username
                            else:
                                print("\33[31;0m输入的密码不匹配 认证失败\33[0m")
                        else:
                            print("\33[31;0m输入的用户名不存在 认证失败\33[0m")
                else:
                    print("\33[31;0m输入的用户名为空 认证失败\33[0m")

            return wrapper
    return outer_wrapper

'''用户登录认证'''
@auth(auth_type="user_auth")
def user_auth():
    print("\33[32;0m用户登录认证\33[0m".center(40,"-"))
    return "True"

'''信用卡认证'''
@auth(auth_type="creditcard_auth")
def creditcard_auth():
    print("\33[32;0m信用卡登录认证\33[0m".center(40,"-"))
    return "True"

'''后台管理认证'''
@auth(auth_type="admincenter_auth")
def admincenter_auth():
    print("\33[32;0m后台管理登录认证\33[0m".center(40,"-"))
    return "True"