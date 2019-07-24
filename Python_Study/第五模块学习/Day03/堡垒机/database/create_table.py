#-*-coding:utf-8 -*-
# Author: D.Gray
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ChoiceType
from sqlalchemy import Column,Integer,String,ForeignKey,UniqueConstraint,Table,Text,DateTime
from conf.setting import CONN

Base = declarative_base()

user_m2m_bind = Table(
    'user_m2m_bind',Base.metadata,
    Column('user_profile_id',Integer,ForeignKey('user_profile.id')),
    Column('bind_host_id',Integer,ForeignKey('bind_host.id'))
)

bind_m2m_group = Table(
    'bind_m2m_group',Base.metadata,
    Column('group_id',Integer,ForeignKey('group.group_id')),
    Column('bind_host_id',Integer,ForeignKey('bind_host.id'))
)

user_m2m_group = Table(
    'user_m2m_group',Base.metadata,
    Column('group_id',Integer,ForeignKey('group.group_id')),
    Column('user_id',Integer,ForeignKey('user_profile.id'))
)

class Host(Base):
    __tablename__ = 'host'
    host_id = Column(Integer,primary_key=True)
    host_name = Column(String(32),unique=True)
    IP = Column(String(32),nullable=False,unique=True)
    port = Column(Integer,default=22)

    def __repr__(self):
        return '<名称：【%s】    IP：【%s】     port：【%s】>'%(self.host_name,self.IP,self.port)

class Group(Base):
    __tablename__ = 'group'
    group_id = Column(Integer,primary_key=True)
    group_name = Column(String(32),nullable=False,unique=True)
    group_bind = relationship('BindHost',secondary = 'bind_m2m_group',backref = 'groups_key')

    def __repr__(self):
        return '<组名：【%s】>'%(self.group_name)

class RemUser(Base):
    '''
    远程登录用户
    '''
    __tablename__ = 'rem_user'
    __table_args__ = (UniqueConstraint('auth_type','username','password',name = 'rems_uc'),)
    id = Column(Integer,primary_key=True)
    Auth_types = [
        ('ssh-password','SSH/Password'),
        ('ssh-key','SSH/Key'),
    ]
    auth_type = Column(ChoiceType(Auth_types))
    username = Column(String(32),nullable=False)
    password = Column(String(32))

    def __repr__(self):
        return '<名称：【%s】    密码：【%s】     验证方式：【%s】>'%(self.username,self.password,self.auth_type)

class BindHost(Base):
    '''
    此表是用来实现操控主机IP 和 登录用户 之间的绑定关系
        IP                                             远程登录名
    192.168.111.128                                       root
    192.168.111.129                                       admin_kyo
    host_id                                               remuser_id
    '''
    __tablename__ = 'bind_host'
    __table_args__ = (UniqueConstraint('remuser_id','host_id',name = 'binds_uc'),)
    id = Column(Integer,primary_key=True)
    remuser_id = Column(Integer,ForeignKey('rem_user.id'),nullable=False)
    host_id = Column(Integer,ForeignKey('host.host_id'),nullable=False)
    bind_hosts = relationship('Host',backref = 'bind_hosts')
    bind_remusers = relationship('RemUser',backref = 'bind_remusers')

    def __repr__(self):
        return '<IP：【%s】    远程登录名：【%s】>'\
               %(self.bind_hosts.IP,self.bind_remusers.username)

class UserProfile(Base):
    '''
    堡垒机用户
    '''
    __tablename__ = 'user_profile'
    id = Column(Integer,primary_key=True)
    user_name = Column(String(32),nullable=False)
    password = Column(String(32),nullable=False)
    profile_bind = relationship('BindHost',secondary = 'user_m2m_bind',backref = 'user_profiles')
    profile_group = relationship('Group',secondary = 'user_m2m_group',backref = 'profile_groups')

    def __repr__(self):
        return '<名称：【%s】    密码：【%s】>'\
               %(self.user_name,self.password)

class AuditLog(Base):
    '''
    用户操作日志表
    '''
    __tablename__ = 'audit_log'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_profile.id'))
    bind_host_id = Column(Integer, ForeignKey('bind_host.id'))
    action_choices = [
        (u'cmd', u'CMD'),
        (u'login', u'Login'),
        (u'logout', u'Logout'),
    ]

    action_type = Column(ChoiceType(action_choices))
    # 命令可能存的数值更大
    # cmd = Column(String(255))
    cmd = Column(Text(65535))
    date = Column(DateTime)

    user_profile = relationship("UserProfile")
    bind_host = relationship("BindHost")

