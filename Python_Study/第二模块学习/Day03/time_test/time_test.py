#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
标准库：
1.time 与 datetime
a.时间戳           time.time()方法 ----> 1970年1月1日到现在的秒数
b.格式化时间       2017-11-24  14:35:34
c.元组(struct_time)   time.localtime()
UTC(世界协调时)---->格林威治天文时间，世界标准时间。在中国UTC+8
DST---->夏令时
time.gmtime()-----> 把当地时间戳转换成UTC时间
time.localtime()---->把当地时间戳转化成本地时间 以 元组形式显示
'''

import time,datetime
'''
时间戳转换成元组
'''
x = time.localtime()  #可获取当前、过去、未来的时间戳时间
print(x)
print('时间戳转换成元组：%s年%s月'%(x.tm_year,x.tm_mon))
#print(help(x))

'''
元组转换成时间戳
'''
mt = time.mktime(x)
print('元组转换成时间戳：%s'%mt)


'''
时间戳转换成特定时间格式字符串
strftime("格式",struct_time) -----> 格式化的字符串
strptime("格式化字符串","格式")-----struct_time
'''
stime = time.strftime('%Y/%m/%d  %H:%M:%S',x)  # %Y = x.tm_year  ...
print('时间戳转换成特定时间格式字符串：%s'%stime)

sdtime = time.strptime('2017/11/25  15:54:52','%Y/%m/%d  %H:%M:%S')
#('2017/11/25  15:54:52','%Y/%m/%d  %H:%M:%S')  位置关系必须一一对应
print('时间格式字符串转换成struct_time：%s'%str(sdtime))

'''
将当前时间元组转化成 asctime："星期几/月份/ 几号  时分秒  年份"格式
'''
atime = time.asctime()  # 不赋值则取本地当前时间
print('将当前时间转化成 asctime时间格式：%s'%atime)

'''
将当前时间戳转化成 asctime："星期几/月份/ 几号  时分秒  年份"格式
'''
actime = time.ctime()
print('将当前时间戳转化成 asctime：%s'%actime)


'''
datetime模块
datetime.datetime.now():获取当前时间
datetime.datetime.now() + datatime.timedelta(3):当天3天后时间
datetime.datetime.now() + datatime.timedelta(-3):当天3天前时间
datetime.datetime.now() + datatime.timedelta(hours = 3):当天时间后3小时
datetime.datetime.now() + datatime.timedelta(hours = -3):当天时间前3小时
datetime.datetime.now() + datatime.timedelta(minutes = 30):当天时间后30分钟
datetime.datetime.now() + datatime.timedelta(minutes = -30):当天时间前30分钟
'''
print('获取当前时间：%s'%datetime.datetime.now())

befort_day = datetime.datetime.now() + datetime.timedelta(3)
print('当天后3天时间：%s'%befort_day)

after_day = datetime.datetime.now() + datetime.timedelta(-3)
print('当天前3天时间：%s'%after_day)

befort_hours = datetime.datetime.now() + datetime.timedelta(hours=3)
print('当天时间后3小时：%s'%befort_hours)

after_hours = datetime.datetime.now() + datetime.timedelta(hours=-3)
print('当天时间前3小时：%s'%after_hours)







