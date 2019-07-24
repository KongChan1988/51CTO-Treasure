# -*- coding:utf-8 -*-
# Author:D.Greay
import getpass   #导入getpass库

_username = 'aliex'
_password = 'abc123'
username = input('username:')
password = getpass.getpass('password:')  #密文形式 输入密码
if _username == username and _password == password:
    print('Welcome user.txt {name} Login...' .format(name = username.title()))
else:
    print('Inavalid username or password!')
 # print(username,password)  #IndentationError:  缩进错误