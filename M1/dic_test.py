# -*- coding:utf-8 -*-

dic_a = {'name': 'wyd', 'age': 22, 'Job': 'IT'}

# clear 删除字典内所有元素
dic_a.clear()
print(dic_a)

# copy 浅复制
dic_b = {'name': 'wyd', 'age': 22, 'Job': ['IT','HR']}
a = dic_b.copy()
print(dic_b,a)
dic_b['Job'] = ['IT','HR','CEO']
print(id(dic_b),id(a))
print(id(dic_b['Job']),id(a['Job']))

# fromkeys 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
b = dict.fromkeys([1,2,3],'y')
print(b)

# get(key, default=None)返回指定键的值，如果值不在字典中返回default值

print(dic_b.get('name'))
print(dic_b.get('hello','hi')) # 当key不在字典中时，返回指定数据，默认为none

# in       key in dict 检查键是否在字典中

print('wyd' in dic_b ) # False

# items 以列表返回可遍历的(键, 值) 元组数组

dict_d = {'Name': 'Runoob', 'Age': 7}
for i,j in dict_d.items():
    print(i, ":\t", j)

# keys 以列表返回一个字典所有的键
print(dict_d.keys()) #print(dict_d.keys()) #

#pop(key[,default]) 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值

print(dic_b.pop('name'))

# popitem 随机返回并删除字典中的一对键和值。如果字典已经为空，却调用了此方法，就报出KeyError异常。

print(dict_d.popitem())

# setdefault(key, default=None)  和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default

print(dict_d.setdefault('爱好','无'))

# update 把字典dict2的键/值对更新到dict里

dict_f = {'addr':'beijing','hometown':'heibei'}

dict_d.update(dict_f)
print(dict_d)

# values 以列表返回字典中的所有值

print(dict_d.values())
#  'pop', 'popitem', 'setdefault', 'update', 'values'