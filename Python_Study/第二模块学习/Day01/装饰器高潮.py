#-*- Coding:utf-8 -*-
# Author: D.Gray
import time
user,passwd = 'alex','123'
def auth(auth_type):
    print('auth type:',auth_type)
    def out_wapper(func):
        print('out wapper:',func)
        def wapper(*args, **kwargs):
            print('wapper:',*args,**kwargs)
            if auth_type == 'local':
                username = input('Username:')
                pwd = input('Password:')

                if username == user and pwd == passwd:
                    print('\033[32;1m登录成功\033[0m')
                    res = func(*args, **kwargs)  # 执行home()方法  home有返回结果，func就返回'from home'
                    print('-----after authenticaion-----')
                    return res  # 定义res变量存储并返回home()的返回结果'from home'
                else:
                    exit('输入不正确')
            elif auth_type == 'ldap':
                print('搞毛线ldap,不会...')

        return wapper
    return out_wapper

def index():
    print('in the index pager')
@auth(auth_type = 'local')      # home = wapper()
def home():                     #wapper
    print('in the home pager')
    return 'from home'
@auth(auth_type = 'ldap')
def bbs():
    print('in the bbs pager')

index()
print('home的返回值:',home())           #打印home的返回值  'from home'
bbs()