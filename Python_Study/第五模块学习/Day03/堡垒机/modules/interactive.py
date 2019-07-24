#-*-coding:utf-8 -*-
# Author: D.Gray
# Copyright (C) 2003-2007  Robey Pointer <robeypointer@gmail.com>
#
# This file is part of paramiko.
#
# Paramiko is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# Paramiko is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Paramiko; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA.


import socket
import sys
from paramiko.py3compat import u
from database import create_table
# from modules.views import log_recording
import datetime
import redis
import time

# windows does not have termios...
try:
    import termios
    import tty

    has_termios = True
except ImportError:
    has_termios = False


def interactive_shell(chan, user_obj, bind_host_obj, cmd_caches, log_recording):
    '''
    :param chan:
    :param user_obj:
    :param bind_host_obj: 主机
    :param cmd_caches: 命令列表
    :param log_recording: 日志记录
    :return:
    '''
    # 判断是否是windows shell
    if has_termios:
        posix_shell(chan, user_obj, bind_host_obj, cmd_caches, log_recording)
    else:
        windows_shell(chan)


def posix_shell(chan, user_obj, bind_host_obj, cmd_caches, log_recording):
    '''

    :param chan:
    :param user_obj:
    :param bind_host_obj:
    :param cmd_caches:
    :param log_recording:
    :return:
    '''
    import select

    oldtty = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)
        cmd = ''
        tab_key = False
        while True:
            r, w, e = select.select([chan, sys.stdin], [], [])
            if chan in r:
                try:
                    x = u(chan.recv(1024))
                    if tab_key:
                        if x not in ('\x07', '\r\n'):
                            # print('tab:',x)
                            cmd += x
                        tab_key = False
                    if len(x) == 0:
                        sys.stdout.write('\r\n*** EOF\r\n')
                        # test for redis to mysql
                        break
                    sys.stdout.write(x)
                    sys.stdout.flush()
                except socket.timeout:
                    pass
            if sys.stdin in r:
                x = sys.stdin.read(1)
                if '\r' != x:
                    cmd += x
                else:
                    user_record_cmd = user_obj.username + '_user_record'
                    pool = redis.ConnectionPool(host='localhost', port=22)
                    user_record = [user_obj.id, bind_host_obj.id, 'cmd', cmd,
                                   time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())]
                    r = redis.Redis(connection_pool=pool)
                    r.lpush(user_record_cmd, user_record)
                    cmd = ''
                    # 最后用户退出的时候取出来log_item 列表循环写入数据库
                if '\t' == x:
                    tab_key = True
                if len(x) == 0:
                    break
                chan.send(x)

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)


# thanks to Mike Looijmans for this code
def windows_shell(chan):
    '''

    :param chan:
    :return:
    '''
    import threading

    sys.stdout.write("Line-buffered terminal emulation. Press F6 or ^Z to send EOF.\r\n\r\n")

    def writeall(sock):
        while True:
            data = sock.recv(256)
            if not data:
                sys.stdout.write('\r\n*** EOF ***\r\n\r\n')
                sys.stdout.flush()
                break
            sys.stdout.write(data.decode())
            sys.stdout.flush()

    writer = threading.Thread(target=writeall, args=(chan,))
    writer.start()

    try:
        while True:
            d = sys.stdin.read(1)
            if not d:
                break
            chan.send(d)
    except EOFError:
        # user.txt hit ^Z or F6
        pass