# -*- coding:utf-8 -*-
# Author:D.Greay
age_of_oldboy = 56
count = 0   #定义一个循环次数变量count
while count < 3:
    guess = int(input('Guess age: '))
    if guess == age_of_oldboy:
        print('Yes, you got it.')
        break
    elif guess > age_of_oldboy:
        print('Thinke smaller...')
    else:
        print('Think bigger!')
    count +=1
else:
    print('You have tried too many times...fuck off')


 # print('count:' , count)
    # count +=1
