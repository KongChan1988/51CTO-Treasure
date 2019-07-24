# -*- coding:utf-8 -*-
# Author:D.Greay
age_of_oldbody = 56
for i in range(3):
    guess_age = int(input('Guess age: '))
    if guess_age == age_of_oldbody:
        print('Yes, you got it.')
        break
    elif guess_age < age_of_oldbody:
        print('Think smaller...！')
    else:
        print('Think bigger...!')
else:
    print('You have tried too many times...fuck off ')