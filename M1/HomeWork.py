# -*- coding:utf-8 -*-

import os

user_dict = {'zhangsan': 'abcd', 'lisi': '1234', 'wangwu': 'ww123'}
count = 0
user_status = {}

if os.path.exists('user_status.file') is False:
    file_create = open('user_status.file', 'w+', encoding='utf-8')
    for i in user_dict:
        user_status[i] = 'Unlock'
    file_create.write(str(user_status))

else:
    file_create = open('user_status.file', 'r+', encoding='utf-8')
    user_status = eval(file_create.readline())


while count < 3:
    username = input("Please input you username:").strip()
    password = input("Please input you password:").strip()

    if username in user_dict.keys() and password == user_dict[username]:

        if len(user_status) > 0:
            if user_status[username] == 'Locked':
                print('\033[1;31m 用户状态已锁定,请联系Administrator解锁 \033[0m')
            else:
                print(
                    "Welcome \033[1;42m %s \033[0m login system !" %
                    username)
        else:
            print("Welcome %s login system !" % username)
        break

    else:
        print("User/Password entered is invalid. Please try again.")
        if count == 2:
            user_status[username] = 'Locked'
            file_create.write(str(user_status))

    count = count + 1
