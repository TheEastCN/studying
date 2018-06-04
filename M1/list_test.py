# -*- coding:utf-8 -*-

a = [1, 2, 3, 4]

b = a

c = a.copy()
print(b, a, c)
a[1] = 5
print(b, a, c)

a[3] = [6,7,8]
d = a.copy()
print(b, a, d)

a[3][1] = ['x','y','z']
print(b, a, d)


li_a = ['a','b','c']
li_a.append('d')
print(li_a)

# pop 删除列表中的最后一个元素,并将删除元素进行返回str类型
print(type(li_a.pop()))
print(li_a)

#count  统计列表中元素出现的次数，返回int类型
li_a.append('b')
print(li_a.count('b'),type(li_a.count('b')))

#insert 在所指定的索引下进行元素插入操作，原来的元素向后移位
li_a.insert(1,'x')
print(li_a)

#reverse 将列表进行翻转
li_a.reverse()
print(li_a)

# remove 删除列表中的第一个指定元素
li_a.remove('b')
print(li_a)

# sort 对列表进行排序
li_a.sort()
print(li_a)

# index 返回所检索元素的索引，可进行切片检索
li_b = ['z','b','c','b','d']
print(li_b.index('b'))
print(li_b.index('b',2,4))

#extend  扩展数据进入原列表
li_a.extend(li_b)
print(li_a)

# clear 删除列表中的所有元素
li_b.clear()
print(li_b)

