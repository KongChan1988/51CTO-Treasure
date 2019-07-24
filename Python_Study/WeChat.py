# -*- coding:utf-8 -*-
# Author:D.Gray

import sys,os,shutil,re
while True:
    path = input('请输入微信安装路径>>>').capitalize()
    if not os.path.isdir(path):
        print('\033[31;1m无效路径\033[0m')
    else:
        num = input('请输入微信多开数>>>')
        if num.isdigit():
            num = int(num)
            if num <= 50:
                title = '@echo off\n'
                end = 'exit'
                with open('WeChat.bat','a')as fh:
                    fh.write(title)
                    for item in range(1, num + 1):
                        str = 'start /d "%~sdp0" WeChat.exe\n'
                        fh.write(str)
                    fh.write(end)
                shutil.move('WeChat.bat',path)
                os.chdir(path)
                if os.path.isfile('WeChat.bat'):
                    os.system('WeChat.bat')
                    os.remove('WeChat.bat')
                else:
                    print('\033[31;1m文件不存在\033[0m')
                exit('程序退出')
            else:
                print('\033[31;1m微信多开数超过限制\033[0m')
        else:
            print('\033[31;1m请输入有效数字\033[0m')