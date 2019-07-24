#-*-coding:utf-8 -*-
# Author: D.Gray
from database import create_table
from pymysql.err import IntegrityError
from conf import setting
from modules.utils import print_err, yaml_parser
from modules.db_conn import engine, session
from modules import ssh_login
from modules import common_filters
import codecs,os

def syncdb(argvs):
    '''
    创建表结构方法
    :param argvs:
    :return:
    '''
    print("Syncing DB....")
    engine = create_table.create_engine(setting.CONN, echo=True)
    create_table.Base.metadata.create_all(engine)  # 创建所有表结构

def create_hosts(argvs):
    '''
    create 主机
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        # 指定一个文件名否则报错
        hosts_file = argvs[argvs.index("-f") +1]
        host_path = os.path.join(setting.BASE_DESC,hosts_file)
        #print('hosts_path:',host_path)
    else:
        print_err("invalid usage, should be:\ncreate_hosts -f <the new hosts file>", quit=True)
    source = yaml_parser(host_path)  # 传文件回来
    if source:  # 循环字典
        print(source)
        for key, val in source.items():
            print(key, val)
            obj = create_table.Host(host_name=key, IP=val.get('ip'), port=val.get('port') or 22)
            # 添加到表
            try:
                session.add(obj)
            except IntegrityError as e:
                print('主机名和主机IP是唯一值已在数据库创建:',e)
            else:
                session.commit()

def create_remoteusers(argvs):
    '''
    create 远程用户数据
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        remoteusers_file = argvs[argvs.index("-f") +1]
        host_path = os.path.join(setting.BASE_DESC, remoteusers_file)
    else:
        print_err("invalid usage, should be:\ncreate_remoteusers -f <the new remoteusers file>", quit=True)
    source = yaml_parser(host_path)
    if source:
        for key, val in source.items():
            print(key, val)
            obj = create_table.RemUser(username=val.get('username'), auth_type=val.get('auth_type'),
                                    password=val.get('password'))
            session.add(obj)
        session.commit()

def create_users(argvs):
    '''
    create 堡垒机用户数据
    create little_finger access user.txt
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        user_file = argvs[argvs.index("-f") +1 ]
        host_path = os.path.join(setting.BASE_DESC, user_file)
    else:
        print_err("invalid usage, should be:\ncreateusers -f <the new users file>",quit=True)

    source = yaml_parser(host_path)
    if source:
        for key, val in source.items():
            print(key, val)
            obj = create_table.UserProfile(user_name=key, password=val.get('password'))
            if val.get('groups'):
                groups = session.query(create_table.Group).\
                    filter(create_table.Group.group_name.in_(val.get('groups'))).all()
                if not groups:
                    print_err("none of [%s] exist in group table." % val.get('groups'), quit=True)
                obj.groups = groups
            if val.get('bind_hosts'):
                bind_hosts = common_filters.bind_hosts_filter(val)
                obj.bind_hosts = bind_hosts
            #print(obj)
            session.add(obj)
        session.commit()

def create_groups(argvs):
    '''
    create 组数据
    create groups
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        group_file = argvs[argvs.index("-f") + 1]
        host_path = os.path.join(setting.BASE_DESC, group_file)
    else:
        print_err("invalid usage, should be:\ncreategroups -f <the new groups file>", quit=True)
    source = yaml_parser(host_path)
    if source:
        for key, val in source.items():
            print(key, val)
            obj = create_table.Group(group_name=key)
            if val.get('bind_hosts'):
                bind_hosts = common_filters.bind_hosts_filter(val)
                obj.bind_hosts = bind_hosts

            if val.get('user_profiles'):
                user_profiles = common_filters.user_profiles_filter(val)
                obj.user_profiles = user_profiles
            session.add(obj)
        session.commit()

