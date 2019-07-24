#-*-coding:utf-8 -*-
# Author: D.Gray
import base64
import getpass
import os
import socket
import sys
import traceback
from paramiko.py3compat import input
from database import create_table
import redis
import datetime
import time

import paramiko
try:
    import interactive
except ImportError:
    from . import interactive


def ssh_login(user_obj, bind_host_obj, mysql_engine, log_recording):
    '''
    ssh登陆
    :param user_obj:
    :param bind_host_obj:
    :param mysql_engine: 连接数据库
    :param log_recording: 写日志记录
    :return:
    '''
    # now, connect and use paramiko Client to negotiate SSH2 across the connection
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy())
        print('*** Connecting...')
        client.connect(bind_host_obj.host.ip,
                       bind_host_obj.host.port,
                       bind_host_obj.remote_user.username,
                       bind_host_obj.remote_user.password,
                       timeout=30)
        cmd_caches = []
        chan = client.invoke_shell()
        # print(repr(client.get_transport()))
        print('*** Here we go!\n')
        # 连接redis
        pool = redis.ConnectionPool(host='192.168.84.66', port=6379)
        # 传一个命令列表给redis
        user_record = [user_obj.id, bind_host_obj.id, 'login',
                       time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())]
        r = redis.Redis(connection_pool=pool)
        # 用用户名做key前缀,避免冲突
        key_name = str(user_obj.username)+'_login'
        r.lpush(key_name, user_record)
        interactive.interactive_shell(chan, user_obj, bind_host_obj, cmd_caches, log_recording)
        chan.close()
        client.close()
        # 数据库写入操作
        login_record = r.lrange(key_name, 0, -1)
        login_redis_record = login_record[0].decode().replace('[', '').replace(']', '').split(',')
        log_item = create_table.AuditLog(user_id=login_redis_record[0],
                                   bind_host_id=login_redis_record[1],
                                   action_type='login',
                                   cmd='login',
                                   date=login_redis_record[3].replace("'", ''))
        cmd_caches.append(log_item)
        log_recording(user_obj, bind_host_obj, cmd_caches)
        user_record_cmd = user_obj.username+'_user_record'
        cmd_redis_record = r.lrange(user_record_cmd, 0, -1)
        for i in cmd_redis_record:
            cmd_caches = []
            v = i.decode().replace('[', '').replace(']', '').split(',')
            v2 = v[3].replace("'", '')
            # print(v[0], v[1], v[2], v[3], v[4])
            log_item = create_table.AuditLog(user_id=v[0],
                                       bind_host_id=v[1],
                                       action_type='cmd',
                                       cmd=v2, date=v[4].replace("'", ''))
            cmd_caches.append(log_item)
            log_recording(user_obj, bind_host_obj, cmd_caches)
        # 当退出的时候将redis的值写入到数据库并且清空redis
        logout_caches = []
        logout_caches.append(create_table.AuditLog(user_id=user_obj.id,
                                             bind_host_id=bind_host_obj.id,
                                             action_type='logout',
                                             cmd='logout',
                                             date=datetime.datetime.now()))
        log_recording(user_obj, bind_host_obj, logout_caches)
        # 清空keys
        r.delete(key_name)
        r.delete(user_record_cmd)
    except Exception as e:
        print('*** Caught exception: %s: %s' % (e.__class__, e))
        traceback.print_exc()
        try:
            client.close()
        except:
            pass
        sys.exit(1)