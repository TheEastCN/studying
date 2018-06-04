# -*- coding:utf-8 -*-
import functools

def fun1(n):
    return n * n


l = list(range(10))
m = map(fun1, l)
print(list(m))


f = map(lambda s: s * s, l)
print(list(f))

fi = filter(lambda x:x > 3,l)
print(fi)

re = functools.reduce()