# -*- coding:utf-8 -*-

import json,pickle

data = {'d1': {'role': 'aaaa'}}
# a = json.dumps(data)
# print(a, type(a))
#
# b = json.loads(a)
# print(b, type(b))
#
data2 = {'d1': {'role': 'aaaa'}}
f = open('test.json', 'wb', encoding='utf-8')
c = json.dump(data, f)
f.close()
# print(c, type(c))
# g = open('test.json', 'r', encoding='utf-8')
# d = json.load(g)
# print(d)

f_b = open('test.pickel','wb')
a = pickle.dump(data,f_b)
f_b.close()

r_b = open('test.pickel','rb')
a = pickle.load(r_b)
r_b.close()
print(a)

b = pickle.dumps(data)
print(b,type(b))
c = pickle.loads(b)
print(c)