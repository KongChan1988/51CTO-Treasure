#-*- Coding:utf-8 -*-
# Author: D.Gray

import  getpass
username = 'kyo'
password = 'admin1988'
count = 0
while count < 3:
    guess_username = input('Please enter the username:  ')
    guess_password = input('Please enter the password:  ')
    if guess_username == username and guess_password == password:
        print('Welcom {name} Login: '.format(name = username.title()))
        break
    elif guess_username != username or guess_username == '' or guess_username == ' ':
        print('Username error ')
    else:
        print('Password error')

    count += 1
    if count == 3:
        continue_guessing = input('You have been kepping:')
        if continue_guessing != 'n':
            count = 0

