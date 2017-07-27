# -*- coding:utf-8 -*-
# Author:D.Gray

#  key-value  键值对
info = {
    'stu1101':'TengLan Wu',
    'stu1102':'LongZe Luola',
    'stu1103':'Xiao Maliya',
}
print('*******查询字典元素*******')
print(info)
print(info['stu1101'])     #查询字典中键为'stu1101'所对应的值
#print(info['stu1104'])      #使用info[key] 方法查询字典中某一元素。只能查询字典已存在的键值对，
                            #若查询字典中不包含的键值时会报错

print(info.get('stu1104'))      #使用info.get('key')方法，若字典中已存在该元素会正常打印，若没有回返回个‘None’

print('\n*******判断字典是否存在该元素*******')
print('stu1104' in info)    #info.has_key('stu1103')   in py2

print('\n*******修改字典元素*******')
info['stu1101'] = '武藤兰'
print(info)

print('\n*******增加字典元素*******')
info['stu1104'] = '苍井空'
print(info)

print('\n*******删除字典元素*******')
del info['stu1101']
print(info)

info.pop('stu1102')
print(info)

# info.popitem()     #随机删除字典元素
# print(info)

print('\n*******  update() 使用方法')
info = {
    'stu1101':'TengLan Wu',
    'stu1102':'LongZe Luola',
    'stu1103':'Xiao Maliya',
}
b = {                               #创建一个新的字典
    'stu1101':'Alex',
    1:3,
    2:5,
}
info.update(b)   # 在info字典中 使用 update()方法合并 b 字典
print(info)      # 字典info和字典b 中都有 'stu1101'这个key。使用 update()方法后，将b字典中 'stu1101'所对应的值 'Alex'
                 # 替换字典info  'stu1101'的 'TengLan Wu'。并将b字典中 1:3 和 2:5 新增到 字典info中


print('\n*******  .items() 使用方法')
print(info.items())          # .items()方法 将字典 转成一个列表

print('\n*******  .fromekys() 使用方法')
c = dict.fromkeys([6,7,8])   #初始化一个新的字典，该字典的键就是列表中的值
print(c)
c = dict.fromkeys([6,7,8],'test')  #初始化一个新的字典，该字典的键就是列表中第一个值[6,7,8]，
print(c)                           #该字典的值就是列表中的第二个值'test'

c = dict.fromkeys([6,7,8],[1,{'name':'alex'}])   #初始化一个新字典c，该字典的key就是列表中的[6,7,8]
print(c)                                         #该字典中 每个key6,7,8所对应的值就是列表中的[1,{'name':'alex'}]\n
print('\n******更改后*****')
c[7][1]['name'] = 'Jack Chen'   #把字典c中key是7 的第二个值{'name':'alex'}中的'alex' 更改为 'Jack Chen'
print(c)                        #其实是吧字典c所有key中所对应的'alex'更改为 'Jack Chen'

print('\n*******循环字典  第一种方法******')
for i in info:           #第一种方法，比第二种方法高效 推荐使用
    print(i,info[i])
print('\n*******循环字典  第二种方法******')
for k,v in info.items():   #第二种方法，首先通过items()方法把字典转换成列表 比第一种方法多了 转换的步骤
    print(k,v)             #数据一多就会造成机器崩溃