# -*- coding:utf-8 -*-
# Author:D.Gray
import sqlalchemy
from Day02.ORM.orm_多外键关联 import create_table
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=create_table.engine)
session = Session_class()
# add1 = create_table.Address(street = '中春路',city = '上海',state = '上海')
# add2 = create_table.Address(street = '西湖',city = '无锡',state = '江苏')
# add3 = create_table.Address(street = '宁波路',city = '宁波',state = '杭州')
# c1 = create_table.Customer(name = 'Alex',cus_billing_address = add1,cus_shipping_address = add2)
# c2 = create_table.Customer(name = 'Jack',cus_billing_address = add3,cus_shipping_address = add3)
#
# session.add_all([add1,add2,add3,c1,c2])
# session.commit()
# print('数据创建成功')

print('多外键查询'.center(50,'-'))
data = session.query(create_table.Customer).filter(create_table.Customer.name == 'Alex').first()
print(data.name,data.cus_billing_address,data.cus_shipping_address)