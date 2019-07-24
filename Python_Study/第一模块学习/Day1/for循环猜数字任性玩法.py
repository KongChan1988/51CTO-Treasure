# -*- coding:utf-8 -*-
# Author:D.Greay
age_of_oldboy = 56
i = 0
for i in range(3):
    guess_age = int(input('Guess age: '))
    if guess_age == age_of_oldboy:
        print('Yes, you got it.')
        break
    elif guess_age < age_of_oldboy:
        print('Think smaller...！')
    else:
        print('Think bigger...!')
    if i == 3:
        countine_confirm = input('Do you have want to keep guessing...?')
        if countine_confirm != 'n':
            i == 0