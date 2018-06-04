# -*- coding:utf-8 -*-

tup1 = ('Google', 'Runoob', 1997, 2000)

tup2 = ('wyd',) #元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
print(type(tup2))


set1 = {'wyd','hello'}
print(type(set1))


dict_f = {'addr':'beijing','hometown':'heibei'}

key1 = dict_f.keys()['addr']
print(key1)