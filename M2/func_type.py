# -*- coding:utf-8 -*-

def type_func(args):
    
    for i in args:
        if i is None:
            print('%s 元素为空'%i)
        else:
            print('%s 元素均不为空'%i)
            
type_func([1,None,3])