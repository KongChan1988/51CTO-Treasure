# -*- coding:utf-8 -*-
# Author:D.Gray

account = 0
age = 30
while account <3:
    for num in range(1,50):
        if num %2 ==0 and num == age:
            print(1)
        else:
            print(2)
            account += 1