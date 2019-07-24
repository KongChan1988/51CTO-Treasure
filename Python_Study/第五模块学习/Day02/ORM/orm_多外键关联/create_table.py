# -*- coding:utf-8 -*-
# Author:D.Gray
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import Column,String,Integer,ForeignKey

engine = create_engine('mysql+pymysql://root:admin1988@localhost/18girls?charset=utf8')
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer,primary_key=True)
    name = Column(String(64),nullable=False)
    billing_address_id = Column(Integer,ForeignKey('address.id'),nullable=False)
    shipping_address_id = Column(Integer,ForeignKey("address.id"),nullable=False)

    #多外键关联时customer表能通过cus_billing_address和cus_shipping_address查找到 address表中数据
    #address表通过billing_address_id和shipping_address_id反向查 customer表钟数据前
    #必须通过foreign_keys方法 将billing_address_id和shipping_address_id绑定相应的 address_id
    cus_billing_address = relationship('Address',foreign_keys = [billing_address_id])
    cus_shipping_address = relationship('Address',foreign_keys = [shipping_address_id])
    def __repr__(self):
        return self.name

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer,primary_key=True)
    street = Column(String(64),nullable=False)
    city = Column(String(64),nullable=False)
    state = Column(String(64),nullable=False)

    def __repr__(self):
        return '街道:%s 城市:%s'%(self.street,self.city)

Base.metadata.create_all(engine)
print('创建表成功')