def create_bindhosts(argvs):
    '''
    create IP和远程用户关联数据
    create bind hosts
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        bindhosts_file = argvs[argvs.index("-f") + 1]
        host_path = os.path.join(setting.BASE_DESC, bindhosts_file)
    else:
        print_err("invalid usage, should be:\ncreate_hosts -f <the new bindhosts file>",quit=True)
    source = yaml_parser(host_path)
    if source:
        for key, val in source.items():
            print(key, val)
            # 获取到了主机
            host_obj = session.query(create_table.Host).\
                filter(create_table.Host.host_name == val.get('host_name')).first()
            # 取hostname
            assert host_obj  # 断言，必须存在
            for item in val['remote_users']:  # 判断
                print(item)
                assert item.get('auth_type')
                if item.get('auth_type') == 'ssh-password':  # 判断认证password
                    remoteuser_obj = session.query(create_table.RemUser).filter(
                        create_table.RemUser.username == item.get('username'),
                        create_table.RemUser.password == item.get('password')
                                                    ).first()
                else:
                    # 获取远程用户
                    remoteuser_obj = session.query(create_table.RemUser).filter(
                        create_table.RemUser.username == item.get('username'),
                        create_table.RemUser.auth_type == item.get('auth_type'),
                                                    ).first()
                if not remoteuser_obj:  # 没取到,程序退出
                    print_err("RemoteUser obj %s does not exist." % item, quit=True)
                bindhost_obj = create_table.BindHost(host_id=host_obj.host_id, remuser_id=remoteuser_obj.id)
                session.add(bindhost_obj)  # 获取到关系后添加session
                # for groups this host binds to
                if source[key].get('groups'):  # 获取组
                    group_objs = session.query(create_table.Group).filter(create_table.Group.group_name.in_
                                                                        (source[key].get('groups'))).all()
                    assert group_objs
                    print('groups:', group_objs)
                    bindhost_obj.host_groups = group_objs
                # for user_profiles this host binds to
                if source[key].get('user_profiles'):  # 判断是否直接属于哪一台机器
                    userprofile_objs = session.query(create_table.UserProfile).\
                        filter(create_table.UserProfile.user_name.in_(
                        source[key].get('user_profiles')
                    )).all()
                    assert userprofile_objs
                    print("userprofiles:", userprofile_objs)
                    bindhost_obj.user_profiles = userprofile_objs
                # print(bindhost_obj)
        session.commit()

def auth():
    '''
    用户验证
    do the user.txt login authentication
    :return:
    '''
    count = 0
    while count < 3:
        username = input("\033[32;1mUsername>>>:\033[0m").strip()
        if len(username) == 0:
            continue
        password = input("\033[32;1mPassword>>>:\033[0m").strip()
        if len(password) == 0:
            continue
        user_obj = session.query(create_table.UserProfile).filter(create_table.UserProfile.user_name == username,
                                                                  create_table.UserProfile.password == password).first()
        if user_obj:
            return user_obj
        else:
            print("wrong username or password, you have %s more chances." % (3-count-1))
            count += 1
    else:
        print_err("too many attempts.")

def welcome_msg(user):
    '''
    :param user: 接收start_session函数的user
    :return:
    '''
    WELCOME_MSG = '''\033[32;1m
    ------------- Welcome [%s] login TinyServer -------------
    \033[0m''' % user.user_name
    print(WELCOME_MSG)

def start_session(argvs):
    '''
    开始远程登陆函数
    :param argvs:
    :return:
    '''
    print('going to start sesssion ')
    user = auth()               #调用auth认证函数 来判断输入的堡垒机用户是否存在
    if user:
        welcome_msg(user)
        # print(user.txt.bind_hosts)
        # print(user.txt.host_groups)
        exit_flag = False
        while not exit_flag:
            if user.profile_bind:
                # 显示未分组的机器
                print('\033[32;1mz.\t z查看未分组主机列表/任意键查看已分组主机列表 (%s)\033[0m' % len(user.profile_bind))
            for index, group in enumerate(user.profile_group):
                print('\033[32;1m%s.\t%s (%s)\033[0m' % (index, group.group_name, len(group.group_bind)))
            # 用户输入
            choice = input("[%s]:" % user.user_name).strip()
            if len(choice) == 0:
                continue
            # 如果是z 打印未分组机器
            if choice == 'z':
                print("------ Group: 未分组主机 ------")
                for index, bind_host in enumerate(user.profile_bind):
                    print("  %s.\t%s@%s(%s)" % (index,
                                                bind_host.bind_remusers.username,
                                                bind_host.bind_hosts.host_name,
                                                bind_host.bind_hosts.IP,
                                                ))
                print("----------- END -----------")
            elif choice.isdigit():  # 打印分组的机器
                choice = int(choice)
                if choice < len(user.profile_group):
                    print("------ Group: %s ------" % user.profile_group[choice].group_name)
                    for index, bind_host in enumerate(user.profile_group[choice].group_bind):
                        print("  %s.\t%s@%s(%s)" % (index,
                                                    bind_host.bind_remusers.username,
                                                    bind_host.bind_hosts.host_name,
                                                    bind_host.bind_hosts.IP,
                                                    ))
                    print("----------- END -----------")

                    # host selection 选择机器去登陆
                    while not exit_flag:
                        user_option = input("[(b)back, (q)quit, select host to login]:").strip()
                        if len(user_option) == 0:
                            continue
                        if user_option == 'b':
                            break
                        if user_option == 'q':
                            exit_flag = True
                        if user_option.isdigit():
                            user_option = int(user_option)
                            if user_option < len(user.host_groups[choice].bind_hosts):
                                print('host:', user.host_groups[choice].bind_hosts[user_option])
                                # print('audit log:', user.txt.host_groups[choice].bind_hosts[user_option].audit_logs)
                                ssh_login.ssh_login(user,  # 传用户,用户组,连上对应的
                                                    user.host_groups[choice].bind_hosts[user_option],
                                                    session, log_recording)
                else:
                    print("no this option..")

def log_recording(user_obj, bind_host_obj, logs):
    '''
    flush user.txt operations on remote host into DB
    :param user_obj:
    :param bind_host_obj:
    :param logs: list format [logItem1,logItem2,...]
    :return:
    '''
    # print("\033[41;1m--logs:\033[0m", logs)
    session.add_all(logs)
    session.commit()
def user_record_cmd(argvs):
    '''
    查看操作记录方法
    :param argvs:
    :return:
    '''
    print('going to start view record')
    user = auth()
    # 默认root可以查所有人的记录
    if user.username == 'root':
        print('welcome %s ' % user.username)
        exit_flag = False
        # 用户对象
        user_obj = session.query(create_table.UserProfile).filter().all()
        # 循环查看堡垒机用户操作
        while not exit_flag:
            for user_profile_list in user_obj:
                # 打印堡垒机用户，根据堡垒机用户ID选择其管辖的机器并打印日志
                print("%s.\t%s" % (user_profile_list.id, user_profile_list.username))
            choice = input("[%s]:" % user.username).strip()
            for user_profile_list in user_obj:
                if str(choice) == str(user_profile_list.id):
                    if user_profile_list.bind_hosts:
                        # 显示未分组的机器
                        print('\033[32;1mz.\tungroupped hosts (%s)\033[0m' % len(user_profile_list.bind_hosts))
                    else:
                        print(' no binding groups ')
                    for index, group in enumerate(user_profile_list.host_groups):
                        print('\033[32;1m%s.\t%s (%s)\033[0m' % (index, group.group_name, len(group.bind_hosts)))
                    choice = input("[%s]:" % user.user_name).strip()
                    if choice.isdigit():  # 打印分组的机器
                        choice = int(choice)
                        if choice < len(user_profile_list.host_groups):
                            print("------ Group: %s ------" % user_profile_list.host_groups[choice].name)
                            for index, bind_host in enumerate(user_profile_list.host_groups[choice].bind_hosts):
                                print("  %s.\t%s@%s(%s)" % (index,
                                                            bind_host.remote_user.user_name,
                                                            bind_host.host.host_name,
                                                            bind_host.host.IP,
                                                            ))
                            print("----------- END -----------")
                            # host selection 选择机器去查看操作信息
                            while not exit_flag:
                                user_option = input("[(b)back, (q)quit, select host to login]:").strip()
                                if len(user_option) == 0:
                                    continue
                                if user_option == 'b':
                                    break
                                if user_option == 'q':
                                    exit_flag = True
                                if user_option.isdigit():
                                    user_option = int(user_option)
                                    if user_option < len(user_profile_list.host_groups[choice].bind_hosts):
                                        # print('host:', user_profile_list.host_groups[choice].bind_hosts[user_option])
                                        data = \
                                            session.query(create_table.AuditLog).filter(
                                                create_table.AuditLog.user_id == user_profile_list.id,
                                                create_table.AuditLog.bind_host_id == user_profile_list.host_groups[choice].
                                                bind_hosts[user_option].id).all()
                                        if data:
                                            for index, i in enumerate(data):
                                                # redis 写入value的时候带有了\t \n 等需要转义
                                                # 第一个注释从数据库里读注释的这种不能转移\t,
                                                # 第二个和现行的俩种中文转义有些问题
                                                # print(i.user_id, i.bind_host_id, i.action_type, i.cmd, i.date)
                                                # print(i.user_id, i.bind_host_id, i.action_type,
                                                #        codecs.getdecoder("unicode_escape")(i.cmd)[0], i.date)
                                                # print(i.user_id, i.bind_host_id, i.action_type,
                                                #       i.cmd.encode().decode('unicode-escape'), i.date)
                                                print(index, i.date, i.cmd.encode().decode('unicode-escape'))
                                        else:
                                            print('no record in host:', user_profile_list.host_groups[choice].
                                                  bind_hosts[user_option])
    # 其他人只能查自己的操作记录
    else:
        exit_flag = False
        while not exit_flag:
            if user.bind_hosts:
                # 显示未分组的机器
                print('\033[32;1mz.\tungroupped hosts (%s)\033[0m' % len(user.bind_hosts))
            for index, group in enumerate(user.host_groups):
                print('\033[32;1m%s.\t%s (%s)\033[0m' % (index, group.group_name, len(group.bind_hosts)))
            choice1 = input("[%s]:" % user.user_name).strip()
            # 查询选项
            if choice1 == 'z':
                print("------ Group: ungroupped hosts ------")
                for index, bind_host in enumerate(user.bind_hosts):
                    print("  %s.\t%s@%s(%s)" % (index,
                                                bind_host.remote_user.username,
                                                bind_host.host.hostname,
                                                bind_host.host.ip,
                                                ))
                print("----------- END -----------")
            elif choice1.isdigit():  # 打印分组的机器
                choice = int(choice1)
                if choice < len(user.host_groups):
                    print("------ Group: %s ------" % user.host_groups[choice].name)
                    for index, bind_host in enumerate(user.host_groups[choice].bind_hosts):
                        print("  %s.\t%s@%s(%s)" % (index,
                                                    bind_host.remote_user.user_name,
                                                    bind_host.host.host_name,
                                                    bind_host.host.IP,
                                                    ))
                    print("----------- END -----------")

                    # host selection 选择机器去查看操作信息
                    while not exit_flag:
                        user_option = input("[(b)back, (q)quit, select host to view record]:").strip()
                        if len(user_option) == 0:
                            continue
                        if user_option == 'b':
                            break
                        if user_option == 'q':
                            exit_flag = True
                        if user_option.isdigit():
                            user_option = int(user_option)
                            if user_option < len(user.host_groups[choice].bind_hosts):
                                data = session.query(create_table.AuditLog)\
                                    .filter(create_table.AuditLog.user_id == user.id,
                                            create_table.AuditLog.bind_host_id == user.host_groups[choice].
                                            bind_hosts[user_option].id).all()
                                # print(user.txt.host_groups[choice].bind_hosts[user_option].id)
                                if data:
                                    for index, i in enumerate(data):
                                        print(index, i.date, i.cmd.encode().decode('unicode-escape'))
                                else:
                                    print('no record in host:', user.host_groups[choice].bind_hosts[user_option])
                else:
                    print("no this option..")