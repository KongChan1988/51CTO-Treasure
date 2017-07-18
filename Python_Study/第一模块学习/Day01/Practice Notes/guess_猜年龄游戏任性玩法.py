# -*- coding:utf-8 -*-
# Author:D.Greay
age_of_oldboy = 56
count = 0
while count < 3:
    guess_age = int(input('Guess age:'))
    if guess_age == age_of_oldboy:
        print('Yes, you got it.')
        break
    elif guess_age < age_of_oldboy:
        print('Think smaller...！')
    else:
        print('Think bigger...!')
    count += 1
    if count == 3:  #如果count=3的时候  给出一个输入反馈
        countine_confirm = input('Do you want to keep guessing...')
        if countine_confirm != 'n': #如果输入不是n 则重置count=0   继续重置循环
            count = 0

