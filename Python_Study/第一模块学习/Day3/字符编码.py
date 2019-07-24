#-*- Coding:utf-8 -*-    文件编码是utf-8
# Author: D.Gray
'''
ASCII：美国(国家)信息交换标准(代)码，一种使用7个或8个二进制位进行编码的方案，
最多可以给256个字符(包括字母、数字、标点符号、控制字符及其他符号)分配(或指定)数值。
GB2312：GB2312是一个简体中文字符集，由6763个常用汉字和682个全角的非汉字字符组成。
GBK：GBK即汉字内码扩展规范GBK编码标准兼容GB2312，共收录汉字21003个、
符号883个，并提供1894个造字码位，简、繁体字融于一库。
Unicode：Unicode当然是一个很大的集合，现在的规模可以容纳100多万个符号
但是它的效率不高，中英文都占2个字节
UTF-8：为了提高Unicode的编码效率，于是就出现了UTF-8编码。UTF-8可以根据不同的
符号自动选择编码的长短。比如英文字母可以只用1个字节就够了。

不同编码转换都需要通过Unicode这个中间环节，然后在将其需要的字符编码
'''

import sys
print(sys.getdefaultencoding())   #打印默认编码格式

s = '你好'
print(s.encode('gbk'))    #Python默认unicode编码 所以可直接转换为gbk
                          #将pychome文件编码变为 gbk格式会报错
                          # Non-UTF-8 code starting with
print(s.encode('utf-8').decode('utf-8').encode('gb2312'))
#decode('utf-8').encode('gb2312')将utf8编码转换为gb2312
print(s.encode('utf-8').decode('utf-8').encode('gb2312').decode('gb2312'))
#.decode('utf-8').encode('gb2312').decode('gb2312')将gb2312编码转换为字符串

print('\n----将gbk转换为utf-8')
s = '你是谁'
s_gbk = s.encode('gbk')
print(s_gbk)
gbk_to_utf8 = s_gbk.decode('gbk').encode('utf-8') #将gbk编码格式转换成utf8
#s_gbk.decode('GBK')就是将gbk转换为Unicode,然后在转换成utf-8
print('utf8编码：',gbk_to_utf8)

print('\n----将gb2312转换为utf-8')
s = '我就是'
s_gb2312 = s.encode('gb2312')
print(s_gb2312)
gb2312_to_utf8 = s_gb2312.decode('gb2312').encode('utf-8')
print('utf8编码：',gb2312_to_utf8)
