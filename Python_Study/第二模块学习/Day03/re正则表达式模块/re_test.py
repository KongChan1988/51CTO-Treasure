#-*- Coding:utf-8 -*-
# Author: D.Gray

'''
常用正则表达式符号
'.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
'^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
'$'     匹配字符结尾，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以
'*'     匹配*号前的字符0次或多次，re.findall("ab*","cabb3abcbbac")  结果为['abb', 'ab', 'a']
'+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
'?'     匹配前一个字符1次或0次
'{m}'   匹配前一个字符m次
'{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
'|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
'(...)' 分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456c

'\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
'\Z'    匹配字符结尾，同$
'\d'    匹配数字0-9
'\D'    匹配非数字
'\w'    匹配[A-Za-z0-9]
'\W'    匹配非[A-Za-z0-9]
's'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'
'(?P<name>...)' 分组匹配 re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city")
结果{'province': '3714', 'city': '81', 'birthday': '1993'}
例：匹配字符是否数子开头数子结尾
re.search("\d.*\d$","需要匹配的字符串").group()   \d\Z或\d$
'''
import re

a = re.findall("\D+","adj2jj23 jjsajkdjajeiuij") #将所有非数字筛选出来
print(a)   #['adj', 'jj', ' jjsajkdjajeiuij']

c = re.sub("\d+","&","adj2jj23 jjsa j234jaj43eiuij" ,count=3) #将所有非数字筛选出来，并将数字以"&"符号显示，执行count次
print(c)   #adj&jj& jjsa j&jaj43eiuij

d = re.split("\\\\",r"c:\\users\data\python35")
print(d)  #['c:', '', 'users', 'data', 'python35']

b = re.search("(\d{1,3}\.){3}\d{3}",
              '''
                默认网关. . . . . . . . . . . . . : 192.168.1.1
                IPv4 地址 . . . . . . . . . . . . : 192.168.1.113
                子网掩码  . . . . . . . . . . . . : 255.255.255.0
                默认网关. . . . . . . . . . . . . : 192.168.1.1''',flags=re.M).group()
print(b)    #192.168.1.113

