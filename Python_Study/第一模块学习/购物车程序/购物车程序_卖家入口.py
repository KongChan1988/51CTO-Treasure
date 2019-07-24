# -*- coding:utf-8 -*-
# Author:D.Gray

seller_shop =  open('porduct_shop','a',encoding='utf-8')
seller_shop.write('小学生皮肤'+'\t')             #卖家添加商品名称
seller_shop.write('80' + '\n')                   #卖家添加商品价格信息
seller_shop.flush()