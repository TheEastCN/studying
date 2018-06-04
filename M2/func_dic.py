# -*- coding:utf-8 -*-


def dic_func(arg):

    for key_dic in arg:
        if type(arg[key_dic]) is str or type(arg[key_dic]) is list:
            if len(arg[key_dic]) > 2:
                arg[key_dic] = arg[key_dic][:2]
        else:
            print('类型错误')

    return arg

dic_test = {'key1':'2222','key2':'33','key3':[1,2,3,4]}
dic_1 = dic_func(dic_test)

print(dic_1)