# -*- coding:utf-8 -*-

import re

with open("tongji.txt",'r',encoding='utf-8') as re_file:
    data = re_file.read()
    re_file.seek(0)
    data_1 = re_file.readline()
    re_file.seek(0)
    data_2 = re_file.readlines()
    
    re_file.seek(0)
    for line in re_file:
        re_s = re.search('\w+\.com',line)
        if re_s:
            print(re_s.group())

    print(data,'type(data)',type(data))
    print("---------------------------")
    print(data_1,'type(data_1)', type(data_1))
    print("---------------------------")
    print(data_2,'type(data_2)', type(data_2))