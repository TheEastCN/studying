# -*- coding:utf-8 -*-

f  = '将进酒.txt'
old_tr = '李白'
new_str = '李太白'
f_1 = open(f,'r+',encoding='utf-8')

data = f_1.readlines()
f_1.seek(0)
f_1.truncate()

for line in data:

    if old_tr in line:
        line = line.replace(old_tr,new_str)

    f_1.write(line)

f_1.close()