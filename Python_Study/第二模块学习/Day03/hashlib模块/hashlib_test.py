#-*- Coding:utf-8 -*-
# Author: D.Gray
import hashlib

print('hashlib.md5'.center(50,'-'))
m = hashlib.md5()
m.update(b"Hello")
print(m.hexdigest())
m.update(b"It's me")
print(m.hexdigest())
#m.update(b"It's been a long time since we spoken....")
m2 = hashlib.md5()
m2.update(b"HelloIt's me")  #验证 m是不是"HelloIt's me"
print(m2.hexdigest())

print('hashlib.sha1'.center(50,'-'))
s = hashlib.sha1()
s.update(b"HelloIt's me")   #通过sha1方法加密 "HelloIt's me"
print(s.hexdigest())

s2 = hashlib.sha1()
s2.update(b"HelloIt's me")
print(s2.hexdigest())


print('hashlib.sha512'.center(50,'-'))
x = hashlib.sha512()
x.update("天王盖地虎".encode(encoding='utf-8'))   #通过sha1方法加密 "HelloIt's me"
print(x.hexdigest())

x2 = hashlib.sha512()
x2.update("天王盖地虎".encode(encoding='utf-8'))
print(x2.hexdigest())

print('hmac.new()'.center(50,'-'))
import hmac
h = hmac.new(b"12345","你是 250".encode(encoding='utf-8'))
#print(h.digest())
print(h.hexdigest())  #16进制加密显示

