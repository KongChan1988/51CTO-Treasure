# -*- coding:utf-8 -*-
# Author:D.Greay

age_of_oldboy = 56

guess_age = int(input('guess age: '))

if guess_age == age_of_oldboy:
    print('Yes, you got it.')
elif guess_age > age_of_oldboy:
    print('Thinke smaller...')
else:
    print('Think bigger!')