#-*-coding:utf-8 -*-
# Author: D.Gray
from modules import views

actions = {
    'start_session': views.start_session,  # 连接server
    # 'stop': views.stop_server,
    'syncdb': views.syncdb,  # 同步数据
    'create_users': views.create_users,  # 创建users
    'create_groups': views.create_groups,  # 创建组
    'create_hosts': views.create_hosts,  # 创建主机
    'create_bindhosts': views.create_bindhosts,  # 创建绑定关系
    'create_remoteusers': views.create_remoteusers,  # 创建远程用户
    'view_user_record': views.user_record_cmd  # 查看用户操作命令
}