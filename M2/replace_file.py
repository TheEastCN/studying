# -*- coding:utf-8 -*-

import os

f = open('静夜思.txt', 'r+', encoding='utf-8')
f_new = open('静夜思new.txt', 'w', encoding='utf-8')
old_str = '疑是地上霜'
new_str = '地上鞋两双'

# data = f.readlines()
# print(data)
for line in f:

    if old_str in line:
        line=line.replace(old_str,new_str)
        f_new.write(line)
    else:
        f_new.write(line)
    print(line, type(line))
f.close()
f_new.close()

os.remove('静夜思.txt')
os.rename('静夜思new.txt','静夜思.txt')
