# -*- coding:utf-8 -*-
# Author:D.Greay
username = 'alex'
password = '123'

_username = input('请输入用户名: ')
_password = input('请输入密码: ')

if _username == username and _password == password:
    print('Welcome user.txt {name} Login '.format(name = username.title()))
else:
    print('Please enter the correct username')
