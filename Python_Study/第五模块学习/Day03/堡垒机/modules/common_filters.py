#-*-coding:utf-8 -*-
# Author: D.Gray
from database import create_table
from modules.db_conn import engine, session
from modules.utils import print_err

def bind_hosts_filter(vals):
    '''

    :param vals:
    :return:
    '''
    print('**>', vals.get('bind_hosts'))
    bind_hosts = session.query(create_table.BindHost).\
        filter(create_table.Host.host_name.in_(vals.get('bind_hosts'))).all()
    if not bind_hosts:
        print_err("none of [%s] exist in bind_host table." % vals.get('bind_hosts'), quit=True)
    return bind_hosts

def user_profiles_filter(vals):
    '''

    :param vals:
    :return:
    '''
    user_profiles = session.query(create_table.UserProfile).filter(create_table.UserProfile.user_name.
                                                                   in_(vals.get('user_profiles'))).all()
    if not user_profiles:
        print_err("none of [%s] exist in user_profile table." % vals.get('user_profiles'), quit=True)
    return user_profiles